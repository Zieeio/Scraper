# Crawler API

A FastAPI-based web crawler service that accepts POST requests with URLs and returns the content in markdown format.

## Building the Docker Image

Build the Docker image with the following command:

```bash
docker build -t crawler-app .
```

## Running the Container

### Basic Run

Run the container and expose port 8000:

```bash
docker run -p 8000:8000 crawler-app
```

### Run in Detached Mode

To run the container in the background:

```bash
docker run -d -p 8000:8000 --name crawler crawler-app
```

## API Usage

Once the container is running, the API will be available at `http://localhost:8000`.

### Health Check

Check if the API is running:

```bash
curl http://localhost:8000/
```

### Crawl a URL

Send a POST request to crawl a URL and get markdown content:

```bash
curl -X POST http://localhost:8000/crawl \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

### Example with JSON Output

Using `jq` for formatted JSON output:

```bash
curl -X POST http://localhost:8000/crawl \
  -H "Content-Type: application/json" \
  -d '{"url": "https://ziee.io"}' \
  -s | jq .
```

## API Endpoints

- `GET /` - Health check endpoint
- `POST /crawl` - Crawl a URL and return markdown content
  - Request body: `{"url": "https://example.com"}`
  - Response: `{"markdown": "..."}`

## License

Copyright 2025 Clivern

Licensed under the Apache License, Version 2.0
