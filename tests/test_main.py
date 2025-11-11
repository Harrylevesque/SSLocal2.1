import pytest
from httpx import AsyncClient

# ...existing code...
from app.main import app


@pytest.mark.asyncio
async def test_health():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        r = await ac.get("/health")
        assert r.status_code == 200
        assert r.json() == {"status": "ok"}


@pytest.mark.asyncio
async def test_echo():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        r = await ac.post("/echo", json={"message": "hello"})
        assert r.status_code == 200
        assert r.json() == {"echo": "hello"}

