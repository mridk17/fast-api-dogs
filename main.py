from enum import Enum
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class DogType(str, Enum):
    terrier = "terrier"
    bulldog = "bulldog"
    dalmatian = "dalmatian"


class Dog(BaseModel):
    name: str
    pk: int
    kind: DogType


class Timestamp(BaseModel):
    id: int
    timestamp: int


dogs_db = {
    0: Dog(name='Bob', pk=0, kind='terrier'),
    1: Dog(name='Marli', pk=1, kind="bulldog"),
    2: Dog(name='Snoopy', pk=2, kind='dalmatian'),
    3: Dog(name='Rex', pk=3, kind='dalmatian'),
    4: Dog(name='Pongo', pk=4, kind='dalmatian'),
    5: Dog(name='Tillman', pk=5, kind='bulldog'),
    6: Dog(name='Uga', pk=6, kind='bulldog')
}

post_db = [
    Timestamp(id=0, timestamp=12),
    Timestamp(id=1, timestamp=10)
]


@app.get('/')
def root():
    # ваш код здесь
    return {}


@app.get('/dog/')
def dogs(kind: str = None):
    
    dog_kinds = { 'terrier', 'bulldog', 'dalmatian' }
    
    if kind is None or kind in dog_kinds:
        return [dogs_db[key] for key in dogs_db if key is None or dogs_db[key].kind == kind]
    raise HTTPException(status_code=404)

@app.get('/dog/{id}')
def dogs(id: int):
    if id in dogs_db:
        return dogs_db[id]
    raise HTTPException(status_code=404)