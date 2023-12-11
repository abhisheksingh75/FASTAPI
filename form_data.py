from fastapi import FastAPI, Form, File, UploadFile, Depends, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

class Book(BaseModel):
    title: str
    author: str

class DocumentUploadForm(BaseModel):
    document_name: str

app = FastAPI()

# Dummy in-memory database
users_db = {}
documents_db = {}

# Endpoint to create a new user
@app.post("/create-user/")
async def create_user(user: User):
    """
    Endpoint to create a new user.

    Parameters:
    - user: An instance of the User model representing user details.

    Returns:
    - A JSON response with the created user details.
    """
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    
    users_db[user.username] = user
    return {"message": f"User {user.username} created successfully", "user_details": user.dict()}

# Endpoint for user login
@app.post("/login/")
async def user_login(username: str = user_login(...), password: str = Form(...)):
    """
    Endpoint to handle user login using a form.

    Parameters:
    - username: The username provided in the form.
    - password: The password provided in the form.

    Returns:
    - A JSON response with the received username and password.
    """
    user = users_db.get(username)
    if user and user.password == password:
        return {"message": "Login successful", "user_details": user.dict()}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

# Endpoint to retrieve all users
@app.get("/users/")
async def get_all_users():
    """
    Endpoint to retrieve details of all users.

    Returns:
    - A JSON response with details of all users.
    """
    return {"users": [user.dict() for user in users_db.values()]}

# Endpoint to retrieve details of a specific user
@app.get("/users/{username}")
async def get_user(username: str):
    """
    Endpoint to retrieve details of a specific user.

    Parameters:
    - username: The username of the user to retrieve.

    Returns:
    - A JSON response with details of the specified user.
    """
    user = users_db.get(username)
    if user:
        return {"user_details": user.dict()}
    else:
        raise HTTPException(status_code=404, detail="User not found")

# Endpoint to retrieve details of all documents
@app.get("/documents/")
async def get_all_documents():
    """
    Endpoint to retrieve details of all documents.

    Returns:
    - A JSON response with details of all documents.
    """
    return {"documents": [document_name for document_name in documents_db]}

# Endpoint to retrieve details of a specific document
@app.get("/documents/{document_name}")
async def get_document(document_name: str):
    """
    Endpoint to retrieve details of a specific document.

    Parameters:
    - document_name: The name of the document to retrieve.

    Returns:
    - A JSON response with details of the specified document.
    """
    document = documents_db.get(document_name)
    if document:
        return {"document_name": document_name, "document_details": document.dict()}
    else:
        raise HTTPException(status_code=404, detail="Document not found")

# Endpoint to upload a document related to a book
@app.post("/upload-document/")
async def upload_document(
    form_data: DocumentUploadForm = Depends(),
    document_file: UploadFile = File(...),
):
    """
    Endpoint to handle document uploads using a form.

    Parameters:
    - form_data: An instance of DocumentUploadForm representing the form data.
    - document_file: The document file provided in the form.

    Returns:
    - A JSON response confirming the successful document upload.
    """
    # Check if the user is authenticated (we may use OAuth2, JWT, etc. for proper authentication)
    if form_data.document_name not in documents_db:
        documents_db[form_data.document_name] = document_file
        return JSONResponse(content={"message": f"Document '{form_data.document_name}' uploaded successfully"})
    else:
        raise HTTPException(status_code=400, detail="Document with the same name already exists")

