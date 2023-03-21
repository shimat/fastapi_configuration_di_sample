class MyFactoryService:
    def __init__(self, config: str) -> None:
        print("MyFactoryService init")
        print(f"{type(config)=}, value={config}")
        self.config_value = str(config)

    def run(self) -> str:
        return self.config_value


class MySingletonService:
    def __init__(self, config: str) -> None:
        print("MySingletonService init")
        print(f"{type(config)=}, value={config}")
        self.config_value = str(config)

    def run(self) -> str:
        return self.config_value
