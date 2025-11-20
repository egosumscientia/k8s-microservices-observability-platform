from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def home():
    # Llama al servicio de autenticación
    auth = requests.post("http://auth-service:8080/login",
                         json={"user": "admin", "password": "123"}).json()

    # Llama a microservicios internos
    orders = requests.get("http://orders-service:8080/orders").json()
    inventory = requests.get("http://inventory-service:8080/inventory").json()

    return {
        "auth": auth,
        "orders": orders,
        "inventory": inventory
    }
