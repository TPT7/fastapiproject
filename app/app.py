from fastapi import FastAPI

app = FastAPI()

#endpoints
@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}#json response