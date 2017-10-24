"""Grundläggande övningar."""


def sum_of_digits(x):
    """Summera alla värdesiffrorna i ett heltal.

    Exempel: 389 består av 3, 8 och 9 och resultatet blir 3 + 8 + 9 = 20
    """
    s = 0
    while x:
        s += x % 10
        x //= 10
    return s


def binary_string_to_int(s):
    """Översätt en sträng med ett binärt tal till ett heltal."""
    return int(s, 2)


def count_numbers_and_letters(s):
    """Räkna antalet bokstavstecken och siffersymboler i strängen `s`.

    Resultatet returneras som en dictionary med nycklarna 'letters' och
    'numbers'.
    """
    dict = {'letters': 0, 'numbers': 0}
    dict['letters'] = sum(c.isalpha() for c in s)
    dict['numbers'] = sum(c.isdigit() for c in s)
    return dict


def sum_of_cubes(x):
    """Summera all kuber (i^3) av heltalen från 1 till och med `x`.

    Exempel:
    x = 4: 1^3 + 2^3 + 3^3 + 4^3 = 100
    """
    soc = 0
    while x > 0:
        soc += x**3
        x = x - 1
    return soc
