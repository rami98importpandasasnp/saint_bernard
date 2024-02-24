from fastapi import FastAPI
from web import adv, channel

app = FastAPI()

app.include_router(adv.router)
app.include_router(channel.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
