###############################
############ JUEGO ############
##### --- CODEBREAKER --- #####
## --No--Cerca--Acertaste--  ##
###############################

# El juego funciona de la siguiente manera:
# 1. El ordenador "pensara" un numero de 3 digitos no repetidos
# 2. Tu adivinaras un numero de 3 digitos
# 3. El ordenador devolvera pistas. Las posibles pistas seran:

#   Cerca: Has adivinado el numero correcto pero en la posicion erronea
#   Acertaste: Has acertado el numero correcto en la posicion correcta
#   No: No has acertado ni el numero ni la posicion correcta

# 4. Basandole en las pistas, iras adivinando numeros hasta que rompas el codigo con
# la combinacion perfecta

# Necesitaras investigar un poco para realizar el juego.
# No obstante, aqui hay algunas pistas:

# Intenta averiguar para que sirve este pedazo de codigo y como puede servirte en el juego:
import random
digits = list(range(10))
random.shuffle(digits)
print(digits[:3])
#numero=""+str(digits[0])+str(digits[1])+str(digits[2])
numero = "023"
print(numero)
guess=""

while( not( str( guess ) == numero ) ):
    guess = str( raw_input("Cual es tu suposicion? ") )
    print(guess)
    primero = ( str(guess)[0] == numero[0] ) or ( str(guess)[0] == numero[1] ) or ( str(guess)[0] == numero[2] )
    segundo = ( str(guess)[1] == numero[0] ) or ( str(guess)[1] == numero[1] ) or ( str(guess)[1] == numero[2] )
    tercero = ( str(guess)[2] == numero[0] ) or ( str(guess)[2] == numero[1] ) or ( str(guess)[2] == numero[2] )

    if(guess == numero):
        print("Acertaste: Has acertado el numero correcto en la posicion correcta")
    elif( ( primero ) and ( segundo ) and ( tercero ) ):
        print("Cerca: Has adivinado el numero correcto pero en la posicion erronea")
    else:
        print("No: No has acertado ni el numero ni la posicion correcta")

# Otra pista:
#guess = input("Cual es tu suposicion? ")
#print(guess)

# Piensa en como compararias el valor que obtines del input con el numero aleatorio,
# que formato deberia tener? Ves alguna secuencia?