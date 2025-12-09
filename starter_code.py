# ---------------------------------------
# 📄 **starter_code/safe_login.py**
# ---------------------------------------

# safe_login.py
# Simple CodeSafe Challenge on Timing Attack Prevention (Beginner-Friendly)

import time

class User:
    def __init__(self, username, password):
        # In reality, passwords would be hashed.
        self.username = username
        self.password = password

    def __repr__(self):
        return f"User({self.username})"


class LoginSystem:
    def __init__(self):
        # Preloaded test users
        self.users = {
            "katy": User("katy", "hellokitty"),
            "yuling": User("yuling", "ubeicecream"),
            "dyt": User("dyt", "kurasushi"),
        }

    def get_user(self, username):
        return self.users.get(username)

    def check_password(self, actual_pw, provided_pw):
        """
        VULNERABLE PASSWORD CHECK:
        - Returns early if a character does NOT match.
        - This leaks timing information (how long until mismatch).
        - Attackers can guess characters based on response time.

        YOUR TASK:
        Implement this method in *constant time* so that
        the time taken does NOT reveal which characters matched.
        """

        # CURRENT INSECURE VERSION:
        if len(actual_pw) != len(provided_pw):
            return False  # Leaks password length

        # Returns early → vulnerable
        for a, b in zip(actual_pw, provided_pw):
            if a != b:
                return False

        return True

    def login(self, username, password):
        user = self.get_user(username)
        if not user:
            return "User not found."

        if self.check_password(user.password, password):
            return f"Welcome, {username}!"
        else:
            return "Incorrect password."

    def interactive_shell(self):
        print("Welcome to SafeLogin Testing Console")
        print("Type 'quit' at any time to exit.")

        while True:
            username = input("Username: ").strip()
            if username.lower() == "quit":
                break

            password = input("Password: ").strip()
            if password.lower() == "quit":
                break

            start = time.time()
            result = self.login(username, password)
            end = time.time()

            print(result)
            print(f"(Response time: {round(end - start, 5)} seconds)")


if __name__ == "__main__":
    system = LoginSystem()
    system.interactive_shell()
