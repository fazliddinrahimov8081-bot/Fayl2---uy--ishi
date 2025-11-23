mahsulotlar = {
    "olma": [13000, 14000, 15000],
    "anor": [19000, 22000, 24000, 15000],
    "gilos": [6000, 9000, 5000, 4000],
    "banan": [30000, 28000]
}
def ortacha_narxlar(data):
    for  nom, narxlar in data.items():
      orta = sum(narxlar) / len(narxlar)
      print(f"{nom}: {int(orta)}")
ortacha_narxlar(mahsulotlar)