from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

from .knowledge import find_context
from .llm_service import generate_answer
from .schemas import AssistantRequest, AssistantResponse

app = FastAPI(title="AI Sales Assistant", version="1.0.0")
STATIC_DIR = Path(__file__).parent / "static"


@app.get("/")
def index():
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/api/v1/assistant", response_model=AssistantResponse)
def assistant(payload: AssistantRequest):
    context, source = find_context(payload.message)
    result = generate_answer(payload.message, context)
    return AssistantResponse(**result, source=source)