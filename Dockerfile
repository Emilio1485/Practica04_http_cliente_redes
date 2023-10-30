#Dockerfile

#Imagen base para construir la imagen a trabajar
#Se usa Python 3.11.2 
FROM python:3.11.2


ADD clientHTTP_base.py /opt/
