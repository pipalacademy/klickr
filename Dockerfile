FROM python:3.6
LABEL MAINTAINER Nabarun Pal <pal.nabarun95@gmail.com>

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000
ENV FLASK_DEBUG=true
ENV FLASK_ENV=development

CMD ["python", "run.py"]
