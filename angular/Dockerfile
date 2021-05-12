#FROM python:3 as django
#ENV PYTHONUNBUFFERED 1
#RUN mkdir /app
#WORKDIR /app
#COPY portal_with_advertisements/requirements.txt /app
#RUN python -m pip install --upgrade pip
#RUN pip install -r requirements.txt
## CMD python manage.py runserver
#
#FROM node:14.1-alpine AS node
#RUN mkdir /app
#COPY angular-app/package.json /app/
#WORKDIR /app
#RUN npm install
#RUN npm install -g @angular/cli
#EXPOSE 4200
#CMD ["./app"]
## CMD npm run start

### Stage 1: build ###

FROM node:12.0-alpine as builder

# Set working directory.
RUN mkdir /app
WORKDIR /app

# Copy app dependencies.
COPY angular-app/package.json angular-app/package-lock.json /app/angular-app/

# Install app dependencies.
RUN npm install --prefix angular-app

# Copy app files.
COPY . /app

# Default build configuration.
ARG configuration=""

# Build app
RUN npm run build --prefix angular-app -- --output-path=./dist/out --configuration $configuration

#FROM node:12.0-alpine as builder
#RUN mkdir /app
#WORKDIR /app
#COPY angular-app/package.json angular-app/package-lock.json /app/angular-app/
#RUN npm install
#RUN npm run build --prod

### Stage 2: delivery ###

FROM nginx:1.15.7-alpine

# Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

# Copy output directory from builder to nginx image.
COPY --from=builder /app/angular-app/dist/out /usr/share/nginx/html

# Copy nginx configuration file.
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf

