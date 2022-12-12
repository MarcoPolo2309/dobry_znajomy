from emotion_recognizer import EmotionRecognizer
import datetime


class Asker(EmotionRecognizer):
    def __init__(
        self,
        mood_scale_max_value: int,
        session_start_date: datetime,
        session_duration: datetime,
        give_feedback: bool,
        feedback_timeout: datetime,
        silent_dates: list[dict],
    ):
        super().__init__(
            session_start_date,
            session_duration,
            give_feedback,
            feedback_timeout,
            silent_dates,
        )

        self.mood_scale_max_value = mood_scale_max_value
        self.emotion_question = (
            f"How you rate your current mood in scale 1 to {self.mood_scale_max_value}?"
        )

    def ask_for_mood(self):
        "TODO write this function"
        pass

    def ask_for_emotion(self):
        "TODO write this function"
        pass
