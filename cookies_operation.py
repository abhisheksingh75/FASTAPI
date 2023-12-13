from fastapi import FastAPI, Response, Request

tags_metadata = [
    {
        "name": "cookies operation",
    }
]

app = FastAPI(openapi_tags=tags_metadata)

@app.post("/set_cookie")
def set_cookie(response: Response):
    response.set_cookie(key="mycookie", value="cookie_value")
    return {"message": "Cookie set"}


@app.get("/get_cookie")
def get_cookie(request: Request):
    cookie_value = request.cookies.get("mycookie")
    return {"cookie_value": cookie_value}


@app.delete("/delete_cookie")
def delete_cookie(response: Response):
    response.delete_cookie(key="mycookie")
    return {"message": "Cookie deleted"}
