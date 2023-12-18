from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional

app = FastAPI()


SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Employee(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None
    disabled: Optional[bool] = None
    is_admin: bool = False

temp_db = {
    "alice": {
        "username": "alice",
        "full_name": "Alice Smith",
        "email": "alice@gmail.com",
        "hashed_password": pwd_context.hash("chocoland"),
        "disabled": False,
        "is_admin": True,
    },
     "brian": {
        "username": "brian",
        "full_name": "brian dan",
        "email": "brian@gmail.com",
        "hashed_password": pwd_context.hash("creamland"),
        "disabled": False,
        "is_admin": False,
    }
}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_employee(fake_db, username: str, password: str):
    employee = fake_db.get(username)
    if not employee:
        return False
    if not verify_password(password, employee["hashed_password"]):
        return False
    return employee

def create_access_token(data: dict, user_role: str, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    to_encode.update({"role": user_role})
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    employee = authenticate_employee(temp_db, form_data.username, form_data.password)
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": employee["username"]}, user_role="admin" if employee["is_admin"] else "user", expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_role: str = payload.get("role")
    except JWTError:
        raise credentials_exception
    user = temp_db.get(username)
    if user is None:
        raise credentials_exception
    return {"username": user["username"], "role": token_role}

async def get_current_admin_user(current_user: dict = Depends(get_current_user)):
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Operation not permitted")
    return current_user

@app.delete("/admin/delete-user/{username}")
async def delete_user(username: str, current_admin_user: dict = Depends(get_current_admin_user)):
    if username not in temp_db:
        raise HTTPException(status_code=404, detail="User not found")
    del temp_db[username]
    return {"message": "User deleted successfully"}

# Additional endpoints can be added here
