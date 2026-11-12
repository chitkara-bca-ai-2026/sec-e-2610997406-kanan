username = input("Enter your username: ")
password = input("Enter your password: ")

length_valid = len(password) >= 8
digit_valid = any(char.isdigit() for char in password)
uppercase_valid = any(char.isupper() for char in password)

print("==========================")
print("PASSWORD VALIDATION REPORT")
print("==========================")

print("Username:", username)
print("Password:", "*" * len(password))


if length_valid:
    print("[PASS] Minimum 8 characters")
else:
    print("[FAIL] Minimum 8 characters")

if digit_valid:
    print("[PASS] At least one digit")
else:
    print("[FAIL] At least one digit")

if uppercase_valid:
    print("[PASS] At least one uppercase letter")
else:
    print("[FAIL] At least one uppercase letter")

print("Result")

if length_valid and digit_valid and uppercase_valid:
    print("Password is VALID")
  
else:
    print("Password is INVALID.")