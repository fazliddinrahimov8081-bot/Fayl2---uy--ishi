def bank (depozit, foiz, yil):
    foyda = depozit * foiz / 100
    return int(depozit + foyda * yil)
    
print(bank(10000,24, 3))
