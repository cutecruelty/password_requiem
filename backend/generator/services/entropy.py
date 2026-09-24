import math

# entropy calculation logic for password qc

def calculate_entropy(length: int, pool_size: int) -> float:
    # formula: L * log2(R) where L is length and R is pool size
    return length * math.log2(pool_size)

def calculate_passphrase_entropy(word_count: int, wordlist_size: int) -> float:
    # formula: W * log2(N) where W is word count and N is wordlist size
    return word_count * math.log2(wordlist_size)

def strength_label(bits: float) -> str:
    # return string ranking based on cryptographic strength thresholds
    if bits < 40:
        return "weak"
    elif bits < 60:
        return "fair"
    elif bits < 80:
        return "strong"
    else:
        return "strong asf"

# ensuring this runs only if i exceute directly
    
if __name__ == "__main__":
    # isolated execution block for manual validation
    from generate import pool, load_wordlist

    # evaluate raw character array configurations
    password_length = 16
    bits = calculate_entropy(password_length, len(pool))

    # evaluate multi word string configurations
    wordlist = load_wordlist("wordlist.txt")
    word_count = 8
    bits = calculate_passphrase_entropy(word_count, len(wordlist))
