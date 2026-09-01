from fastapi import FastAPI


app = FastAPI()

@app.get("/hello")
def hello_world():
    return {"Status": "OK", "Message": "Hello, World!"}
