import datetime
from pathlib import Path
import pickle
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from emotion import *


class Asker:
    def __init__(
        self,
        session_id: str,
        session_start_date: datetime,
        session_duration: datetime,
        give_feedback: bool,
        question_timeout: datetime,
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
        self.question_timeout = question_timeout

        self.dates_of_questions = []
        question_timeout_hours = self.question_timeout.hour
        question_timeout_minutes = self.question_timeout.minute
        question_timeout_seconds = self.question_timeout.second
        last_date_of_question = self.session_start_date
        while True:
            last_date_of_question = last_date_of_question + datetime.timedelta(
                hours=question_timeout_hours,
                minutes=question_timeout_minutes,
                seconds=question_timeout_seconds,
            )
            if last_date_of_question > self.session_end_date:
                break
            self.dates_of_questions.append(last_date_of_question)

        print(f"\nThere will be {len(self.dates_of_questions)} questions")

        self.session_recognized_emotions = []
        self.emotions = {
            "1": "Anger",
            "2": "Fear",
            "3": "Happy",
            "4": "Sad",
            "5": "Neutral",
        }

        self.session_mood_levels = []
        self.moods = {
            "1": "Very bad",
            "2": "Bad",
            "3": "Not in the mood",
            "4": "Good",
            "5": "Excelent",
        }

    def run_session(self):
        for date_of_question in self.dates_of_questions:
            while True:
                if datetime.datetime.now() > date_of_question:
                    self.ask_for_mood()
                    self.ask_for_emotion()
                    self.feedback()
                    self.save_session_logs()
                    break

    def ask_for_mood(self):
        while True:
            print("How do you feel now?")
            for mood in self.moods.keys():
                print("\t", f"{mood} - {self.moods[mood]}")
            print("\ts - SKIP")

            user_mood = input("Answer: ")
            if user_mood in self.moods.keys():
                mood_level = int(user_mood)
                self.session_mood_levels.append(
                    Mood(
                        mood_level=mood_level, date_of_occurance=datetime.datetime.now()
                    )
                )
                break
            elif user_mood == "s":
                print("Skipping")
                break
            else:
                print("Sorry, I didin't recognize this answer")

    def ask_for_emotion(self):
        while True:
            print("Which emotion do you feel the most now?")
            for emotion in self.emotions.keys():
                print("\t", f"{emotion} - {self.emotions[emotion]}")
            print("\ts - SKIP")

            user_emotion = input("Answer: ")
            if user_emotion in self.emotions.keys():
                emotion = self.emotions[user_emotion]
                self.session_recognized_emotions.append(
                    Emotion(
                        emotion_name=emotion, date_of_occurance=datetime.datetime.now()
                    )
                )
                break
            elif user_emotion == "s":
                print("Skipping")
                break
            else:
                print("Sorry, I didin't recognize this answer")

    def feedback(self):
        memes_paths = list(Path("./data/memes").glob("*"))
        if self.give_feedback:
            meme_path = random.choice(memes_paths)
            img = mpimg.imread(meme_path)
            imgplot = plt.imshow(img)
            plt.show()

    def save_session_logs(self):
        file_name_date = self.session_start_date.strftime("%Y_%m_%d/%H_%M_%S")
        logs_path = Path(f"./logs/{file_name_date}_{self.session_id}.pkl")
        logs_path.parent.mkdir(exist_ok=True, parents=True)

        with open(logs_path, "wb") as f:
            pickle.dump(
                (self.session_mood_levels, self.session_recognized_emotions),
                f,
                protocol=pickle.HIGHEST_PROTOCOL,
            )
