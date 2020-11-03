FROM python:3.7

COPY . /app
WORKDIR /app/

# Install Dependencies
RUN pip install -r requirements.txt

ENTRYPOINT python app.py
