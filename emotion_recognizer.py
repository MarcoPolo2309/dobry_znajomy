from pathlib import Path
import datetime
from emotion import Emotion


class EmotionRecognizer:
    def __init__(
        self,
        session_start_date: datetime,
        session_duration: datetime,
        give_feedback: bool,
        feedback_timeout: datetime,
        silent_dates: list[dict],
    ):
        self.session_start_date = session_start_date
        self.session_duration = session_duration
        self.give_feedback = give_feedback
        self.feedback_timeout = feedback_timeout
        self.silent_dates = silent_dates
        self.recognized_emotions = []

    def get_emotions(self):
        return self.recognized_emotions

    def save_emotions_to_logs(self, logs_path: Path):
        "TODO write this function"
        pass
