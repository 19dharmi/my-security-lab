import string

def analyze_password(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    print("\n--- Password Analysis ---")
    print("Length: " + str(length))
    print("Has uppercase: " + str(has_upper))
    print("Has lowercase: " + str(has_lower))
    print("Has digits: " + str(has_digit))
    print("Has special chars: " + str(has_special))

    score = 0
    if length >= 8: score += 1
    if length >= 12: score += 1
    if has_upper: score += 1
    if has_lower: score += 1
    if has_digit: score += 1
    if has_special: score += 1

    print("Score: " + str(score) + "/6")

    if score <= 2:
        print("Verdict: WEAK")
    elif score <= 4:
        print("Verdict: MEDIUM")
    else:
        print("Verdict: STRONG")

password = input("Enter a password to analyze: ")
analyze_password(password)
