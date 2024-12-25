import random


class MultiversalCalculator:
    """A calculator that operates differently in various universes."""

    def __init__(self):
        self.universes = {
            "Bizarro": self._bizarro_math,
            "Inverse": self._inverse_math,
            "Quantum": self._quantum_math,
            "Randomverse": self._random_math,
        }

    def _bizarro_math(self, a, b, op):
        """In Bizarro Universe, addition means subtraction, and vice versa."""
        if op == "+":
            return a - b
        elif op == "-":
            return a + b
        elif op == "*":
            return b / a if a != 0 else float("inf")
        elif op == "/":
            return a * b
        else:
            return "Bizarro confusion!"

    def _inverse_math(self, a, b, op):
        """In Inverse Universe, all numbers are inverted before calculation."""
        try:
            a, b = 1 / a, 1 / b
        except ZeroDivisionError:
            return "Division by zero in inverse math!"

        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b if b != 0 else "Division by zero in inverse universe!"
        else:
            return "Inverse confusion!"

    def _quantum_math(self, a, b, op):
        """In Quantum Universe, all operations yield Schr├╢dinger's Cat."""
        return "Schr├╢dinger's Cat: Alive or Dead? Who knows?"

    def _random_math(self, a, b, op):
        """In Randomverse, results are entirely random."""
        return random.choice(
            [
                a + b,
                a - b,
                a * b,
                a / b if b != 0 else 0,
                "Totally random bullshit",
            ]
        )

    def calculate(self, universe, a, b, op):
        """Perform calculation in the given universe."""
        if universe not in self.universes:
            return f"Universe '{universe}' not supported!"
        return self.universes[universe](a, b, op)


class ConsoleColors:
  """terminal output coloring done right"""
    def gr(self, string):
        return f"\033[32m{string}\033[0m"

    def rd(self, string):
        return f"\033[31m{string}\033[0m"

    def yl(self, string):
        return f"\033[33m{string}\033[0m"


# Demonstration of MultiverseCalculator
if __name__ == "__main__":
    calculator = MultiversalCalculator()

    try:
        colo = ConsoleColors()

        a = float(input(colo.gr("Enter the first number\t")))
        b = float(input(colo.gr("Enter the second number\t")))
    except Exception:
        print(colo.rd("Invalid Input!"))
        exit(1)
    operation = input(colo.gr("Choose an operation between +, -, * and /\n"))

    if operation == "+":
        print(colo.yl("performing addition"))
    elif operation == "-":
        print(colo.yl("Performing subtraction"))
    elif operation == "*":
        print(colo.yl("Performing multiplication"))
    elif operation == "/":
        print(colo.yl("Performing division"))
    else:
        print(colo.rd("Invalid operation. Lol!"))
        exit(1)

    print(colo.gr("Multiversal Calculator Results:"))
    for universe in calculator.universes.keys():
        result = calculator.calculate(universe, a, b, operation)
        print(colo.yl(f"In {universe} Universe: {result}"))
