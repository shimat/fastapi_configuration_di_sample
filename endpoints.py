from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from containers import Container
from services import MyService

router = APIRouter()


class MyResponse(BaseModel):
    message: str


@router.get("/", response_model=MyResponse)
@inject
def my_get(
    search_service: MyService = Depends(Provide[Container.my_service]),
):
    result = search_service.run()
    return MyResponse(message=result)
