import math
import hashlib
import requests


def get_strength(password):
    def calculate_entropy():
        lower_case = False
        upper_case = False
        number = False
        special = False

        added_possibilities = 0
        length = len(password)
        char_set = set(password)
        characters_used = len(char_set)

        for i in range(length):
            if password[i].islower():
                lower_case = True
            elif password[i].isupper():
                upper_case = True
            elif password[i].isdigit():
                number = True
            else:
                special = True

        if lower_case:
            added_possibilities += 26
        if upper_case:
            added_possibilities += 26
        if number:
            added_possibilities += 10
        if special:
            added_possibilities += 33

        max_entropy = math.log2(added_possibilities) * length
        entropy_value = math.log2(characters_used) * length    

        normalised_value = entropy_value / max_entropy
        entropy = normalised_value * 40

        print(f"Entropy: {entropy}")

        return entropy

    def common_password_checks():
        with open("rockyou.txt", "r", encoding="utf-8", errors="ignore") as file:
            common_passwords = {line.strip("\n") for line in file}

        if password in common_passwords:
            print("The Password is Common")
            return 0
        
        print("The Password is Uncommon")

        return 20

    def check_length_and_variety():
        length = len(password)
    
        if length <= 12:
            length_score = (length - 7) * 2
        else:
            length_score = 8 + (length - 12)
    
        lower_case = any(c.islower() for c in password)
        upper_case = any(c.isupper() for c in password)
        number = any(c.isdigit() for c in password)
        special = any(not c.isalnum() for c in password)

        variety_score = (lower_case + upper_case + number + special) * 3.75

        total_score = length_score + variety_score

        total_score = min(30, total_score)

        print(f"Length Score: {length_score}")
        print(f"Variety Score: {variety_score}")
        print(f"Total Length and Variety Score: {total_score}")

        return total_score

    def leaked_password_checks():
        def sha1_hash(password):
            sha1 = hashlib.sha1()
            sha1.update(password.encode('utf-8'))
            return sha1.hexdigest().upper()

        hash = sha1_hash(password)
        api_url = f"https://api.pwnedpasswords.com/range/{hash[:5]}"
        response = requests.get(api_url)
        hashes = (line.split(':') for line in response.text.splitlines())
        found = any(hash[5:] == h for h, count in hashes)

        if found:
            print("The Password has been Leaked")
            return 0
        
        print("The Password has never been Leaked")

        return 10

    return calculate_entropy() + common_password_checks() + check_length_and_variety() + leaked_password_checks()


password = input("Enter Password: ")

if len(password) < 8:
    print("Password Length is Too Short")
    print("Your Password is Weak")
else:
    score = get_strength(password)

    print(f"Score: {score}")

    if score > 66:
        print("Your Password is Strong")
    elif 33 < score <= 66:
        print("Your Password is Moderate")
    else:
        print("Your Password is Weak")