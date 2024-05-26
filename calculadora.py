#Calculadora usando una funcion con varios input
print("Calculadora")
def mi_calculadora():
       
    calculadora1 = float(input("Ingrese el primer numero\n"))
    operador = input("Ingrese el operador que desea realizar: *, +, -, /\n")  
    calculadora2 = float(input("Ingrese el segundo numero\n"))      

    if operador == "*" :
                print(f"El resutado de la multiplicacion es: {calculadora1 * calculadora2} ")
    elif operador == "/":
                print(f"El resutado de la divicion es: {calculadora1 / calculadora2} ")
    elif operador == "-":
                print(f"El resutado de la resta es: {calculadora1 - calculadora2} ")    
    elif operador=="+": 
                print(f"El resutado de la suma es:{calculadora1 + calculadora2} ") 
   
 

mi_calculadora()