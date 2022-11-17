print("¿Queres jugar? Escribe si para comenzar") 
si = "si"
while input(str()) == si:
    import random
    print("Elija una dificultad, 1 para fácil, 2 para intermedio, 3 para dificil 4 para muy difícil")
    dificultad = int(input())
    if dificultad == 1:
             num = random.randint(1,99)
             máx = 99
    elif dificultad == 2: 
         num = random.randint(1,999)
         máx = 999
    elif dificultad == 3:
         num = random.randint(1,999999)
         máx= 999999
    elif dificultad == 4:
         num = random.randint(1,999999999999)
         máx = 999999999999
    else:
         print("no es una dificultad válida")
    def Adivina_el_num(num, guess):
         if num < guess < máx:
             print("Demasiado grande, tu num está entre ", guess, "y 1")
         elif 1 < guess < num:
            print("Demasiado pequeño, tu num está entre", guess, "y ", máx)
         elif guess < 1:
             print("No está entre 1 y ", máx)
             return
         elif guess > máx:
             print("No está entre 1 y ", máx)
             return
         elif guess == num:
             print("Has ganado")
             print("¿Quieres jugar de nuevo? Escribe si para volver a jugar")
             if input(str()) == si:
                print("Allá vamos de nuevo")
             else:
                print("Nos vemos")
             return
         else:
             print("No es un número, inntentalo otra vez")
             return
    numguess = 0
    if dificultad == 1:
         while numguess <= 5:
             print("introduce un número del 1 al ", máx)
             guess = int(input())
             numguess = numguess + 1
             Adivina_el_num(num,guess)
             if numguess == 5:
                print("te quedastes sin intentos, tu número era ", num)
                print("¿Quieres jugar de nuevo? Escribe si para volver a jugar")
                if input(str()) == si:
                    print("Allá vamos de nuevo")
                else:
                    print("Nos vemos")
                    break
    elif dificultad == 2:
         while numguess <= 10:
             print("introduce un número del 1 al ", máx)
             guess = int(input())
             numguess = numguess + 1
             Adivina_el_num(num,guess)
             if numguess == 10:
                 print("te quedastes sin intentos, tu número era ", num)
                 print("¿Quieres jugar de nuevo? Escribe si para volver a jugar")
                 if input(str()) == si:
                    print("Allá vamos de nuevo")
                 else:
                    print("Nos vemos")
                    break
    elif dificultad == 3:
         while numguess <= 15:
             print("introduce un número del 1 al ", máx)
             guess = int(input())
             numguess = numguess + 1
             Adivina_el_num(num,guess)
             if numguess == 15:
                print("te quedastes sin intentos, tu número era ", num)
                print("¿Quieres jugar de nuevo? Escribe si para volver a jugar")
                if input(str()) == si:
                    print("Allá vamos de nuevo")
                else:
                    print("Nos vemos")
                    break
    elif dificultad == 4:
         while numguess <= 25:
             print("introduce un número del 1 al ", máx)
             guess = int(input())
             numguess = numguess + 1
             Adivina_el_num(num,guess)
             if numguess == 25:
                print("te quedastes sin intentos, tu número era ", num)
                print("¿Quieres jugar de nuevo? Escribe si para volver a jugar")
                if input(str()) == si:
                    print("Allá vamos de nuevo")
                else:
                    print("Nos vemos")
                    break
    else:
         print("No es una dificultad válida")
         break
"el rankink no he tenido ni idea de como hacerlo"
