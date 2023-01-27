FROM python:3-alpine

RUN apk update \
    && apk add libpq \
    && apk add bash



ENV PYTHONDONTWRITEBYTEapp 1
ENV PYTHONUNBUFFERED 1


# Make user and group 'application' that owns /app
RUN addgroup -S application \
    && adduser -S application -G application

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Layers...
COPY LICENSE /app/
COPY manage.py /app/
COPY entrypoint.sh /app/
COPY portal /app/portal
COPY rcos_io /app/rcos_io


RUN chown -R application:application /app \
    && chmod -R 755 /app \
    && chmod u+rx /app/manage.py \
    && chmod u+rx /app/entrypoint.sh

# Set user to 'application'
USER application

ENTRYPOINT ["/app/entrypoint.sh"]