FROM python:3

# Set environment variables
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /

# Install dependencies.
RUN pip install -r /requirements.txt

# Set work directory.
RUN mkdir /code
WORKDIR /code



COPY ./docker-entrypoint.sh ./docker-entrypoint.sh

# Copy project code.
COPY . /code/

# run docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]


EXPOSE 8080

CMD ["uwsgi", "--http", ":8080", "--ini", "./uwsgi/uwsgi.ini"]