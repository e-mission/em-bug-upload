FROM python:3.9

WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn==20.0.4

CMD [ "gunicorn", "uploader:app", "-b 0.0.0.0:5000" ]
