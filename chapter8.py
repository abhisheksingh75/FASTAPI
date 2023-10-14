from fastapi import FastAPI, Depends, HTTPException

tags_metadata = [
    {
        "name": "Chapter 8 - Dependency Injection"
    }
]

app = FastAPI(openapi_tags=tags_metadata)
# Dependency function for request logging
def log_request(request: dict):
    print("Received request:", request)

# Protected POST route using the request logging dependency
@app.post("/log_request/")
async def log_request_data(
    request_data: dict = Depends(log_request)
):
    return {"message": "Request logged successfully", "request_data": request_data}
