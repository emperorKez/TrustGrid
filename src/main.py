from fastapi import FastAPI

from src.features.fraud_detection.router import router as fraud_router

app = FastAPI(
    title="TrustGrid API",
    description="A Scalable, Real-Time Fraud Detection Microservice API",
    version="0.1.0",
)

app.include_router(fraud_router, prefix="/api/v1/fraud", tags=["Fraud Detection"])

@app.get("/")
def read_root():
    return {"message": "Welcome to TrustGrid API"}
