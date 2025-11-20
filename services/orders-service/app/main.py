from fastapi import FastAPI

app = FastAPI()

@app.get("/orders")
def get_orders():
    return {
        "orders": [
            {"id": 1, "product": "Laptop"},
            {"id": 2, "product": "Monitor"},
            {"id": 3, "product": "Mouse"}
        ]
    }
