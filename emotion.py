import datetime

valid_emotion_names = ["Anger" "Fear" "Happy" "Sad" "Neutral"]


class Emotion:
    def __init__(self, emotion_name: str, date_of_occurance: datetime):
        # Check if emotion is valid
        if emotion_name not in valid_emotion_names:
            valid_emotion_names_listed = "\n\t".join(valid_emotion_names)
            raise ValueError(
                f"Got emotion: {emotion_name}\nValid emotion names: {valid_emotion_names_listed}"
            )

        self.emotion_name = emotion_name
        self.date_of_occurance = date_of_occurance
