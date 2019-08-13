FROM python:3.6.9-alpine3.10
RUN apk --update add bash nano
COPY app /app/
COPY static/* /app/static/
ENV STATIC_URL /app/static
COPY requirements.txt /app/
WORKDIR /app
RUN chmod 0755 /app/app.py
RUN pip install -r /app/requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
