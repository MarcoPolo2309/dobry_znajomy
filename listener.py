from pathlib import Path
from emotion_recognizer import EmotionRecognizer
import datetime


class Listener(EmotionRecognizer):
    def __init__(
        self,
        audio_device,
        emotion_classifier: Path,
        session_start_date: datetime,
        session_duration: datetime,
        give_feedback: bool,
        feedback_timeout: datetime,
        # silent_dates: list[dict],
    ):
        super().__init__(
            session_start_date,
            session_duration,
            give_feedback,
            feedback_timeout,
            # silent_dates,
        )

        self.audio_device = audio_device
        self.emotion_classifier = emotion_classifier

    def listen(self):
        "TODO write this function"
        pass

    def classify(self):
        "TODO write this function"
        pass
