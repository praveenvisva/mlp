# lightweight python
FROM python:3.7-slim

RUN apt-get update

# copy local code to container image
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . . /

RUN ls -la $APP_HOME/

#Install Dependencies

RUN pip install requirements.txt

ENV PORT 5432

# Run the flask service on container startup
# CMD exec gunicorn --bind: $PORT --workers 1 --threads 8 complaints_server
CMD ["python", "complaints_server.py"]