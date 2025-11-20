from fastapi import FastAPI

app = FastAPI()

@app.get("/inventory")
def get_inventory():
    return {
        "inventory": [
            {"item": "Laptop", "stock": 15},
            {"item": "Monitor", "stock": 8},
            {"item": "Mouse", "stock": 42}
        ]
    }
