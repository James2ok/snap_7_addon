FROM python:3.12-slim

# Install dependencies
RUN apt-get update && \
    apt-get install -y gcc g++ && \
    pip install --no-cache-dir python-snap7 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copia gli script dentro il container
COPY app /app
COPY run.sh /run.sh
RUN chmod +x /run.sh
WORKDIR /app

CMD ["/run.sh"]
