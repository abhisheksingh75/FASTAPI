from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import time

app = FastAPI()

class Employee(BaseModel):
    id: int
    name: str
    role: str

# In-memory database simulation
employees_db = []

def send_email_to_admin(employee_data: Employee):
    time.sleep(5)  # Simulate a delay in sending email
    print(f"Email sent to admin: New employee created - {employee_data.name}, Role: {employee_data.role}")

@app.post("/create-employee/")
async def create_employee(employee: Employee, background_tasks: BackgroundTasks):
    employees_db.append(employee.dict())  # Add employee to the in-memory database
    background_tasks.add_task(send_email_to_admin, employee)
    return {"message": f"Employee {employee.name} added successfully"}

@app.get("/employees/")
async def get_employees():
    return employees_db
