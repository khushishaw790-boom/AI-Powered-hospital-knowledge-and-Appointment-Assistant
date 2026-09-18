import asyncio

from fastapi import (
    APIRouter,
    WebSocket,
    WebSocketDisconnect,
)

from app.services.rag import ask_rag
from app.websocket.manager import manager


router = APIRouter()


@router.websocket("/ws/chat")
async def websocket_chat(
    websocket: WebSocket,
):

    await manager.connect(websocket)

    try:

        await manager.send_message(
            websocket,
            {
                "type": "connected",
                "message": "Connected to Hospital AI Assistant",
            },
        )

        while True:

            data = await websocket.receive_json()

            question = data.get(
                "question",
                "",
            ).strip()

            top_k = data.get(
                "top_k",
                5,
            )

            if not question:

                await manager.send_message(
                    websocket,
                    {
                        "type": "error",
                        "message": "Question is required",
                    },
                )

                continue

            await manager.send_message(
                websocket,
                {
                    "type": "status",
                    "message": "Searching hospital knowledge...",
                },
            )

            try:

                result = await asyncio.to_thread(
                    ask_rag,
                    question,
                    top_k,
                )

                await manager.send_message(
                    websocket,
                    {
                        "type": "answer",
                        "answer": result["answer"],
                        "sources": result["sources"],
                    },
                )

            except Exception as error:

                await manager.send_message(
                    websocket,
                    {
                        "type": "error",
                        "message": f"AI processing failed: {str(error)}",
                    },
                )

    except WebSocketDisconnect:

        manager.disconnect(websocket)

    except Exception:

        manager.disconnect(websocket)