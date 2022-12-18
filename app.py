import datetime
from pathlib import Path

from asker import Asker
from plotter import Plotter


class App:
    def __init__(self):
        return

    def show_logs_path_choice(self):
        for idx, single_logs_path in enumerate(list(Path("./logs").glob("**/*.pkl"))):
            print("\t", f"{str(idx)} - {single_logs_path}")

    def choose_logs_path(self):
        choice = {}
        for idx, single_logs_path in enumerate(list(Path("./logs").glob("**/*.pkl"))):
            choice[str(idx)] = single_logs_path

        user_choice = input("My choice: ")
        logs_path = Path(choice[user_choice])
        return logs_path

    def run_app(self):
        while True:
            print("Welcome to Good Friend! An App to track your emotions and mood!")
            print("Please follow the instrukctions displayed on screen")
            print("You can exit app all the time with Ctrl+C shortcut.")
            try:
                # options "window"
                while True:
                    options = input(
                        "\nWhat would you like to do now?\n\t1 - Start emotion recognition session\n\t2 - See plots for previous sessions\nMy choice: "
                    )
                    if options == "1":
                        # emotion recognition "window"
                        while True:
                            print("\nSet up your session")
                            session_id = input(
                                "\tSession id - alias that will help you recognize this session later: "
                            )

                            session_type = input(
                                "What type of session do you prefer?\n\ta - asker\n\tb - listener\nType: "
                            )

                            print("Session duration")
                            duration_days = input("\tDays: ")
                            duration_hours = input("\tHours: ")
                            duration_minutes = input("\tMinutes: ")

                            hour = (
                                int(duration_days) * 24 + int(duration_hours)
                                if duration_days != "" and duration_hours != ""
                                else 0
                            )
                            minute = (
                                int(duration_minutes) if duration_minutes != "" else 0
                            )
                            session_duration = datetime.time(hour=hour, minute=minute)

                            print("How often do you want to get questions? Every:")
                            question_timeout_hours = input("\tHours: ")
                            question_timeout_minutes = input("\tMinutes: ")
                            question_timeout_seconds = input("\tSeconds: ")

                            hour = (
                                int(question_timeout_hours)
                                if question_timeout_hours != ""
                                else 0
                            )
                            minute = (
                                int(question_timeout_minutes)
                                if question_timeout_minutes != ""
                                else 0
                            )
                            second = (
                                int(question_timeout_seconds)
                                if question_timeout_seconds != ""
                                else 0
                            )
                            question_timeout = datetime.time(
                                hour=hour, minute=minute, second=second
                            )

                            print(
                                "Do you want to get feedback (memes)?\n\ty - Yes\n\tn - No"
                            )
                            give_feedback = input("My choice: ")
                            if give_feedback == "y":
                                give_feedback = True
                            else:
                                give_feedback = False

                            if session_type == "a":
                                asker = Asker(
                                    session_id=session_id,
                                    session_start_date=datetime.datetime.now(),
                                    session_duration=session_duration,
                                    give_feedback=give_feedback,
                                    question_timeout=question_timeout,
                                )
                                asker.run_session()
                            else:
                                raise NotImplementedError

                    elif options == "2":
                        # see plots "window"
                        while True:
                            print("Choose, which session you want to display:")
                            self.show_logs_path_choice()
                            logs_path = self.choose_logs_path()
                            plotter = Plotter(logs_path=logs_path)
                            plotter.show_emotion_plots()
                            plotter.show_mood_plots()
                    else:
                        print("Sorry, I didn't recognize this option.")
            except:
                KeyboardInterrupt
                print("\nShutting down gracefully\nGoodbye!")
                break


if __name__ == "__main__":
    app = App()
    app.run_app()
