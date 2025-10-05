#Error de orden de Ejecución:El bloque correcto estara al final del archivo
#Estas son constantes de configutación que se pueden usar en metodos numericos u optimización
MAX_ITERS = 100
TOL = 1e - 8
M = 1e6
#Programa para solucionar problemas de optimización con el metodo simplex


# Importamos las librerias necesarias
import numpy as np
from scipy.optimize import linprog

# Funcion para solicitar los datos al usuario
def leerdatos():
    print("=== Metodo Simplex ===")
    tipo= input("¿Desea Maximizar o Minimizar? solo coloca: (Max/Min):").strip().lower()
    while tipo not in["Max", "Min"]:
       print("Entrada no valida intente de nuevo")
       tipo= input("¿Desea Maximizar o Minimizar? solo coloca: (Max/Min):").strip().lower()

    #Solicitamos el Numero de Variables
    n = int(input("Ingresa el numero de variables:"))

    #Solicitamos los coeficientes de la función objetivo.
    print("Ingresa los coeficientes de la funcion objetivo:")
    c = [] #Coeficientes que agreguemos
    for i in range(n_vars):
     coef = float(input(f"coeficiente de x{i+1}:"))
     c.append(coef)


    # Leemos los coeficientes de la función colectivo
    print("\nIntroduce los coeficientes de la función objetivo:")
    c = []
    for i in range(n_vars):
      coef = float(input(f"coeficiente de x{i+1}: "))  
      c.append(coef)

      #Si es maximización cambiamos el signo de los coeficientes
      #Porque Lingpro resuelve solo problemas de Minimización
      if tipo == "Maximización":
         c = [-x for x in c]
         # Leemos el numero de restricciones
         n_restricciones = int(input("\n¿Cuantas Restricciones hay?"))

         A= [] #Matriz de coeficientes
         B= [] #Lado derecho
         signos = [] #Signos de las restricciones
         print("\nIntroduce las restricciones una por una:")
         print("Ejemplo: Para 2X1 + 3X2 <= 10, Escribe los coeficientes y el signo")
         for i in range(n_restricciones):
            print(f"\nRestriccion {i+1}: ")
            fila = []
            for j in range(n_vars):
               coef=float(input(f"coeficiente de x{j+1}:"))
               fila.append(coef)
            signo = input("Signo de la restricción (<=,>=,=):").Strip()
            valor = float(input("Valor del lado derecho: "))
            #Para igualdad agregamos dos restricciones
            if signo== "<=":
               A.append(fila)
               B.append(valor)
            elif signo== ">=" :
            #Multiplicamos por -1 para convertir a <=
               A.append([-x for x in fila])   
               B.append(-Valor)
            elif signo== "="   :
            #Para igualdad agregamos tanto <= como >=
               A.append(fila)   
               B.append(valor)
               A.append([-x for x in fila])
               B.append(-valor)
            else:
               print("Signo no valido Usa <=,>= o =")   
               return None, None, None, None
            
            return c, A, b, tipo
      
      # Funcion Principal
      def main():
         #Leemos los datos del problema
         c, A, b, tipo=leer_datos()
         if c is None:
            return
         #Resolvemos con linprog (por defecto metodo simplex revisado)
         res = linprog(c, A_ub=A, b_ub=b, method="highs")

         print("\n=== RESULTADOS ===")
         if ref.success:
            print("Solucion optima encontrada")
            for i, val in enumerate(res.x):
               print(f"x{i+1}= {val:.4f}")

            #Recordar: si era de maximización, revertimos el signo
            valor_optimo=res.fun if tipo== "Minimización"  else-res.fun
            print(f"\nValor optimo de la funcion objetivo: {valor_optimo:.4f}")
    else:
       print("No se encontro una solucion optima. Revisa los datos.")
#Ejecutamos el programa principal
if name== "_main_":
   main()     
           
      

         
  

