"""Doppel-Hashing (double hashing) als Kollisionsbehandlung.

Sondierungsfunktion:      s(x, i) = i * h2(x),          i in N0
Vollstaendige Hashfunktion: h(x, i) = (h1(x) + s(x, i)) mod m

Verwendete Hashfunktionen:
    h1(x) = (3x + 1) mod m
    h2(x) = 1 + (x mod (m - 1))
"""


def h1(x, m):
    """Primaere Hashfunktion."""
    return (3 * x + 1) % m


def h2(x, m):
    """Sekundaere Hashfunktion."""
    return 1 + (x % (m - 1))


def s(x, i, m):
    """Sondierungsfunktion."""
    return i * h2(x, m)


def h(x, i, m):
    """Vollstaendige Hashfunktion h(x, i) = (h1(x) + s(x, i)) mod m."""
    return (h1(x, m) + s(x, i, m)) % m


if __name__ == "__main__":
    m = 13
    while True:
        try:
            x = int(input("x = "))
            i = int(input("i = "))
        except (EOFError, KeyboardInterrupt):
            print()
            break
        except ValueError:
            print("Bitte ganze Zahlen eingeben.")
            continue

        rows = [
            (f"h({x}, {i})", h(x, i, m)),
            (f"h1({x})", h1(x, m)),
            (f"h2({x})", h2(x, m)),
            (f"s({x}, {i})", s(x, i, m)),
        ]
        width = max(len(name) for name, _ in rows)

        print(f"| {'Funktion':<{width}} | Wert |")
        print(f"|{'-' * (width + 2)}|------|")
        for name, value in rows:
            print(f"| {name:<{width}} | {value:>4} |")
        print()
