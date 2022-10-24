import json
import torch
from typing import List
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from pathlib import Path
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=['*'])

BASE_DIR = Path(__file__).resolve(strict=True).parent
__version__ = "0.1.0"


class TensorOut(BaseModel):
    tensor: List[int]


@app.get("/")
def home():
    response = {
        "HealthCheck": "Ok",
        "Version": __version__

    }
    return JSONResponse(content=response, media_type="application/json")


@app.post("/predict", response_model=BaseModel)
async def predict(tensor: TensorOut):
    item = jsonable_encoder(tensor) # Se podría pasar directamente un array
    ts = torch.jit.load(str(BASE_DIR) + '/model/doubleit_model.pt')
    sample_tensor = torch.tensor(item['tensor'])
    tensor = ts(sample_tensor)
    value = tensor.tolist()
    response = json.dumps({'tensor': value})
    return JSONResponse(content=response, media_type="application/json")

