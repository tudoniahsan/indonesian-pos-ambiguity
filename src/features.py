verb_prefixes = ["me", "ber", "di", "ter"]

pronouns = ["saya", "dia", "mereka", "kami", "kamu", "aku", 
            "beliau", "kita", "kalian", "ia"]

modals = ["sudah", "sudah", "akan", "bisa", "harus", "boleh", 
          "mau", "ingin", "sedang", "telah", "pernah"]

def has_predicate(tokens):
    for t in tokens:
        if t in pronouns:
            continue  # skip pronoun, jangan dianggap verba
        for prefix in verb_prefixes:
            if t.startswith(prefix) and len(t) > len(prefix) + 1:
                return True
    return False

def has_pronoun(tokens):
    for t in tokens:
        if t in pronouns:
            return True
    return False

def has_modal(tokens):
    for t in tokens:
        if t in modals:
            return True
    return False

def token_length(tokens):
    return len(tokens)

def extract_features(constituent):
    tokens = constituent.lower().split()
    return {
        "has_predicate": has_predicate(tokens),
        "has_pronoun": has_pronoun(tokens),
        "has_modal": has_modal(tokens),
        "token_length": token_length(tokens)
    }

if __name__ == "__main__":
    contoh = "dia tidak mau pergi"
    fitur = extract_features(contoh)
    print("Contoh kalimat:", contoh)
    print("Fitur:", fitur)