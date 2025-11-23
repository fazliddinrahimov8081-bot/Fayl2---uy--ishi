users = [
    'Abdulla Abdullaev', 
    'Samandar Asadov', 
    'Shaxnoza Jurayeva', 
    'Ikrom Karimov',
    'Gulnora Xalilova',
    'Ziyoda Yuldashova'
]

men = []
women = []
for ism in users:
    familya = ism.split()[-1]
    if familya.endswith("ov") or familya.endswith("ev"):
        men.append(ism)
    elif familya.endswith("ova") or familya.endswith("eva"):
        women.append(ism)
print("Erkaklar: ", men)
print("Ayollar: ", women)