from pathlib import Path
import datetime


class Listener:
    def __init__(
        self,
        audio_device,
        emotion_classifier: Path,
        session_start_date: datetime,
        session_duration: datetime,
        give_feedback: bool,
        feedback_timeout: datetime,
    ):

        self.audio_device = audio_device
        self.emotion_classifier = emotion_classifier

    def listen(self):
        "TODO write this function"
        pass

    def classify(self):
        "TODO write this function"
        pass
