from pathlib import Path


class User:
    def __init__(self, user_name: str, user_password: str, logs_path: Path):
        self.user_name = user_name
        self.user_password = user_password
        self.logs_path = logs_path
