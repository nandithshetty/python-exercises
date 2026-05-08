# Exercise 27: Regex Email Validation
# Task: Validate if a string is a correctly formatted email address using regex.

import re

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

if __name__ == "__main__":
    emails = ["john.doe@example.com", "invalid-email@", "user@domain.co.in"]
    for email in emails:
        print(f"Is '{email}' valid? {is_valid_email(email)}")
