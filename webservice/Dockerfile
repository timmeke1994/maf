FROM python:3.6
LABEL maintainer="Tim Fransen tim.fransen@student.hu.nlpy"
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git
RUN mkdir /usr/tim/website \
    && cd /usr/tim/website \
    && git clone https://github.com/timmeke1994/maf.git
