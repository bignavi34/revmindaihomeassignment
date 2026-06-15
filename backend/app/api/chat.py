from fastapi import APIRouter
from app.database import SessionLocal
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.query_service import get_context
from app.services.llm_service import generate_answer

router = APIRouter()


@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest):
    db = SessionLocal()

    try:
        context = get_context(
            request.question,
            db,
        )

        answer = generate_answer(
            request.question,
            context,
        )

        return {
            "answer": answer
        }

    finally:
        db.close()