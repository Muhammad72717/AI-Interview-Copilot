
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InterviewRequest(BaseModel):
    answer: str

@app.get("/")
def home():
    return {"message": "AI Interview Copilot Running"}

@app.post("/evaluate")
def evaluate(req: InterviewRequest):

    score = min(len(req.answer) * 2, 100)

    return {
        "technical_score": score,
        "feedback": "Strong answer" if score > 70 else "Needs improvement"
    }
