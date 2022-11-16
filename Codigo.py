import random
num = random.randint(1,99)
def Adivina_el_num(num,guess):
    if num < guess < 100:
        print("Demasiado grande")
    elif 1 < guess < num:
        print("Demasiado pequeño")
    elif guess < 1:
        print("No está entre 1 y 100")
    elif guess > 100:
        print("No esté entre 1 y 100")
    elif guess == num:
        print("Has ganado")
    else:
        print("No es un número, inntentalo otra vez")
        return
guess1 = int(input("introduce un número del 1 al 99 "))
Adivina_el_num(num,guess1)
guess2 = int(input("introduce otro número del 1 al 99 "))
Adivina_el_num(num,guess2)
guess3 = int(input("introduce un último número del 1 al 99 "))
if num == guess3:
    print("Ganastes :)")
else:
    print("Perdistes, el número era:")
    print(num)
