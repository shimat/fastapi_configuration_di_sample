from dependency_injector import providers


class MyService:
    def __init__(self, config: providers.Configuration) -> None:
        print("MyService init")
        self.config_value = config()

    def run(self) -> str:
        return self.config_value
