FROM python:3.9.10-slim

LABEL version="0.0.1" maintainer="migueorg@correo.ugr.es"

RUN groupadd testeo && useradd -ms /bin/bash -g testeo testeo

USER testeo

WORKDIR /home/testeo

RUN python -m pip install --upgrade pip

RUN pip3 install --user pypyr

COPY task.yaml ./

ENV PATH=$PATH:/home/testeo/.local/bin

RUN pypyr task installdeps

WORKDIR /app/test

ENTRYPOINT ["pypyr","task","test"]
