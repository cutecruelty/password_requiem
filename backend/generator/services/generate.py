import secrets
import string

# classic password generation 

# excluding symbols commonly not accepted by website login forms
excluded = "`~|\\"
safe_punctuation = ''.join(c for c in string.punctuation if c not in excluded)

pool = string.ascii_letters + string.digits + safe_punctuation


def generate_password(length: int, pool: str) -> str:
    return ''.join(secrets.choice(pool) for _ in range(length))


# passphrase generation 

def load_wordlist(path: str) -> list[str]:
    with open(path) as f:
        return [line.strip() for line in f if line.strip()]


def generate_passphrase(word_count: int, wordlist: list[str]) -> str:
    return " ".join(secrets.choice(wordlist) for _ in range(word_count))


# manual test
if __name__ == "__main__":
    password_length = 16
    password = generate_password(password_length, pool)
    print("password:", password)

    wordlist = load_wordlist("wordlist.txt")
    word_count = 8
    passphrase = generate_passphrase(word_count, wordlist)
    print("passphrase:", passphrase)