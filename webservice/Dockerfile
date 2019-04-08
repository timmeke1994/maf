FROM python:latest
USER dockeruser
LABEL maintainer="Tim Fransen tim.fransen@student.hu.nlpy"
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git
RUN mkdir /root/tim/website
RUN cd /root/tim/website
RUN git clone https://github.com/timmeke1994/maf.git
WORKDIR /root/tim/website
RUN pip install flask authomatic requests
EXPOSE 5000
  ENTRYPOINT [ "website" ]
  CMD [ "main.py" ]