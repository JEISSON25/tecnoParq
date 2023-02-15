FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

# Installing required packages
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    build-base libc-dev linux-headers postgresql-dev zlib zlib-dev \
    python3-dev libffi-dev openssl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

WORKDIR /tecnoParq

COPY . .

EXPOSE 8003

# run entrypoint.sh
ENTRYPOINT ["/tecnoParq/entrypoint.sh"]

# This must be later changed for a production WSGI server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8003"]