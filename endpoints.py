from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from containers import Container
from services import MyFactoryService, MySingletonService

router = APIRouter()


class MyResponse(BaseModel):
    factory_result: str
    singleton_result: str


@router.get("/", response_model=MyResponse)
@inject
def my_get(
    factory_service: MyFactoryService = Depends(Provide[Container.factory_service]),
    singleton_service: MySingletonService = Depends(Provide[Container.singleton_service]),
):
    factory_result = factory_service.run()
    singleton_result = singleton_service.run()
    return MyResponse(factory_result=factory_result, singleton_result=singleton_result)
