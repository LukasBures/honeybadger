from fastapi import APIRouter

router = APIRouter()


@router.get("/ping")
async def pong():
    """
    Sanity check.

    :return: Pong!
    """
    return {"ping": "pong!"}
