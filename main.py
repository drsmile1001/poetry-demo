from typing import Union
from fastapi import FastAPI, Form, Response, Request

app = FastAPI()

default_user = "root"
default_password = "y1ZDezJhorSf5JBbJzpMz08D"

allow_username = "alice"
allow_password = "bob"


@app.post("/user")
async def check_user(username: str = Form(), password: str = Form()):
    if username == default_user and password == default_password:
        return Response("allow administrator management", status_code=200)
    if username == allow_username and password == allow_password:
        return Response(
            "allow", status_code=200, headers={"Content-Type": "text/plain"}
        )
    return Response("deny", status_code=200, headers={"Content-Type": "text/plain"})


@app.post(
    "/vhost",
)
async def check_vhost(request: Request):
    # parse request as plan text
    body = await request.body()
    body = body.decode("utf-8")

    print(body)
    Response("allow", status_code=200)
    # if username == allow_username or username == default_user:
    #     return Response(
    #         "allow", status_code=200, headers={"Content-Type": "text/plain"}
    #     )
    # return Response("deny", status_code=200, headers={"Content-Type": "text/plain"})


@app.post("/resource")
async def check_vhost(
    username: str = Form(),
    vhost: str = Form(),
    resource: str = Form(),
    name: str = Form(),
    permission: str = Form(),
):
    if username == allow_username or username == default_user:
        return Response("allow", status_code=200)
    return Response("deny", status_code=200, headers={"Content-Type": "text/plain"})


@app.post("/topic")
async def check_topic(
    username: str = Form(),
    vhost: str = Form(),
    resource: str = Form(),
    name: str = Form(),
    permission: str = Form(),
    routing_key: str = Form(),
):
    if username == allow_username or username == default_user:
        return Response("allow", status_code=200)
    return Response("deny", status_code=200, headers={"Content-Type": "text/plain"})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8082)
