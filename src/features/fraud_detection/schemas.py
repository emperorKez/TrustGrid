from pydantic import BaseModel
from typing import Dict, Any

class FraudDetectionRequest(BaseModel):
    transaction_id: str
    amount: float
    user_id: str
    merchant_id: str
    event_timestamp: str
    features: Dict[str, Any]

class FraudDetectionResponse(BaseModel):
    transaction_id: str
    is_fraud: bool
    score: float
    risk_level: str
    recommendation: str
