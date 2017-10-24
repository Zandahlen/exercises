"""Avancerade övningar."""


def factorial(x):
    """Faktorisera ett tal.

    Returnera en lista med alla faktorer för talet `x`.
    """
    fx = []
    
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
    Kåk         'full house'
    Liten stege 'small_straight'
    Stor stege  'large_straight'
    Yatzy       'yahtzee'
    Chans       'chance'
    """
    pass


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
