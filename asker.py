from emotion_recognizer import EmotionRecognizer
import datetime


class Asker:
    def __init__(
        self,
        session_id: str,
        session_start_date: datetime,
        session_duration: datetime,
        give_feedback: bool,
        feedback_timeout: datetime,
    ):
        self.session_id = session_id
        self.session_start_date = session_start_date
        self.session_duration = session_duration
        self.session_end_date = self.session_start_date + datetime.timedelta(
            hours=self.session_duration.hour,
            minutes=self.session_duration.minute,
            seconds=self.session_duration.second,
        )
        self.give_feedback = give_feedback
        self.feedback_timeout = feedback_timeout
        self.dates_of_feedbacks = []
        feedback_timeout_hours = self.feedback_timeout.hour
        feedback_timeout_minutes = self.feedback_timeout.minute
        feedback_timeout_seconds = self.feedback_timeout.second
        last_date_of_feedback = self.session_start_date
        while True:
            last_date_of_feedback = last_date_of_feedback + datetime.timedelta(
                hours=feedback_timeout_hours,
                minutes=feedback_timeout_minutes,
                seconds=feedback_timeout_seconds,
            )
            if last_date_of_feedback > self.session_end_date:
                break
            self.dates_of_feedbacks.append(last_date_of_feedback)

        print(f"\nThere will be {len(self.dates_of_feedbacks)} questions")

    def run_session(self):
        i = 0
        for date_of_feedback in self.dates_of_feedbacks:
            while True:
                if datetime.datetime.now() > date_of_feedback:
                    print(i)
                    i += 1
                    break

    def ask_for_mood(self):
        "TODO write this function"
        pass

    def ask_for_emotion(self):
        "TODO write this function"
        pass
