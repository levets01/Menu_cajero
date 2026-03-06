
print("░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░      ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓██████████████▓▒░░▒▓████████▓▒░") 
print("░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░       ") 
print("░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░       ") 
print("░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░  ") 
print("░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░       ") 
print("░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░       ")
print("░▒▓█████████████▓▒░  ▒▓████████▓▒░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░")
                                                                                                                                                                                                     
intentosmx = 4
saldo = 1000
intentos = 0
contrasenia = 4444

def ver_saldo():
    if not saldo:
        print("saldo \n")
        return

    print("\n---SALDO DISPONIBLE---")
    for nombre, datos in saldo.items():
       
        print("------------------")
    print()

while intentos <= intentosmx:
    user = int(input ("introduce nuemero de cuenta de nequi:"))
    contrasenia_user = int (input("introduce tu pin:"))
    intentos +=1

    
     
    if (contrasenia == contrasenia_user):
        while True:

            print ( "Hola de nuevo  ", user)

            
            print(" ======= WELCOME TO BANK  =======")
            print("||                             ||")
            print("||1. Ver saldo disponible (x)  ||")
            print("||2. Retirar dinero       ( )  ||")
            print("||3. Depositar Dinero     ( )  ||")
            print("||6. Salir                ( )  ||")
            print("||                             ||")
            print("====== FOR CODER RIWI =========")
                
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
            
                print("Su saldo es:", saldo )
            
            if opcion == "2":

                retiro =  int(input(print("Introduzca el valor a retirar: ")))
               
            
    else:
        print("password incorrect X")
        

