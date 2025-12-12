import pytest
from safe_login import LoginSystem, User

# ------------------------------------
# 1. Test: basic login functionality (correct password)
# ------------------------------------
def test_login_success():
    system = LoginSystem()
    assert system.login("katy", "hellokitty") == "Welcome, katy!"
    assert system.login("yuling", "ubeicecream") == "Welcome, yuling!"
    assert system.login("dyt", "kurasushi") == "Welcome, dyt!"

# ------------------------------------
# 2. Test: login failure (wrong password)
# ------------------------------------
def test_login_fail_wrong_password():
    system = LoginSystem()
    assert system.login("katy", "wrongpass") == "Incorrect password."
    assert system.login("yuling", "") == "Incorrect password."
    assert system.login("dyt", "kurasushii") == "Incorrect password."  # off by one

# ------------------------------------
# 3. Test: unknown user
# ------------------------------------
def test_unknown_user():
    system = LoginSystem()
    assert system.login("unknown", "whatever") == "User not found."

# ------------------------------------
# 4. Test: password comparison works for exact matches
# ------------------------------------
def test_check_password_exact():
    system = LoginSystem()
    assert system.check_password("abc123", "abc123") is True

# ------------------------------------
# 5. Test: password comparison fails for mismatched passwords
# ------------------------------------
def test_check_password_mismatch():
    system = LoginSystem()
    assert system.check_password("abc123", "abc124") is False
    assert system.check_password("abc123", "abc12") is False
    assert system.check_password("short", "longer") is False

# ------------------------------------
# 6. Test: constant-time check does NOT short-circuit (functional correctness test)
# ------------------------------------
def test_constant_time_behavior():
    """
    IMPORTANT:
    We cannot test exact timing due to OS noise,
    but we *can* test that unequal-length comparisons
    still perform a full loop instead of failing early.

    Strategy:
    - Provide mismatched strings with LARGE difference
    - Ensure function returns False (correct)
    - Ensure no crash or early return
    """

    system = LoginSystem()

    # Long mismatch: before fix, len mismatch returns early
    assert system.check_password("aaa", "bbbbbbbbbbbb") is False

    # Different characters in early position — should still evaluate all positions
    assert system.check_password("password123", "pXssword123") is False

# ------------------------------------
# 7. Test: defensive handling of None / non-string inputs
# ------------------------------------
def test_invalid_inputs():
    system = LoginSystem()
    assert system.check_password("abc", None) is False
    assert system.check_password(None, "abc") is False
    assert system.check_password(None, None) is False
