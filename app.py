from fastapi import FastAPI
from endpoints import router
from containers import Container


container = Container()

app = FastAPI()
app.include_router(router)


@app.on_event("startup")
async def startup_event():
    print("startup_event")
    container.env_config.factory_message.from_env("FACTORY_MESSAGE")
    container.env_config.singleton_message.from_env("SINGLETON_MESSAGE")
    print(f"{container.env_config()=}")
