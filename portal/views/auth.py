from django.shortcuts import redirect
from django.core.exceptions import BadRequest
from portal.forms import ChangeEmailForm, UserProfileForm
from portal.services import discord
from django.conf import settings
from portal.models import User
from requests import HTTPError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render
from django.contrib import messages
from django.utils import timezone
from django.core.mail import send_mail
from django.urls import reverse


@login_required
def profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            messages.success(request, "Your profile was updated.")
            form.save()
    else:
        form = UserProfileForm(instance=request.user)

    return render(
        request,
        "portal/auth/profile.html",
        {"form": form, "change_email_form": ChangeEmailForm()},
    )


def impersonate(request):
    if settings.DEBUG or request.user.is_superuser:
        email = request.POST["email"]
        user = User.objects.get(email=email)
        login(request, user, backend="django.contrib.auth.backends.ModelBackend")

    return redirect("/")


@login_required
def start_discord_link(request):
    return redirect(discord.DISCORD_OAUTH2_URL)


@login_required
def discord_link_callback(request):
    code = request.GET.get("code")
    if not code:
        raise BadRequest

    try:
        discord_user_tokens = discord.get_tokens(code)
        discord_access_token = discord_user_tokens["access_token"]
        discord_user_info = discord.get_user_info(discord_access_token)
    except HTTPError as error:
        return error

    discord_user_id = discord_user_info["id"]

    request.user.discord_user_id = discord_user_id
    request.user.save()

    return redirect("/")


@login_required
def change_email(request):
    if request.method == "POST":
        form = ChangeEmailForm(request.POST)

        if form.is_valid():
            new_email = form.cleaned_data["new_email"]
            verification_code = "abcd"
            request.session["email_change"] = {
                "new_email": new_email,
                "verification_code": verification_code,
                "expires_at": (
                    timezone.now() + timezone.timedelta(minutes=1)
                ).isoformat(),
            }
            send_mail(
                subject="Verify email address change",
                message=f"""Hi {request.user.first_name or 'RCOS member'}, we received a request to change your primary email to this account.
                If you did not make such a request, please ignore this email. Otherwise, click the link below to confirm the change. Once confirmed, you will only be able to login with this email address and not the original.

                {settings.PUBLIC_BASE_URL}{reverse("verify_change_email")}?verification_code={verification_code}
                """,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[new_email],
                fail_silently=False,
            )

            messages.info(
                request,
                f"Check {new_email} for a verification email to confirm your email change.",
            )
        else:
            messages.warning(
                request,
                "Unable to submit your email change request. That email might already be in use or invalid.",
            )

    return redirect(reverse("profile"))


@login_required
def verify_change_email(request):
    try:
        verification_code = request.GET["verification_code"]
        email_change = request.session.pop("email_change")
        if timezone.datetime.fromisoformat(email_change["expires_at"]) < timezone.now():
            messages.error(
                request, "Your email change request expired. Please try again."
            )
        elif verification_code == email_change["verification_code"]:
            request.user.email = email_change["new_email"]
            request.user.save()
            messages.success(
                request,
                f"You've confirmed your email change to {request.user.email}. Please use this email to login in the future.",
            )
            return redirect(reverse("profile"))
    except:
        messages.error(request, "Could not confirm your email address change.")

    return redirect(reverse("profile"))
