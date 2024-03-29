class StrategyExecutor:

    def __init__(self, strategy=None):
        self.strategy = strategy

    def execute(self, arg1, arg2):
        if self.strategy is None:
            print("Strategy not implemented...")
        else:
            self.strategy.execute(arg1, arg2)


class AdditionStrategy:

    def execute(self, arg1, arg2):
        print(arg1 + arg2)

class SubtractStrategy:

    def execute(self, arg1, arg2):
        print(arg1 - arg2)

def main():
    no_strategy = StrategyExecutor()
    addition_strategy = StrategyExecutor(AdditionStrategy())
    subtract_strategy = StrategyExecutor(SubtractStrategy())

    no_strategy.execute(4, 6)
    addition_strategy.execute(4, 6)
    subtract_strategy.execute(4, 6)


if __name__ == "__main__":
    main()