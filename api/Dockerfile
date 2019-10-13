FROM python:2

MAINTAINER Vitor Aquino <vitordeaquino@gmail.com>

ADD app.py requirements.txt /
RUN pip install -r ./requirements.txt


CMD [ "python", "./app.py" ]