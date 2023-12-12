from fastapi import FastAPI, Response
from datetime import datetime, timedelta

app = FastAPI()

@app.get("/set_cookie")
def set_cookie(response: Response):
    expires = datetime.now() + timedelta(days=1)
    response.set_cookie(
        key="sessionId1",
        value="a3fWa",
        expires=expires.strftime("%a, %d-%b-%Y %H:%M:%S GMT"),
        max_age=86400,
        path="/",
        secure=True,
        httponly=True,
        samesite="Strict"
    )
    return {"message": f"Cookie set for user"}
