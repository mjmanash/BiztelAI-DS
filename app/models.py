from pydantic import BaseModel

class TranscriptInput(BaseModel):
    transcript_id: str
