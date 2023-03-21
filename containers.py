from dependency_injector import containers, providers
from services import MyFactoryService, MySingletonService, AService, BService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["endpoints"])

    env_config = providers.Configuration()

    factory_service = providers.Factory(
        MyFactoryService,
        config=env_config.factory_message
    )

    singleton_service = providers.Singleton(
        MySingletonService,
        config=env_config.singleton_message
    )

    conditional_service = providers.Selector(
        env_config.service_switch,
        A=providers.Factory(AService),
        B=providers.Factory(BService),
    )
