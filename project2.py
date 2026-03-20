import re
import pandas as pd
import matplotlib.pyplot as plt


def check_password_strength(password):
    score = 0

   
    length = len(password) >= 8
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    digit = re.search(r"[0-9]", password)
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

  
    if length:
        score += 1
    if upper:
        score += 1
    if lower:
        score += 1
    if digit:
        score += 1
    if special:
        score += 1


    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return score, strength



password = input("Enter your password: ")

score, strength = check_password_strength(password)

print(f"\nPassword Score: {score}/5")
print(f"Strength: {strength}")


data = {
    "Criteria": ["Length>=8", "Uppercase", "Lowercase", "Digit", "Special Char"],
    "Met": [
        len(password) >= 8,
        bool(re.search(r"[A-Z]", password)),
        bool(re.search(r"[a-z]", password)),
        bool(re.search(r"[0-9]", password)),
        bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    ]
}

df = pd.DataFrame(data)


plt.figure()
plt.bar(df["Criteria"], df["Met"])
plt.title("Password Strength Criteria Check")
plt.xlabel("Criteria")
plt.ylabel("Met (True=1 / False=0)")
plt.xticks(rotation=30)

plt.show()