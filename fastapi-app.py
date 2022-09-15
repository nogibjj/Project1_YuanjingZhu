from fastapi import FastAPI
import uvicorn
from dblib.querydb import querydb

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to my Databricks sql query!"}


@app.get("/query")
async def query():
    """Excute a SQL query"""

    result = querydb()
    return {"Spending score of customers with $50,000 annual income": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
