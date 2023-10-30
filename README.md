# Practica04_http_cliente_redes

Ejecucion del programa:

Con Python 3:

python3 clientHTTP_base.py GET / 1 gzip close

o 
python clientHTTP_base.py GET / 1 gzip close


Con Docker:
Ejecute los siguientes comandos:

sudo docker build -t redes:p4

sudo docker image ls

sudo docker run --interactive --tty redes:p4 /bin/sh

python3 /opt/clientHTTP_base.py www.fciencias.unam.mx GET / 1 gzip close

o 

python /opt/clientHTTP_base.py www.fciencias.unam.mx GET / 1 gzip close

Preguntas:
1. ¿Cuál es la función de los métodos de HTTP HEAD, GET, POST, PUT y DELETE?

    HTTP HEAD: Obtiene las cabeceras de los recursos.
   
    GET:  Su funcion es obtener información del servidor, recursos en especifico.
   
    POST: Manda informacion al servidor para ser agredado.
   
    PUT: Usualmente usado para editar algun recurso del servidor
   
    DELETE: Eliminar un recurso del servidor.


2. ¿Investigue y enliste junto con su significado las categorías de códigos de estado que usa HTTP?

   1XX Informativo

   2XX Exito

   3XX Redireccion

   4XX Error del Cliente

   5XX Error del servidor

3. ¿Para qué se usan los campos encoding y connection?
   
    Encoding: Es la forma como se quiere codificar y comprimir la informacion para que la informacino sea mandada.

    Connection: Para indicar si queremos cerrar la conexion despues de cada peticion y abrir de nuevo por cada uno, o si queremos mantener la conexion abierta por mas tiempo aun despues de terminar cada       peticion.

Referencias:

  9cv9. (2019). What are GET, POST, PUT, PATCH, DELETE? A walkthrough with JavaScript’s Fetch API. Medium. Disponible de: https://medium.com/@9cv9official/what-are-get-post-put-patch-delete-a-walkthrough-with-javascripts-fetch-api-17be31755d28
  
 Mendoza Castro, R. (2023). Codigos HTTP: Lista Completa + Explicaciones. Semrush Blog. Disponible en: https://es.semrush.com/blog/codigos-de-estado-http/
