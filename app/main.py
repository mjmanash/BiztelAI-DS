from fastapi import FastAPI, HTTPException
from app.processor import ChatProcessor
from app.analyzer import ChatAnalyzer
from app.auth import verify_api_key
from fastapi import Depends
from app.models import TranscriptInput
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://manash-biztelai-ds.streamlit.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


processor = ChatProcessor("data/BiztelAI_DS_Dataset_V1.json")
analyzer = ChatAnalyzer(processor.load_data())

@app.get("/")
def root():
    return {"message": "Welcome to BiztelAI DS API"}

@app.get("/summary")
def get_summary(api_key: str = Depends(verify_api_key)):
    return analyzer.get_summary()

@app.post("/analyze")
def analyze_transcript(input: TranscriptInput, api_key: str = Depends(verify_api_key)):
    return analyzer.analyze_transcript(input.transcript_id)
