from fastapi import FastAPI, Query

app = FastAPI()

# Endpoint using FastAPI's Query function with notations
@app.get("/items/")
async def read_item(name: str = Query(..., title="Item Name", description="Name of the item", min_length=3)):
    """
    Read an item with additional notations using FastAPI's Query function.

    Parameters:
    - name: Query parameter representing the item name with notations.

    Example Usage:
    - /items/?name=example_item
    """

    return {"item_name": name}
