FROM python:latest
USER root
LABEL maintainer="Tim Fransen tim.fransen@student.hu.nlpy"
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git
RUN mkdir /root/scripts/website
RUN cd /root/scripts/website
RUN git clone https://github.com/timmeke1994/maf.git
WORKDIR /root/scripts/website
RUN pip install flask authomatic requests
EXPOSE 5000
  ENTRYPOINT [ "website" ]
  CMD [ "main.py" ]