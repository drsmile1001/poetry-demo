from fastapi import FastAPI

app = FastAPI()


@app.get("/items/")
def read_item():
    return ["apple", "banana", "cherry"]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8082)
