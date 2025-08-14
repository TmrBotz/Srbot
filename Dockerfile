FROM python:3.10.4-slim-bullseye

# Update and install required packages
RUN apt update && apt upgrade -y && \
    apt-get install -y git curl python3-pip ffmpeg wget bash neofetch software-properties-common && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip3 install --no-cache-dir wheel && \
    pip3 install --no-cache-dir -U -r requirements.txt

WORKDIR /app
COPY . .

CMD flask run -h 0.0.0.0 -p 8000 & python3 -m devgagan
# CMD gunicorn app:app & python3 -m devgagan
