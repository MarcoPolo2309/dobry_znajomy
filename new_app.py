import datetime

from user import *
from asker import Asker
from listener import Listener
from emotion import Emotion


def __main__():
    while True:
        print(
            "Welcome to Good Friend! An App to recognize and track your emotions and mood!"
        )
        print("You can exit app all the time with Ctrl+C shortcut.")
        try:
            # options "window"
            while True:
                options = input(
                    "\n\t1 - Start emotion recognition session\n\t2 - See plots for saved logs\n"
                )
                if options == "1":
                    # emotion recognition "window"
                    while True:
                        print("\nSet up your session")
                        session_id = input(
                            "\tSession id - alias that may be used to check this session statistics in the future: "
                        )

                        print("What type of session do you prefer?")
                        session_type = input("\ta - asker\n\tb - listener\n")

                        print("Session duration")
                        duration_days = input("\tDays: ")
                        duration_hours = input("\tHours: ")
                        duration_minutes = input("\tMinutes: ")

                        hour = int(duration_days) * 24 + int(duration_hours)
                        minute = int(duration_minutes)
                        session_duration = datetime.time(hour=hour, minute=minute)

                        print("How often do you want to get questions/feedback? Every:")
                        feedback_timeout_hours = input("\tHours: ")
                        feedback_timeout_minutes = input("\tMinutes: ")
                        feedback_timeout_seconds = input("\tSeconds: ")

                        hour = int(feedback_timeout_hours)
                        minute = int(feedback_timeout_minutes)
                        second = int(feedback_timeout_seconds)
                        feedback_timeout = datetime.time(
                            hour=hour, minute=minute, second=second
                        )

                        if session_type == "a":
                            asker = Asker(
                                session_id=session_id,
                                session_start_date=datetime.datetime.now(),
                                session_duration=session_duration,
                                give_feedback=True,
                                feedback_timeout=feedback_timeout,
                            )
                            asker.run_session()

                elif options == "2":
                    # see plots "window"
                    while True:
                        pass
                else:
                    print("Sorry, I didn't recognize this option.")
        except:
            KeyboardInterrupt
            print("\nShutting down gracefully")
            break


if __name__ == "__main__":
    __main__()
