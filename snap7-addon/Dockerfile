FROM python:3.12-slim

# Install dependencies
RUN apt-get update && \
    apt-get install -y gcc g++ && \
    pip install --no-cache-dir python-snap7 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY app /app
COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD ["/run.sh"]


