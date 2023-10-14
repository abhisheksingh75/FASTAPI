from fastapi import FastAPI, Form

tags_metadata = [
    {
        "name": "Chapter 6 - Building Form data structure"
    }
]

app = FastAPI(openapi_tags=tags_metadata)

@app.post("/submit_form/")
async def submit_form(username: str = Form(...), email: str = Form(...)):
    # Process form data, such as username and email
    return {"username": username, "email": email}


@app.post("/submit_form_with_validation/")
async def submit_form_with_validation(
    username: str = Form(..., min_length=3, max_length=20),
    age: int = Form(..., gt=18, lt=100),
    email: str = Form(..., regex=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$")
):
    # Process form data with custom validation
    return {"username": username, "age": age, "email": email}