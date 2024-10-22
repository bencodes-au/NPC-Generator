import pytest
from generator import Generator  # Ensure that this import is correct


class FakeManager:
    def __init__(self):
        self.saved_character = None

    def save_character(self, character):
        self.saved_character = character


def test_generate_character_male_warrior(monkeypatch):
    manager = FakeManager()
    generator = Generator(manager)

    answers = {
        "What genre is the world?": {"genre": "Fantasy"},
        "How does this character identify?": {"identity": "Male"},
        "What is this character's main trait?": {"trait": "Strong"},
        "What is this character's background?": {"background": "Warrior"},
        # Add this line
        "Would you like to save this character?": {"save": "Save"}
    }

    def mock_prompt(questions):
        # This assumes `questions` can be a list of question objects
        response = {}
        for question in questions:
            if question.message in answers:
                response[question.name] = answers[question.message][question.name]
            else:
                raise KeyError(f"Unhandled question: {question.message}")
        return response

    monkeypatch.setattr("inquirer.prompt", mock_prompt)
    generator.generate_character()

    assert manager.saved_character is not None
    assert "From a life of swords and sorcery," in manager.saved_character
    assert "he is a Strong Warrior" in manager.saved_character
