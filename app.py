from fastapi import FastAPI
from endpoints import router
from containers import Container


container = Container()
# container.config.hoge.from_env("HOGE_KEY")

app = FastAPI()
app.include_router(router)


@app.on_event("startup")
async def startup_event():
    container.env_config.value.from_env("MY_ENV")
    print("startup_event")
    print(f"{container.env_config.value()=}")
