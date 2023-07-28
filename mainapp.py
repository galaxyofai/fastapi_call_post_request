from fastapi import FastAPI
import uvicorn



app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/text")
def read_item(msg_text: str):
    return {"response":"your text is "+ msg_text}

  
if __name__=='__main__':
    uvicorn.run(app,port=8005)