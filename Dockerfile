FROM python:3.8-alpine

ARG run_env
ENV env $run_env

LABEL "Creator"="DN"

WORKDIR ./usr/docker_img

COPY . .

RUN apk update && apk upgrade && apk add bash

RUN pip install -r requirements.txt

CMD pytest -v -m "$env" -s -v -m development

# Create image: docker build --build-arg run_env=development -t autotests .
# After the image is created we can run the tests: docker run autotests
