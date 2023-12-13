from fastapi import FastAPI, Header


tags_metadata = [
    {
        "name": "Basic header example",
    }
]

app = FastAPI(openapi_tags=tags_metadata)


@app.get("/headers/")
async def read_headers(user_agent: str = Header(None), x_token: str = Header(None)):
    return {"User-Agent": user_agent, "X-Token": x_token}
