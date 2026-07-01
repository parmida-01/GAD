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
    x = int(input("x = "))
    i = int(input("i = "))

    print(f"h1({x})        = {h1(x, m)}")
    print(f"h2({x})        = {h2(x, m)}")
    print(f"s({x}, {i})     = {s(x, i, m)}")
    print(f"h({x}, {i})     = {h(x, i, m)}")
