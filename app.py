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

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crawl4ai import AsyncWebCrawler
import asyncio

app = FastAPI()


class URLRequest(BaseModel):
    url: str


@app.post("/crawl")
async def crawl_url(request: URLRequest):
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
async def root():
    return {"message": "Crawler API is running"}
