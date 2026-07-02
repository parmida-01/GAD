"""Berechnet fuenf Funktionen aus drei ganzzahligen Eingaben.
"""


def f1(a, b, c):
    """Funktion 1."""
    return (a + 2*b + 4*c) % 17  # TODO: Formel einsetzen


def f2(a, b, c):
    """Funktion 2."""
    return c % 7  # TODO: Formel einsetzen


def f3(a, b, c):
    """Funktion 3."""
    return (6*a + 6*b + 2*c) % 7  # TODO: Formel einsetzen


def f4(a, b, c):
    """Funktion 4."""
    return a % 3  # TODO: Formel einsetzen


def f5(a, b, c):
    """Funktion 5."""
    return (2*b + 2*c) % 3  # TODO: Formel einsetzen


if __name__ == "__main__":
    while True:
        try:
            a = int(input("a = "))
            b = int(input("b = "))
            c = int(input("c = "))
        except (EOFError, KeyboardInterrupt):
            print()
            break
        except ValueError:
            print("Bitte ganze Zahlen eingeben.")
            continue

        rows = [
            (f"f1({a}, {b}, {c})", f1(a, b, c)),
            (f"f2({a}, {b}, {c})", f2(a, b, c)),
            (f"f3({a}, {b}, {c})", f3(a, b, c)),
            (f"f4({a}, {b}, {c})", f4(a, b, c)),
            (f"f5({a}, {b}, {c})", f5(a, b, c)),
        ]
        width = max(len(name) for name, _ in rows)

        print(f"| {'Funktion':<{width}} | Wert |")
        print(f"|{'-' * (width + 2)}|------|")
        for name, value in rows:
            print(f"| {name:<{width}} | {value:>4} |")
        print()
