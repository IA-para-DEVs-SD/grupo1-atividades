from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Cadastro de Produtos")

# Banco de dados em memória
items: list[dict] = []
next_id = 1


class ItemCreate(BaseModel):
    nome: str
    descricao: Optional[str] = None


class Item(ItemCreate):
    id: int


@app.get("/items", response_model=list[Item])
def get_items():
    return items


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: ItemCreate):
    global next_id
    new_item = {"id": next_id, "nome": item.nome, "descricao": item.descricao}
    items.append(new_item)
    next_id += 1
    return new_item


@app.delete("/items/{id}", status_code=204)
def delete_item(id: int):
    for i, item in enumerate(items):
        if item["id"] == id:
            items.pop(i)
            return
    raise HTTPException(status_code=404, detail="Item não encontrado")
