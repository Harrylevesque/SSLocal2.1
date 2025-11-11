from pydantic import BaseModel

# ...existing code...
class EchoIn(BaseModel):
    message: str

