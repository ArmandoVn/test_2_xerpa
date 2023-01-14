# syntax=docker/dockerfile:1
FROM python:3.10

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends gcc

WORKDIR /app

COPY ./requirements.txt /app/
# Install dependencies
RUN pip install -r requirements.txt

# Copy source code
COPY ./soccer_app /app/soccer_app
WORKDIR /app/soccer_app

# Expose the port 8000
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
