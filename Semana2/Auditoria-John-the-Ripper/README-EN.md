# 💻 Password Auditing with John the Ripper

## Project Objective
The objective of this project is to demonstrate the vulnerability of weak and common passwords. We used the ethical hacking tool **John the Ripper** to crack password hashes and audit credential security.

## Tools Used
* **John the Ripper:** An open-source password cracking tool.
* **Kali Linux:** A specialized cybersecurity operating system that includes John the Ripper.
* **Text Editor (`nano`):** Used to create and edit the hashes file.

## Analysis Steps

### 1. Creating the Hashes File (`hashes.txt`)
* We created a file named `hashes.txt` containing the MD5 hashes of plaintext passwords.
* **File Content:**

ruben:25d55ad283aa400af464c76d7132072f
test:098f6bcd4621d373cade4e832627b4f6
admin:21232f297a57a5a743894a0e4a801fc3
user:ee11cbb19052e40b07aac0ca060c23ee
guest:a762956c3a07ed5e45a273295b93d258

### 2. Executing the Dictionary Attack
* The following command was executed in the Kali Linux terminal to audit the file:
* `john --format=Raw-MD5 hashes.txt`
* The program started its process and, upon finding a match in its dictionary, displayed it on the screen.

### 3. Analysis of the Output
* The output was as follows:

user             (user)
admin            (admin)
test             (test)


* The program identified that the passwords for the `user`, `admin`, and `test` accounts were the same as their usernames. This demonstrates their extreme weakness.

## Conclusions and Lessons Learned
* **Vulnerability of Weak Passwords:** It was demonstrated that common passwords are very vulnerable to a dictionary attack. John the Ripper cracked them in seconds, which highlights the importance of educating users to create strong passwords.
* **Importance of Hashes and Salts:** The exercise taught us that a hash is a unique "digital fingerprint" of a password. We also understood the concept of "salt" and why its use is crucial to prevent dictionary attacks.
* **Practical Skill:** This project served to master a password auditing tool in a controlled environment, a fundamental skill for any cybersecurity analyst.
