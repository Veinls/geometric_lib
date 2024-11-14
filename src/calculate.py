import circle
import square
import triangle

figs = {"circle": 1, "square": 1, "triangle": 3}

funcs = ["perimeter", "area"]


def check_sizes(fig, sizes):

    if any(size <= 0 for size in sizes):
        raise ValueError("Sizes must be positive numbers.")

    if fig == "triangle":
        a, b, c = sizes
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("The given sizes do not form a valid triangle.")


def calc(fig, func, size):
    assert fig in figs
    assert func in funcs

    check_sizes(fig, size)

    result = eval(f"{fig}.{func}(*{size})")
    return result


if __name__ == "__main__":
    func = ""
    fig = ""

    while fig not in figs:
        fig = input(f"Enter figure name, available are {list(figs.keys())}:\n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    size = []
    size_count = figs[fig]

    while len(size) != size_count:
        size_input = input(f"Input figure sizes, separated by space ({fig}):\n")
        size = list(map(float, size_input.split()))
