import openai

class StoryGenerator:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_story(self, prompt):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        story = response.choices[0].text.strip()
        return story
