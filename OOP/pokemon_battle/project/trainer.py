from typing import List

from OOP.guild_system.project import Pokemon


class Trainer:

    def __init__(self, name):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)

            return f"Caught {pokemon.pokemon_details()}"

        else:
            return 'This pokemon is already caught'

    def release_pokemon(self, pokemon_name):
        try:
            pokemon = [p for p in self.pokemons if p.name == pokemon_name][0]
            self.pokemons.remove(pokemon)
            return f"You have released {pokemon_name}"
        except IndexError:
            return f"Pokemon is not caught"

    def trainer_data(self):
        result = ''
        result += f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"
        result += "\n".join(f"- {Pokemon.pokemon_details(p)}" for p in self.pokemons)
        return result


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))

print(trainer.trainer_data())
