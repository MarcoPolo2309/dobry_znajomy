from pathlib import Path
import pickle


class Users:
    def __init__(self):
        self.users = pickle.load(open("./data/users.pickle", "rb"))

    def get_users(self):
        return self.users

    def user_nick_name_available(self, name_to_check: str = None):
        used_names = [user.user_nick_name for user in self.users]
        if name_to_check not in used_names and len(name_to_check) != 0:
            return True
        else:
            return False

    def create_user(
        self,
        user_real_name: str = None,
        user_surname: str = None,
        user_nick_name: str = None,
        user_password: str = None,
    ):
        if self.user_nick_name_available(user_nick_name):
            if len(user_nick_name) != 0 and len(user_password) != 0:
                self.users.append(
                    User(
                        user_real_name=user_real_name,
                        user_surname=user_surname,
                        user_nick_name=user_nick_name,
                        user_password=user_password,
                        logs_path=Path(f"./logs/{user_nick_name}"),
                    )
                )
            else:
                raise ValueError("Invalid user nick name or user password")
        else:
            raise ValueError("User nick name not available")

        with open("./data/users.pickle", "wb") as f:
            pickle.dump(self.users, f, protocol=pickle.HIGHEST_PROTOCOL)

    def delete_user(self, user_nick_name: str = None, user_password: str = None):
        for user in self.users:
            if (
                user.user_nick_name == user_nick_name
                and user.user_password == user_password
                and user.user_nick_name != "admin"
            ):
                self.users.remove(user)

        with open("./data/users.pickle", "wb") as f:
            pickle.dump(self.users, f, protocol=pickle.HIGHEST_PROTOCOL)


class User:
    def __init__(
        self,
        user_real_name: str,
        user_surname: str,
        user_nick_name: str,
        user_password: str,
        logs_path: Path,
    ):
        self.user_real_name = user_real_name
        self.user_surname = user_surname
        self.user_nick_name = user_nick_name
        self.user_password = user_password
        self.logs_path = logs_path
