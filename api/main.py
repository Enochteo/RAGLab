from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title='RAGLab API', version='0.1.0')

class AskRequest(BaseModel):
    q: str

class AskResponse(BaseModel):
    answer: str
    citations: list[str] = []

@app.get('/health')
def health():
    return {'status': 'ok'}

@app.post('/ask', response_model=AskResponse)
def ask(payload: AskRequest):
    q = payload.q.strip()
    if not q:
        return AskResponse(answer='Provide an actual response.', citations=[])
    return AskResponse(answer=f'(echo) You asked: {q}', citations=[])