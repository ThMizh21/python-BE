from fastapi import FastAPI
from pydantic import BaseModel

class NewArticle(BaseModel):
    title:str
    description:str
    author:str
    

app = FastAPI( title = "sample" )

@app.get("/")
def hello():
    return{"status" : 200}

@app.get("/v1/articles")
def get_articles():
    return {"data":[]}

@app.get("/v1/articles/{id}")
def get_article_by_id(id:str):
    print(id)
    return {"data":{"id":id}}

@app.post("/v1/articles")
def create_article(new_article:NewArticle):
    print(new_article)
    return{"status":201}

@app.put("/v1/articles/{id}")
def update_article(id:str ,updated_article:NewArticle):
    print(updated_article)
    return{"status":200}

@app.delete("v1/article/{id}")
def delete(id:str):
    print("Record deleted successfully")
    return{"status":200}
