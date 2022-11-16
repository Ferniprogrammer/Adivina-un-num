import random
print("Elija una dificultad, 1 para fácil, 2 para intermedio, 3 para dificil 4 para extremo")
dificultad = int(input())
if dificultad == 1:
    num = random.randint(1,99)
    máx = 99
elif dificultad == 2: 
    num = random.randint(1,999)
    máx = 999
elif dificultad == 3:
    num = random.randint(1,999999)
    máx = 999999
elif dificultad == 4:
    num = random.randint(1,999999999999)
    máx = 999999999999
else:
     print("no es una dificultad válida")
def Adivina_el_num(num, guess):
    if num < guess < máx:
        print("Demasiado grande")
    elif 1 < guess < num:
        print("Demasiado pequeño")
    elif guess < 1:
        print("No está entre 1 y ", máx)
    elif guess > máx:
        print("No esté entre 1 y ", máx)
    elif guess == num:
        print("Has ganado")
    else:
        print("No es un número, inntentalo otra vez")
        return
print("introduce un número del 1 al ", máx)
guess1 = int(input())
Adivina_el_num(num,guess1)
print("introduce otro número del 1 al ", máx)
guess2 = int(input())
Adivina_el_num(num,guess2)
print("introduce un último número del 1 al ", máx)
guess3 = int(input())
if num == guess3:
    print("Ganastes :)")
else:
    print("Perdistes, el número era:", num)
  
