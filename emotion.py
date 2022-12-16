import datetime


class Emotion:
    def __init__(self, emotion_name: str, date_of_occurance: datetime):
        self.emotion_name = emotion_name
        self.date_of_occurance = date_of_occurance


class Mood:
    def __init__(self, mood_level: int, date_of_occurance: datetime):
        self.mood_level = mood_level
        self.date_of_occurance = date_of_occurance
