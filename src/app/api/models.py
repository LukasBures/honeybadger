from pydantic import BaseModel


class SlackSchema(BaseModel):
    RecordType: str
    Type: str
    TypeCode: int
    Name: str
    Tag: str
    MessageStream: str
    Description: str
    Email: str
    From: str
    BouncedAt: str
