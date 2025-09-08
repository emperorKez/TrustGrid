from fastapi import APIRouter, Depends
from . import schemas, services

router = APIRouter()

@router.post("/detect", response_model=schemas.FraudDetectionResponse)
async def detect_fraud(
    request: schemas.FraudDetectionRequest,
    service: services.FraudDetectionService = Depends(),
):
    return service.detect_fraud(request)
