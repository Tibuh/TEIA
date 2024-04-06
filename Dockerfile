FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install gunicorn 
RUN pip3 install -r requirements.txt

COPY . .
WORKDIR /app/src

ENTRYPOINT [ "gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "main:app" ]