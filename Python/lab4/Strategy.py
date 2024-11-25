class Strategy:
    def execute(self, data):
        raise NotImplementedError("You should implement this method!")

class ConcreteStrategyA(Strategy):
    def execute(self, data):
        print(f"Sorting data in ascending order: {sorted(data)}")

class ConcreteStrategyB(Strategy):
    def execute(self, data):
        print(f"Sorting data in descending order: {sorted(data, reverse=True)}")

class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def do_some_logic(self, data):
        self._strategy.execute(data)
