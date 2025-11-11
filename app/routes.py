from fastapi import APIRouter
from .schemas import EchoIn

router = APIRouter()


@router.get("/health")
async def health():
    return {"status": "ok"}


@router.post("/echo")
async def echo(payload: EchoIn):
    """Simple echo endpoint to validate JSON request/response handling."""
    return {"echo": payload.message}
