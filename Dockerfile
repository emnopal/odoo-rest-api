FROM odoo:14.0

USER root

RUN apt-get update
RUN apt-get install -y nano git build-essential libssl-dev libffi-dev cargo
RUN pip3 install --no-cache-dir --upgrade pip
