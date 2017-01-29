#Embedded Linux
#Modulo: Redes

##Proyecto AceleroTweet.

##Nombre: Mauricio Quijada Jiménez


###Descripción del proyecto: 

El presente proyecto planea cubrir los temas vistos en el módulo de redes,
así que se pone especial énfasis en los protocolos de comunicación en red como UDP, 
adquisición de datos mediante i2c y publicar los datos adquiridos en una red social.

Se usa una tarjeta raspberrypi 3 con raspbian jessie, con la version del kernel 4.4.
La tarjeta adquiere datos del sensor mpu6050, el cual puede medir acceleración, orientación y temperatura.
Se programa en lenguaje de programación python un servidor y un cliente.
El cliente adquiere los datos del sensor y los envía al servidor mediante el protocolo UDP por medio de sockets
El servidor al recibir los datos del sensor los envía a la siguiente cuenta de twitter:

https://twitter.com/Mau_Krack

###Justificación del protocolo UDP

¿Porqué usé UDP?
El protocolo UDP  es un protocolo no orientado a conexión de la capa de transporte, a diferencia de TCP/IP que requiere la confirmación de la recepción de los datos por parte del servidor, así como tampoco control de flujo.

Recordemos las capas vistas en clase:

*Capa 8  Usuario*
Capa 7  Nivel de Aplicación <br />
Capa 6  Nivel de Presentación<br />
Capa 5  Nivel de sesion<br />
Capa 4  Nivel de transporte<br />
Capa 3  Nivel de Red<br />
Capa 2  Enlace de datos<br />
Capa 1  Fisica<br />
*Capa 0 Todo prendido y conectado*<br />

###Protocolo I2c

Para hacer uso del protocolo i2c, es necesario contar con un driver para la lectura de los datos, este corresponde al módulo de Kernel y se incluye en la carpeta. La tarjeta funcionará como maestro y el sensor como esclavo.
El protocolo consta de 2 lineas sda y scl, una es el reloj y la otra es la linea de datos. por lo que es necesario conectarlas a los pines correspondientes de nuestra tarjeta de la siguiente manera:
[liga]
![alt tag](https://github.com/MauricioQJ25/proyectoredes/blob/master/conexi%C3%B3n.png)
[liga]
Tarjeta y sensor
![alt tag](https://github.com/MauricioQJ25/proyectoredes/blob/master/sensorconectado.jpeg)

Para leer un dato de nuestro sensor, es necesario conocer la dirección del registro que viene de fábrica. Cada dispositivo tiene su dirección, en nuestro caso el sensor tiene la dirección 0x68, y para leer un registro o escribir en el, es necesario llamar a su dirección, el registro, y los datos que se van a leer o escribir, esto viene en el driver, por lo que en el código solo se llama a las librerias de mpu6050.

##Funcionamiento del cliente y el servidor

Para mostrar el funcionamiento del cliente y el servidor, se ejecutan en 2 terminales diferentes de la siguiente manera:
python cliente.py, python servidor.py

Se puede observar el comportamiento en la siguiente imagen.

[liga]
![alt tag](https://github.com/MauricioQJ25/proyectoredes/blob/master/cliente-servidor.png)

Por último para mostrar los datos sensados, se muestra las publicaciones en twitter generadas por el servidor.

[liga]
![alt tag](https://github.com/MauricioQJ25/proyectoredes/blob/master/tweet.png)

Referencias.
En la carpeta ejemplos, muestro los códigos en los que me basé para la integración del proyecto, así como las siguientes ligas que me resultaron muy útiles.
http://pinout.xyz/
http://www.invensense.com/wp-content/uploads/2015/02/MPU-6000-Register-Map1.pdf
https://geekytheory.com/tutorial-raspberry-pi-uso-de-twitter-en-python/
http://developeando.net/sockets-python/
https://www.raspberrypi.org/documentation/linux/kernel/building.md
http://www.linuxjournal.com/article/7136
