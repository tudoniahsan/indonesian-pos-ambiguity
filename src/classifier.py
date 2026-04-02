from features import extract_features

def classify(word, constituent):
    fitur = extract_features(constituent)
    
    # Karena, setelah, sebelum, sejak, hingga
    if word in ["karena", "setelah", "sebelum", "sejak", "hingga"]:
        if fitur["has_predicate"] or fitur["has_pronoun"] or fitur["has_modal"]:
            return "CONJ"
        else:
            return "PREP"
    
    # Untuk: CONJ hanya jika ada verba, bukan hanya pronoun/nomina
    elif word == "untuk":
        if fitur["has_predicate"]:
            return "CONJ"
        else:
            return "PREP"
    
    # Dengan: CONJ jika diikuti verba (me-/ber-/di-)
    elif word == "dengan":
        if fitur["has_predicate"]:
            return "CONJ"
        else:
            return "PREP"
    
    # Sampai
    elif word == "sampai":
        if fitur["has_predicate"] or fitur["has_modal"]:
            return "ADV"
        elif fitur["token_length"] == 1:
            return "PREP"
        else:
            return "VERB"
    
    # Akan
    elif word == "akan":
        if fitur["token_length"] == 1 and not fitur["has_predicate"]:
            return "PREP"
        else:
            return "ADV"
    
    # Buat
    elif word == "buat":
        if fitur["has_predicate"]:
            return "CONJ"
        else:
            return "PREP"
    
    # Sama: excluded from rule-based classification
    # Category shift is not determined by the following constituent,
    # requiring structural analysis beyond this system's scope
    elif word == "sama":
        return "EXCLUDED"
    
    else:
        return "UNKNOWN"


if __name__ == "__main__":
    tes = [
        ("karena", "dia tidak mau pergi"),
        ("karena", "alasan kesehatan"),
        ("untuk", "mendaki gunung semeru"),
        ("untuk", "mereka semua"),
        ("dengan", "membawa seorang paranormal"),
        ("dengan", "pak bau"),
    ]
    
    print("=== TEST CLASSIFIER ===")
    for word, constituent in tes:
        hasil = classify(word, constituent)
        print(f"  '{word}' + '{constituent}' → {hasil}")