def abbr(frasa):
    words_of_frasa = frasa.split()
    abbr = ""
    for currentword in words_of_frasa:
        if currentword and currentword[0].isalpha():
            abbr += currentword[0].upper()
    return abbr
frasa = "я люблю питон"
print(abbr(frasa))
