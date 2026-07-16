#exp-4

def pluralize(noun):
    # Rule 1: Ends with s, x, z, ch, sh
    if noun.endswith("ies") or noun.endswith("es"):
        print("Already plural")
    elif noun.endswith(("s", "x", "z", "ch", "sh")):
        return noun + "es"

    # Rule 2: Ends with consonant + y
    elif noun.endswith("y") and noun[-2].lower() not in "aeiou":
        return noun[:-1] + "ies"

    # Rule 3: Default rule
    else:
        return noun + "s"


# Input
word = input("Enter a noun: ")

# Output
print("Plural form:", pluralize(word))
