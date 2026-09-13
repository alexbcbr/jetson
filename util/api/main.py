from fastapi import FastAPI
from fastapi.responses import JSONResponse
from services.customers import get_customers, get_customer_by_id
from services.products import get_product_by_id
from utils.logging import logger

app = FastAPI()


@app.get("/")
def health():
    logger.info("Health check requested")
    return {"message": "API is working"}


@app.get("/customers")
def list_customers():
    logger.info("Fetching customers")
    customers = get_customers()
    logger.info("Returned %d customers", len(customers))
    return {"customers": customers}


@app.get("/customers/{customer_id}")
def get_customer(customer_id: str):
    logger.info("Fetching customer %s", customer_id)
    customer = get_customer_by_id(customer_id)
    if customer is None:
        logger.info("Customer %s not found", customer_id)
        return JSONResponse(status_code=404, content={"error": "Customer not found"})
    return {"customer": customer}


@app.get("/products/{product_id}")
def get_product(product_id: int):
    logger.info("Fetching product %s", product_id)
    product = get_product_by_id(product_id)
    if product is None:
        logger.info("Product %s not found", product_id)
        return JSONResponse(status_code=404, content={"error": "Product not found"})
    return {"product": product}
