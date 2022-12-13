from pathlib import Path
import pickle


class User:
    def __init__(self, user_name: str, user_password: str, logs_path: Path):
        self.user_name = user_name
        self.user_password = user_password
        self.logs_path = logs_path

        self.users = pickle.load(open("./data/users.pickle", "rb"))

    def user_name_available(self, name_to_check: str = None):
        used_names = [user.user_name for user in self.users]
        if name_to_check not in used_names and len(name_to_check) != 0:
            return True
        else:
            return False

    def create_user(self, user_name: str = None, user_password: str = None):
        if self.user_name_available(user_name):
            if len(user_name) != 0 and len(user_password) != 0:
                self.users.append(
                    User(
                        user_name=user_name,
                        user_password=user_password,
                        logs_path=Path(f"./logs/{user_name}"),
                    )
                )
            else:
                print("Invalid user name or user password")
        else:
            print("User name not available")

        with open("./data/users.pickle", "wb") as f:
            pickle.dump(self.users, f, protocol=pickle.HIGHEST_PROTOCOL)

    def delete_user(self, user_name: str = None, user_password: str = None):
        for user in self.users:
            if (
                user.user_name == user_name
                and user.user_password == user_password
                and user.user_name != "admin"
            ):
                self.users.remove(user)

        with open("./data/users.pickle", "wb") as f:
            pickle.dump(self.users, f, protocol=pickle.HIGHEST_PROTOCOL)
