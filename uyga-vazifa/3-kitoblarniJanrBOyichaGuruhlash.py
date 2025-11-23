books = [
    ("O'tkan kunlar", "Roman"),
    ("Mehrobdan chayon", "Roman"),
    ("Shum bola", "Povest"),
    ("Alkimyogar", "Roman"),
    ("Boy va kambag'al", "Hikoya"),
    ("Urush va tinchlik", "Roman"),
    ("Kecha va kunduz", "Roman"),
    ("Yulduzli tunlar", "Povest"),
    ("Qorako'z Majnun", "Hikoya"),
    ("Qalb ko'zi", "Hikoya")
]

natija = {}
for nom, janr in books:
    if janr not in natija:
        natija[janr] = []
    natija[janr].append(nom)
for janr,kitob in natija.items():
    print(janr + ':')
    for k in kitob:
        print(" -", k)
    print()