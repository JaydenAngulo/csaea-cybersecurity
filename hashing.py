# Hashing: one way function. Same input --> same output.

import hashlib

password = "monkey400?"

data = password.encode("utf-8")
digest = hashlib.md5(data).hexdigest()

print(f"Password: {password}")
print(f"Hash: {digest}")


# comparing hashed passwords

diff_passwords = ["monkey200?", "monkey300?", "monkey400?", "a"]

for p in diff_passwords:
    data = p.encode("utf-8") # converts plaintext to raw bytes
    digest = hashlib.sha256(data).hexdigest()

    print(f"Password: {p}")
    print(f"Hash: {digest}", "\n")