from fastapi.testclient import TestClient
from RAGLab.api.main import app

def test_health():
    client = TestClient(app)
    r = client.get('/health')
    assert r.status_code == 200
    assert r.json()['status'] == 'ok'

def test_ask_echo():
    client = TestClient(app)
    r = client.post('/ask', json={'q': 'hello'})
    assert r.status_code == 200
    assert '(echo) You asked: hello' in r.json()['answer']