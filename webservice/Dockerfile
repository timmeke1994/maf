FROM python:latest
LABEL maintainer="Tim Fransen tim.fransen@student.hu.nl"

# Installing latest updates 
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git
# Creating application source code dir and clone github repo
RUN mkdir -p /var/scripts \
    cd /var/scripts/ &&\
    git clone https://github.com/timmeke1994/maf.git &&\
    cd /var/scripts/maf/webservice

# Setting Homedirectory for container
WORKDIR /var/scripts

# Installing python dependencies
RUN pip install flask authomatic requests

# Exposing ports
EXPOSE 5000

# Running Python Applications
CMD [ "python","main.py" ]