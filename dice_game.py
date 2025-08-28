import random
from parser import parse

class Die:
    def __init__(self,sides=6):
        self.sides = sides
        self.value = None

    def roll(self):
        self.value = random.randint(1,self.sides)
        return self.value
    
class Game:
    def __init__(self,n=5,sides=6):
        self.dice = [Die(sides) for _ in range(n)]
        self.points = 0
        self.available_categories = [
            "Poker", "Kareta", "Full", "Trójka",
            "Dwie pary", "Para",
            "Strit mały", "Strit duży",
            "Suma"
        ]
    
    def roll_all(self):
        return [d.roll() for d in self.dice]
    
    def roll_chosen(self,index):
        for i in index:
            self.dice[i].roll()
        return self.values
    
    def score_large_straight(self):
        s = sorted(self.values)
        return 20 if s == [2,3,4,5,6] else 0

    def score_small_straight(self):
        s = sorted(self.values)
        return 15 if s == [1,2,3,4,5] else 0

    def score_full(self):
        counts = sorted(self.values.count(v) for v in set(self.values))
        return sum(self.values) if counts == [2,3] else 0

    def score_poker(self):
        if len(set(self.values)) == 1:
            v = self.values[0]
            return 40 + 10*v
        return 0

    def score_four_of_a_kind(self):
        for v in set(self.values):
            if self.values.count(v) >= 4:
                return v * 4
        return 0

    def score_three_of_a_kind(self):
        for v in set(self.values):
            if self.values.count(v) == 3:
                return v * 3
        return 0

    def score_two_pairs(self):
        pairs = [v for v in set(self.values) if self.values.count(v) == 2]
        return sum(pairs)*2 if len(pairs) >= 2 else 0

    def score_one_pair(self):
        pairs = [v for v in set(self.values) if self.values.count(v) >= 2]
        if len(pairs) >= 1:
            return 2 * max(pairs)
        return 0

    def score_sum(self):
        return sum(self.values)

    def count_points(self):
        rules = {
            "Poker": self.score_poker,
            "Kareta": self.score_four_of_a_kind,
            "Full": self.score_full,
            "Trójka": self.score_three_of_a_kind,
            "Dwie pary": self.score_two_pairs,
            "Para": self.score_one_pair,
            "Strit mały": self.score_small_straight,
            "Strit duży": self.score_large_straight,
            "Suma": self.score_sum,
        }
        return {name: func() for name, func in rules.items()}


    def round(self):
        self.roll_all()
        print("\nRzut 1 :", self.values)

        for r in range(2, 4):
            inp = input("Które kości przerzucić (1-5 ; Enter/n = brak)? : ")
            to_reroll = parse(inp, n=5)
            if not to_reroll:
                break
            self.roll_chosen(to_reroll)
            print(f"Rzut {r}:", self.values)

        print("Koniec rundy! Kości :", self.values)

        results = self.count_points()
        print("\nDostępne kategorie:")
        for cat in self.available_categories:
            print(f"- {cat}: {results[cat]}")

        choice = input("Wybierz kategorię: ").strip()
        if choice in self.available_categories:
            pts = results[choice]
            self.points += pts
            self.available_categories.remove(choice)
            print(f"Wybrałeś '{choice}' → +{pts} pkt | Razem: {self.points}")
        else:
            print("Nieprawidłowa kategoria (brak zmiany punktów).")
 
    @property
    def values(self):
        return [d.value for d in self.dice]
 
game = Game()

while game.available_categories:
    game.round()
print("\n=== KONIEC GRY ===")
print("Wynik końcowy : ", game.points)
