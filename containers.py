from dependency_injector import containers, providers
from services import MyService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["endpoints"])

    env_config = providers.Configuration()

    my_service = providers.Factory(
        MyService,
        config=env_config
    )
