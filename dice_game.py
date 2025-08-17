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
    
    def roll_all(self):
        return [d.roll() for d in self.dice]
    
    def roll_chosen(self,index):
        for i in index:
            self.dice[i].roll()
        return self.values
    
    def is_large_straight(self):
        if sorted(self.values) == [2,3,4,5,6]:
            return True
        else:
            return False
        
    def is_small_straight(self):
        if sorted(self.values) == [1,2,3,4,5]:
            return True
        else:
            return False
        
    def is_full(self):
        counts = sorted([self.values.count(v) for v in set(self.values)])
        if counts == [2,3]:
            return sum(self.values)
        
    def is_poker(self):
        return (self.values.count(v) for v in set(self.values)) == 5

    def is_four_of_a_kind(self):
        return sorted(self.values.count(v) for v in set(self.values)) == [1,4]
    
    @property
    def values(self):
        return [d.value for d in self.dice]
    
# ---------------------Game Logic--------------------------

game = Game()
game.roll_all()
print("Rzut 1 : ",game.values)

for r in range(2,4):
    inp = input("Które kosci przerzucic (1-5 ; Enter/n = brak)? : ")
    to_reroll = parse(inp,n=5)
    if not to_reroll:
        break
    game.roll_chosen(to_reroll)
    print(f"Rzut {r}:",game.values)

print("Koniec rundy! Kości : ",game.values)
