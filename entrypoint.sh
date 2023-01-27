#!/usr/bin/env bash
echo "Entrypoint script started Derp"

debug(){
    printf "Debugging\n"
    printf "Current directory: %s\n" "$(pwd)"
    printf "Current user: %s\n" "$(whoami)"
    printf "Current user id: %s\n" "$(id -u)"
    printf "Current group id: %s\n" "$(id -g)"
    printf "Directory listing of /\n%s\n" "$(ls -la /)"
    printf "Directory listing of /app\n%s\n" "$(ls -la /app)"
    printf "Environment variables:\n%s\n" "$(env)"
}

#runforalongtime(){
#    # Run for a long time
#    printf "Running for a long time\n"
#    while true; do
#        sleep 1
#    done
#}

runmigrations(){
    # Running migrations
    printf "Running migrations\n"
    python manage.py migrate
}

createsuperuser(){
    # Create Super User
    printf "Creating super user\n"

    # if not set DJANGO_SUPERUSER_PASSWORD, set it to default
    if [ -z "$DJANGO_SUPERUSER_PASSWORD" ]; then
        export DJANGO_SUPERUSER_PASSWORD="admin"
    fi
    # if not set DJANGO_SUPERUSER_USERNAME, set it to default
    if [ -z "$DJANGO_SUPERUSER_USERNAME" ]; then
        export DJANGO_SUPERUSER_USERNAME="admin"
    fi
    # if not set DJANGO_SUPERUSER_EMAIL, set it to default
    if [ -z "$DJANGO_SUPERUSER_EMAIL" ]; then
        export DJANGO_SUPERUSER_EMAIL="developer@rcos.io"
    fi

    python manage.py createsuperuser --no-input
}


start(){
    # Start the application
    printf "Starting the application\n"
    printf "%s:%s\n" $BIND_ADDRESS $PORT

    # if not set bind address or port
    if [ -z "$BIND_ADDRESS" ]; then
        BIND_ADDRESS="127.0.0.1"
    fi
    if [ -z "$PORT" ]; then
        PORT="8000"
    fi

    # run the application with bind address and port,
    # in compose this will be 0.0.0.0:8000
    python manage.py runserver "$BIND_ADDRESS:$PORT"
}
#

main(){
    debug
    runmigrations
    createsuperuser
    start
#    runforalongtime
}
main