"""Avancerade övningar."""


def factorial(x):
    """Faktorisera ett tal.

    Returnera en lista med alla faktorer för talet `x`.
    """
    fx = []
    d = 2
    if x == 1:
        fx.append(1)
    while x > 1:
        if x % d == 0:
            fx.append(d)
            x = x/d
        else:
            d += 1
    return fx


def yahtzee_score(dice, round):
    """Räkna ut den högsta godkända poäng för den aktuella rundan.

    Argumentet `dice` är en lista med fem heltal med värden 1 till och med 6.
    Argumentet `round` är en sträng med något av värdena i tabellen nedan.

    Runda       Värde
    -----------------
    Ettor       'aces'
    Tvåor       'twos'
    Treor       'threes'
    Fyror       'fours'
    Femmor      'fives'
    Sexor       'sixes'

    Triss       'three_of_a_kind'
    Fyrtal      'four_of_a_kind'
    Kåk         'full_house'
    Liten stege 'small_straight'
    Stor stege  'large_straight'
    Yatzy       'yahtzee'
    Chans       'chance'
    """
    value = 0
    alldice = [1, 2, 3, 4, 5, 6]

    if round == 'yahtzee':
        if dice.pop() == dice.pop() == dice.pop() == dice.pop() == dice.pop():
            value = 50

    if round == 'large_straight':
        value = 40
        while alldice != [1]:
            x = alldice.pop()
            if dice.count(x) != 1:
                value = 0
        """ alternative solution
        if dice.count(6) == 1:
            if dice.count(5) == 1:
                if dice.count(4) == 1:
                    if dice.count(3) == 1:
                        if dice.count(2) == 1:
                            value = 40
        """

    if round == 'small_straight':
        value = 30
        while alldice != [6]:
            x = alldice.pop(0)
            if dice.count(x) != 1:
                value = 0
        """alternative solution
        if dice.count(1) == 1:
            if dice.count(5) == 1:
                if dice.count(4) == 1:
                    if dice.count(3) == 1:
                        if dice.count(2) == 1:
                            value = 30
        """

    if round == 'full_house':
        small_house = False
        big_house = False
        while alldice != []:
            x = alldice.pop()
            if dice.count(x) == 2:
                small_house = True
            if dice.count(x) == 3:
                big_house = True
        if small_house and big_house:
            value = 25

    if round == 'three_of_a_kind':
        while alldice != []:
            x = alldice.pop()
            if dice.count(x) >= 3:
                value = 3 * x

    if round == 'four_of_a_kind':
        while alldice != []:
            x = alldice.pop()
            if dice.count(x) >= 4:
                value = 4 * x

    if round == 'aces':
        value = dice.count(1)
        """ alternative solution
        while dice != []:
            if dice.pop() == 1:
                value += 1
        """

    if round == 'twos':
        value = dice.count(2) * 2

    if round == 'threes':
        value = dice.count(3) * 3

    if round == 'fours':
        value = dice.count(4) * 4

    if round == 'fives':
        value = dice.count(5) * 5

    if round == 'sixes':
        value = dice.count(6) * 6

    if round == 'chance':
        return sum(dice)

    if value > 0:
        return value
    else:
        return False


def blackjack_score(cards):
    """Räkna ut poängen för en korthand i blackjack.

    Argumentet cards anges som lista med strängar där varje sträng
    representerar ett kort. En sådan sträng består av en färg,
    ett bindestreck och en valör.

    Färg    Sträng          Valör   Sträng
    --------------          --------------
    Hjärter H               Ess     E
    Ruter   R               2-10    2-10
    Klöver  K               Knekt   Kn
    Spader  S               Dam     D
                            Kung    K

    Till exempel representeras klöver fem som 'K-5' och spader ess som 'S-E'.

    Om en hand innehåller ess ska den räknas på det sätt som är mest
    fördelaktigt för spelaren.
    """
    pass
