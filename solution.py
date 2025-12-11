# ---------------------------------------
# 📄 solution_safe_login.py (Intended Solution)
# SafeLogin — Constant-Time Password Comparison Fix
# ---------------------------------------

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
        SECURE CONSTANT-TIME PASSWORD CHECK

        Fixes timing attack vulnerability by:
        - Not returning early when characters differ.
        - Comparing all positions regardless of mismatch.
        - Using accumulated XOR difference instead of early exit.
        """

        # Defensive handling against None
        if actual_pw is None or provided_pw is None:
            return False

        actual_pw = str(actual_pw)
        provided_pw = str(provided_pw)

        # Compare using the maximum length (prevents early mismatch exit)
        max_len = max(len(actual_pw), len(provided_pw))
        diff = 0

        for i in range(max_len):
            # Pad with zero if shorter
            a = ord(actual_pw[i]) if i < len(actual_pw) else 0
            b = ord(provided_pw[i]) if i < len(provided_pw) else 0
            diff |= (a ^ b)

        # Passwords match only if:
        # - All chars equal (diff == 0)
        # - Lengths match
        return diff == 0 and len(actual_pw) == len(provided_pw)

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
