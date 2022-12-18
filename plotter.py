from pathlib import Path
import pickle

import matplotlib.pyplot as plt

from emotion import *


class Plotter:
    def __init__(self, logs_path: Path):
        self.logs_path = logs_path
        with open(self.logs_path, "rb") as logs:
            (self.session_mood_levels, self.session_recognized_emotions) = pickle.load(
                logs
            )

    def show_mood_plots(self):
        only_mood_levels_list = [mood.mood_level for mood in self.session_mood_levels]
        only_dates_list = [mood.date_of_occurance for mood in self.session_mood_levels]
        moods = set(only_mood_levels_list)
        sizes = [only_mood_levels_list.count(mood) for mood in moods]
        explode = [0.1] * len(moods)

        fig1, ax1 = plt.subplots()
        ax1.pie(
            sizes,
            explode=explode,
            labels=moods,
            autopct="%1.1f%%",
            shadow=True,
            startangle=90,
        )
        ax1.axis("equal")
        plt.show()

        x = [date.strftime("%d/%m/%Y %H:%M:%S") for date in only_dates_list]
        y = only_mood_levels_list

        plt.plot(x, y)
        plt.gcf().autofmt_xdate()
        plt.show()

    def show_emotion_plots(self):
        only_emotions_list = [
            emotion.emotion_name for emotion in self.session_recognized_emotions
        ]
        only_dates_list = [
            emotion.date_of_occurance for emotion in self.session_recognized_emotions
        ]
        emotions = set(only_emotions_list)
        sizes = [only_emotions_list.count(emotion) for emotion in emotions]
        explode = [0.1] * len(emotions)

        fig1, ax1 = plt.subplots()
        ax1.pie(
            sizes,
            explode=explode,
            labels=emotions,
            autopct="%1.1f%%",
            shadow=True,
            startangle=90,
        )
        ax1.axis("equal")
        plt.show()

        x = [date.strftime("%d/%m/%Y %H:%M:%S") for date in only_dates_list]
        y = only_emotions_list

        plt.plot(x, y, "bo-")
        plt.gcf().autofmt_xdate()
        plt.show()
