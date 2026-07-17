from fastapi import APIRouter

from models.request_models import ChatRequest

from models.response_models import ChatResponse

from services.chat_service import ask_llm

router = APIRouter()

@router.post(
    "/chat",
    response_model=ChatResponse
)


def chat(request: ChatRequest):

    answer = ask_llm(
        request.question
    )

    return ChatResponse(

        answer=answer,

        status="success"
    )

@router.get("/health")

def health():

    return {

        "status":"healthy"

    }