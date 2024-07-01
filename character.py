class Character:
    def __init__(self, name, race, character_class):
        self.name = name
        self.race = race
        self.character_class = character_class

    @staticmethod
    def create_character():
        name = input("Enter your character's name: ")
        race = input("Enter your character's race: ")
        character_class = input("Enter your character's class: ")
        
        return Character(name, race, character_class)
