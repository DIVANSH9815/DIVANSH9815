def show_rules():
    print("• Password must be at least 8 characters long")
    print("• Must contain at least one uppercase and one lowercase letter")
    print("• Must contain at least one number")
    print("• Must contain at least one special character")

def check_password_strength(password: str) -> int:
    """Return a strength score for the password."""
    special = "!@#$%^&*()_-+={}[]|\\:;'<?/>,.~`"
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password) and any(c.islower() for c in password):
        score += 2
    score += sum(c.isdigit() for c in password)
    score += sum(c in special for c in password)
    return score

def password_strength_message(score: int):
    """Print password strength message based on score."""
    if score <= 4:
        print("Password is barely strong enough to qualify.")
    elif score >= 15:
        print("Didn't know passwords could be this unhackable!")
        print("( ˶ˆᗜˆ˵ )")
    elif score >= 12:
        print("Password is very very strong")
        print("ᕙ( •̀ ᗜ •́ )ᕗ")
    elif score >= 8:
        print("Password is very secure")
    else:
        print("Password is valid")

# Main loop
while True:
    password = input("Enter password: ")
    score = check_password_strength(password)

    if score > 0 and len(password) >= 8 \
       and any(c.isupper() for c in password) \
       and any(c.islower() for c in password) \
       and any(c.isdigit() for c in password) \
       and any(c in "!@#$%^&*()_-+={}[]|\\:;'<?/>,.~`" for c in password):

        print("Password is valid")
        password_strength_message(score)
        break
    else:
        show_rules()
        print("Try again.\n")
    
