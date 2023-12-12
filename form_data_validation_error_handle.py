from fastapi import FastAPI, Form, HTTPException

tags_metadata = [
    {
        "name": "Form data validation"
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
    try:
        return {"username": username, "email": email}
    except ValidationError as e:
        # add console 
        print(e.json())
        raise HTTPException(status_code=422, detail=str(e.errors()))