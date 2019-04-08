FROM python:3.7
LABEL maintainer="Tim Fransen tim.fransen@student.hu.nlpy"
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git
RUN mkdir -p /var/scripts/website
RUN cd /var/scripts/website
RUN git clone https://github.com/timmeke1994/maf.git
WORKDIR /var/scripts/website/maf/webservice
RUN pip install flask authomatic requests
EXPOSE 5000
  ENTRYPOINT [ "website" ]
  CMD [ "main.py" ]