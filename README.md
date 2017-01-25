#Proyecto de redes

##Nombre: Mauricio Quijada Jiménez

El proyecto consiste tomar las lecturas de un acelerómetro
mpu6050 y la temperatura dada, mediante el protocolo i2c
y el uso de un driver para la tarjeta raspberry pi 3.

Las lecturas se envian  mediante sockets a un servidor desde un cliente.

El servidor recibe las lecturas del sensor y las envía a Twitter.

El lenguaje de programación que se uso fué python por sus extraordinarias
capacidades de scripting.

Para envíar la información se uso UDP ya que no se requiere de una confirmación
de recepción de los datos.

Para ejecutar realize lo siguiente.

1.-$cd /proyectoredes
2.-$python servidor.py
3.-$python cliente.py

y podemos observar los datos enviados en la siguiente cuenta de twitter.

https://twitter.com/Mau_Krack

A continuacion las imagenes de los resultados.



