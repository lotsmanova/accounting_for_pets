FROM python:3.10

RUN mkdir /app_pet

WORKDIR /app_pet

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/app.sh
