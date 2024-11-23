# Copyright 2025 Clivern
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from fastapi import FastAPI, HTTPException, Header, Depends
from pydantic import BaseModel
from crawl4ai import AsyncWebCrawler

app = FastAPI()

API_KEY = os.getenv("API_KEY")


async def verify_api_key(x_api_key: str = Header(None)):
    """
    Optional API key verification.
    """
    if API_KEY:
        if x_api_key is None:
            raise HTTPException(
                status_code=401,
                detail="API key required. Please provide X-API-Key header.",
            )
        if x_api_key != API_KEY:
            raise HTTPException(status_code=403, detail="Invalid API key.")
    return True


class URLRequest(BaseModel):
    url: str


@app.post("/crawl")
async def crawl_url(request: URLRequest, _: bool = Depends(verify_api_key)):
    """
    Accepts a POST request with a URL and returns the content in markdown format.
    """
    try:
        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(url=request.url)
            if result.markdown:
                return {"markdown": result.markdown}
            else:
                raise HTTPException(
                    status_code=500, detail="Failed to extract markdown content"
                )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error crawling URL: {str(e)}")


@app.get("/")
async def root(_: bool = Depends(verify_api_key)):
    return {"message": "Crawler API is running"}
