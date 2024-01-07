from fastapi import FastAPI
from typing import Dict
from pydantic import BaseModel
import asyncio

app = FastAPI()

class Employee(BaseModel):
    id: int
    name: str
    role: str
    processed: bool = False  

employees_db: Dict[int, Employee] = {}

# Simulate fetching additional data with a delay
async def fetch_additional_data(employee_id: int):
    await asyncio.sleep(2)  # Simulate a delay
    # Adding more data or processing logic here
    return {"info": "Additional data processed"}

async def process_employee_data(employee_id: int):
    if employee_id in employees_db:
        additional_data = await fetch_additional_data(employee_id)
        employee = employees_db[employee_id]
        employee.processed = True  # Update the employee's processed status
        print(f"Processed {employee.name}: {additional_data}")

@app.post("/add-employee")
async def add_employee(employee: Employee):
    employees_db[employee.id] = employee
    return {"message": f"Added employee {employee.name}"}

@app.get("/process-all-employees")
async def process_all_employees():
    await asyncio.gather(*(process_employee_data(emp_id) for emp_id in employees_db))
    return {"message": "Processed all employees"}
