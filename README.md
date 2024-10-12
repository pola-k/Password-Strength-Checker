# Password Strength Checker

## Overview
The Password Strength Checker is a Python-based application designed to evaluate the strength of a given password. It calculates entropy, checks against common passwords, evaluates length and variety, and verifies if the password has been leaked in known data breaches. This tool helps users create stronger, more secure passwords to protect their accounts.

## Features
- **Entropy Calculation**: Measures the randomness of the password based on the character set used and its length.
- **Common Password Checks**: Compares the input password against a list of commonly used passwords to assess its uniqueness.
- **Length and Variety Evaluation**: Scores the password based on its length and the diversity of character types used (lowercase, uppercase, digits, special characters).
- **Leaked Password Verification**: Checks if the password has been exposed in known data breaches using the "Have I Been Pwned" API.

## Technologies Used
- Python 3.x
- Requests library (for API calls)
- Math and Hashlib libraries (for calculations and hashing)

## Getting Started

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.x
- Requests library (can be installed via pip)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/pola-k/password-strength-checker.git
   ```

2. Change into the project directory:
   ```bash
   cd password-strength-checker
   ```

3. Install the required dependencies:
   ```bash
   pip install requests
   ```

4. **Download the Common Password List**:
   - Download the `rockyou.txt` file from the web. This file contains a list of common passwords.
   - Place the `rockyou.txt` file in the project directory (the same directory as the Python script).

### Usage
1. Run the script:
   ```bash
   python password_strength_checker.py
   ```

2. When prompted, enter the password you wish to evaluate.

3. The script will display:
   - Entropy value
   - Length score
   - Variety score
   - Total score
   - Information about the common password check and leaked password check

### Example
```bash
Enter Password: P@ssw0rd123
Entropy: 66.5
Length Score: 10
Variety Score: 15
Total Length and Variety Score: 25
The Password has never been Leaked
Score: 80
Your Password is Strong
```

## Scoring System
- **Strong**: Score greater than 66
- **Moderate**: Score between 33 and 66
- **Weak**: Score less than or equal to 33

## Disclaimer
**This tool is intended for educational purposes only. Always ensure that you are using secure passwords and follow best practices for password management.**
