from environment import StoryGenerator
from character import Character

class Game:
    def __init__(self, api_key):
        self.story_generator = StoryGenerator(api_key)

    def start_game(self):
        print("Welcome to the AI Storytelling Game!")
        character = Character.create_character()
        
        prompt = (
            "You are a narrator in a storytelling game where a "
            f"{character.character_class} named {character.name}, "
            f"a {character.race}, begins an adventure in the world of Dungeons & Dragons. "
            "The journey starts at the entrance of a cave, where the air is thick with anticipation. "
            "Before entering, the group encounters a band of ruthless bandits blocking the path.\n\n"
            "1. Describe the immediate surroundings—the cave's entrance, the bandits, and any notable features.\n"
            "2. Detail the initial skirmish with the bandits. How do they attack? Are there surprises or hidden allies?\n"
            "3. After the battle, prompt the user/player for their next move. Do they enter the cave or explore the surroundings?\n"
            "4. Develop the world further based on the user's choices—introduce new characters, challenges, or plot twists.\n"
            "5. Continue to narrate the story step by step, letting the player influence the direction of the adventure.\n"
            "\nAs the narrator, your role is to bring this DnD adventure to life, reacting dynamically to the user's decisions."
        )

        while True:
            story_segment = self.story_generator.generate_story(prompt)
            print(f"\n{story_segment}\n")
            
            user_input = input("What does your character do next? ")
            prompt += f"\n\n{story_segment}\n\nUser: {user_input}\nAI:"
            
            if user_input.lower() in ['quit', 'exit']:
                print("Thank you for playing!")
                break