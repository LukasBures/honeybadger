import os
import requests
from fastapi.testclient import TestClient
from app.main import app
import json

client = TestClient(app)

SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")


def test_process_spam_payload():
    payload = {
        "RecordType": "Bounce",
        "Type": "SpamNotification",
        "TypeCode": 512,
        "Name": "Spam notification",
        "Tag": "",
        "MessageStream": "outbound",
        "Description": "The message was delivered, but was either blocked by the user, or classified as spam, "
                       "bulk mail, or had rejected content.",
        "Email": "zaphod@example.com",
        "From": "notifications@honeybadger.io",
        "BouncedAt": "2023-02-27T21:41:30Z"
    }
    response = client.post("/slack", json=payload)
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_process_clear_payload():
    payload = {
        "RecordType": "Bounce",
        "MessageStream": "outbound",
        "Type": "HardBounce",
        "TypeCode": 1,
        "Name": "Hard bounce",
        "Tag": "Test",
        "Description": "The server was unable to deliver your message (ex: unknown user, mailbox not found).",
        "Email": "arthur@example.com",
        "From": "notifications@honeybadger.io",
        "BouncedAt": "2019-11-05T16:33:54.9070259Z"
    }
    response = client.post("/slack", json=payload)
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_send_slack_alert():
    email = "test@example.com"
    payload = {"text": f"New spam notification received from {email}"}
    headers = {"Content-type": "application/json"}
    response = requests.post(SLACK_WEBHOOK_URL, data=json.dumps(payload), headers=headers)
    assert response.status_code == 200
