from fastapi import FastAPI

tags_metadata = [
    {
        "name": "Query parameters type conversion",
    }
]

app = FastAPI(openapi_tags=tags_metadata)

# Endpoint with query parameter type conversion
@app.get("/multiply/")
async def multiply_numbers(a: int, b: float):
    """
    Multiply two numbers and return the result.

    Parameters:
    - a: An integer
    - b: A floating-point number

    Example Usage:
    - /multiply/?a=5&b=2.5
    """

    result = a * b

    return {"result": result}
