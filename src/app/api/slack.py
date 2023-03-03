from typing import Final

import requests
import json
from fastapi import APIRouter, HTTPException
import os
from app.api.models import SlackSchema

router = APIRouter()

SPAM_NOTIFICATION_TYPE: Final[str] = "SpamNotification"

try:
    SLACK_WEBHOOK_URL: str = os.getenv("SLACK_WEBHOOK_URL")
except Exception as e:
    raise HTTPException(status_code=400, detail=e)


def send_slack_alert(email) -> dict:
    """
    Send message to Slack channel.

    :param email: Email string.
    :return: status
    """
    try:
        payload: dict = {"text": f"New spam notification received from {email}"}
        headers: dict = {"Content-type": "application/json"}
        response = requests.post(SLACK_WEBHOOK_URL, data=json.dumps(payload), headers=headers)
        response.raise_for_status()
        print(f"Success: Sent Slack alert for spam notification from {email}")
        return {"status": "ok"}
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to send Slack alert. Error: {e}")
        raise HTTPException(status_code=400, detail=f"Failed to send Slack alert. Error: {e}")


@router.post("/slack", status_code=200)
async def process_payload(payload: SlackSchema) -> dict:

    if not payload:
        raise HTTPException(status_code=400, detail="Request body must be in JSON format.")

    if not payload.Type:
        raise HTTPException(status_code=400, detail="Request body must include Type field.")
    if not payload.Email:
        raise HTTPException(status_code=400, detail="Request body must include Email field.")

    if payload.Type is not SPAM_NOTIFICATION_TYPE:
        return send_slack_alert(payload.Email)
