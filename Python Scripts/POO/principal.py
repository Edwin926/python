from magnitudes import Temperatura , Masa , Longitud

opcion = input("Seleccione una opcion \n 1.Temperatura \n 2.Longitud \n 3.Masa \n")

valor = input("Ingrese el valor a convertir \n")
while True:
    if(opcion == "1"):
       """ op= input("seleccione una opciion \n 1.kelvin-celsuis \n 2.fahrenheit-celsuis \n 3.kelvin-fahrenheit \n")
        if (op=="1"):""" 
       obj = Temperatura(float(valor));
       print("Kelvin a Celsius " , obj.kelvinCelsius())
       break
   
    if(opcion=="2"):
        obj = Longitud(float(valor));
        print("Centimetro a Pulgada " , obj.centimetrosPulgada())
    
    if(opcion=="3"):
        obj = Masa(float(valor));
        print("Libra a Tonelada " , obj.libraTonelada())


