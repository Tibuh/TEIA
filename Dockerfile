FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip install --upgrade setuptools

COPY . .

CMD [ "python3", "src/main.py" ]