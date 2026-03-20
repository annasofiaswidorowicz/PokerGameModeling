class PlayingCard:
    SUITS = ["♠", "♥", "♦", "♣"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    def __init__(self, suit, rank):
        if suit not in self.SUITS:
            raise ValueError("Invalid suit")
        if rank not in self.RANKS:
            raise ValueError("Invalid rank")
        self._suit = suit
        self._rank = rank

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    def __str__(self):
        return f"{self.rank}{self.suit}"
    def __repr__(self):
        return self.__str__()

card = PlayingCard("♠", "2")
print(card)

