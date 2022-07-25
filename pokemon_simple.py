# create Pokemon class
class Pokemon:
    def __init__(self, name: str, primary_type: str, max_hp: int) -> None:
        self.name = name
        self.primary_type = primary_type
        self.max_hp = max_hp
        self.hp = max_hp

    def __str__(self) -> str:
        return f"{self.name} ({self.primary_type}): {self.hp}/{self.max_hp} hp"

    def feed(self) -> None:
        if self.hp < self.max_hp:
            self.hp += 1
            print(f"{self.name} has {self.hp} hp")
        else:
            print(f"{self.name} has maximum hp")

    def battle(self, other) -> None:
        print(f"Battle {self.name} VS {other.name}")
        result = self.typewheel(self.primary_type, other.primary_type)
        if result == "lose":
            self.hp -= 10
            print(f"{self.name} lost and has {self.hp} hp")
        print(f"Result: {self.name} {result} with {other.name}")

    @staticmethod
    def typewheel(type1, type2) -> str:
        result = {0: "lose", 1: "win", -1: "draw"}
        # mapping between tpes and result conditions
        game_map = {"water": 0, "fire": 1, "grass": 2}
        #win-lose matrix
        wl_matrix = [
            [-1, 1, 0],#water
            [0, -1, 1], #water
            [1, 0, -1], #grass
        ]
        # decalre winner
        wl_result = wl_matrix[game_map[type1]][game_map[type2]]
        return result[wl_result]


if __name__ == '__main__':
    bulbasaur = Pokemon(name="bulbi", primary_type="grass", max_hp=100)
    charmander = Pokemon(name="charmander", primary_type="fire", max_hp=50)
    print(bulbasaur, charmander)
    bulbasaur.feed()
    bulbasaur.battle(charmander)
    bulbasaur.battle(charmander)
    bulbasaur.battle(charmander)