# Challenge Title: SafeLogin — Patch a Weak Password Check in a Login System
A coding-based challenge focused on software engineering &amp; software security.

Scenario:
Your team is maintaining SafeLogin, a small command-line login system used internally by developers to quickly test user authentication workflows. However, the system has a major problem: passwords are stored and compared in plain text, and the function responsible for checking passwords is vulnerable to timing attacks because it exits early when characters don’t match.

A security engineer filed a report saying that the login system leaks information about the correct password length and characters by returning failure too quickly. Attackers can measure response times and guess the password character-by-character. In real systems, this would be extremely dangerous.

For this challenge, you will fix the timing-attack vulnerability by implementing a constant-time password comparison function.

Your Task:
Modify the provided starter code so that:

Passwords are compared in constant time (no early returns).

Existing login functionality still works normally for correct users.

No extra complexity or hashing is required — just fix the comparison logic.

The program should not crash on unexpected input (empty string, long strings, etc.).
