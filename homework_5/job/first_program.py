from fastapi import FastAPI
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

@app.get("/")
async def home():
    log.info('Обработка GET запроса')
    return {"Home": "Home"}