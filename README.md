## Scraper API

A FastAPI-based web scraper service that accepts POST requests with URLs and returns the content in markdown format.

### Running the Container

Run the container with the API key environment variable:

```bash
docker run -d -p 8000:8000 -e API_KEY=xkey --name scraper clivern/scraper:0.4.0
```

### API Usage

Once the container is running, the API will be available at `http://localhost:8000`.

#### Health Check

Check if the API is running:

```bash
curl -H "X-API-Key: xkey" http://localhost:8000/
```

#### Crawl a URL

Send a POST request to crawl a URL and get markdown content:

```bash
curl -X POST http://localhost:8000/crawl \
  -H "Content-Type: application/json" \
  -H "X-API-Key: xkey" \
  -d '{"url": "https://example.com"}'
```

#### Example with JSON Output

Using `jq` for formatted JSON output:

```bash
curl -X POST http://localhost:8000/crawl \
  -H "Content-Type: application/json" \
  -H "X-API-Key: xkey" \
  -d '{"url": "https://ziee.io"}' \
  -s | jq .
```

### API Endpoints

- `GET /` - Health check endpoint
- `POST /crawl` - Crawl a URL and return markdown content
  - Request body: `{"url": "https://example.com"}`
  - Response: `{"markdown": "..."}`

### License

Copyright 2025 Clivern

Licensed under the Apache License, Version 2.0
