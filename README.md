# How to run

1) Create Slack app: https://api.slack.com/messaging/webhooks#getting_started
2) Create `.env` file (you can use provided `.env.example` file) and enter your Slack webhook URL from the step 1.
3) Install Docker on your machine (desktop or CLI version): https://docs.docker.com
4) Edit `docker-compose.yml` as needed (if needed), e.g. change ports
5) Start API from honeybadger folder with command: `docker-compose up -d --build`
6) You can test if everything working executing the tests: `docker-compose exec web pytest .`
7) Your API is now accessible, you can see Swagger docs here: http://localhost:8002/docs  

# The task: Take-home project for Software Developer position (2023)

**Estimated time:** 1-2 hours

Create a production-ready web endpoint that accepts a JSON payload as a POST request and sends an alert to a Slack channel if the payload matches desired criteria. This project should be straight-forward — please don’t spend more than two hours on it! If anything in the instructions is unclear, please send your questions to us. If you hit the two hour mark and you aren’t done, please send what you have at that point. 

## **Requirements**

- The alert should only be sent to the Slack channel if the payload is a spam notification.
- The Slack alert should include the email address included in the payload

All other decisions are up to you! Pick your preferred platform/language/framework, etc., and don’t feel limited by what’s described here… a little extra polish can go a long way. 😁 

## **Deliverable**

When completing your application, please send a link to your code, including instructions on how to deploy it.

## **Sample Payloads**

### A spam report that should result in an alert
```json
{
  "RecordType": "Bounce",
  "Type": "SpamNotification",
  "TypeCode": 512,
  "Name": "Spam notification",
  "Tag": "",
  "MessageStream": "outbound",
  "Description": "The message was delivered, but was either blocked by the user, or classified as spam, bulk mail, or had rejected content.",
  "Email": "zaphod@example.com",
  "From": "notifications@honeybadger.io",
  "BouncedAt": "2023-02-27T21:41:30Z",
}
```

### A payload that should not result in an alert
```json
{
  "RecordType": "Bounce",
  "MessageStream": "outbound",
  "Type": "HardBounce",
  "TypeCode": 1,
  "Name": "Hard bounce",
  "Tag": "Test",
  "Description": "The server was unable to deliver your message (ex: unknown user, mailbox not found).",
  "Email": "arthur@example.com",
  "From": "notifications@honeybadger.io",
  "BouncedAt": "2019-11-05T16:33:54.9070259Z",
}
```