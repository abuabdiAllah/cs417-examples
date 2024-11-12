from typing import Callable


def approach_zero(f: Callable[[float], float]) -> None:
    """
    Evaluate a given function (f) for x values in the range 1 to 2^(-2000)
    where each value is have the previous one (1, 0.5, 0.25, 0.125...)

    Args:
        f: mathematical function to evaluate
    """

    for i in range(0, 2000):
        x = 2**-i
        f_of_x = f(x)

        #  print("2^-{} / {:>24.20e} | {:>24.20e}".format(i, x, f_of_x))
        print(f"2^-{i:} / {x:>24.20e} | {f_of_x:>24.20e}")


if __name__ == "__main__":

    def f(x: float):
        return x**2 + 7 * x + 3

    #  approach_zero(lambda x: math.cos(x))
    approach_zero(f)
