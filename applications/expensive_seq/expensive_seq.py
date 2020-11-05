# Your code here


class Calculator:
    def __init__(self):
        self.memo = dict()

    def exps(self, x, y, z):
        if x <= 0:
            return y + z
        if x > 0:
            return (
                self.calculate(x - 1, y + 1, z)
                + self.calculate(x - 2, y + 2, z * 2)
                + self.calculate(x - 3, y + 3, z * 3)
            )

    def calculate(self, x, y, z):
        key = (x, y, z)
        if key not in self.memo:
            self.memo[key] = self.exps(x, y, z)
        return self.memo[key]


def expensive_seq(x, y, z):
    calculator = Calculator()
    return calculator.calculate(x, y, z)


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i * 2, i * 3, i * 4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
