from fastapi import FastAPI
import uvicorn
from logic.nlpcore import get_phrases

app = FastAPI()

@app.get("/")
async def root():
    return {"Go to phrases/name to get noun phrases from wikipedia for name"}

@app.get("/phrases/{name}")
async def phrase(name: str):
    """Generate NLP noun phrases from wikipedia for name"""
    print(f"running {name}")
    noun_phrases = get_phrases(name)
    return {"noun_phrases": noun_phrases}


if __name__=="__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")