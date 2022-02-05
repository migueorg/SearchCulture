FROM python:3.9.10-slim

#Creo el grupo y usuario testeo
RUN groupadd testeo && useradd -ms /bin/bash -g testeo testeo

#Cambia al usuario testeo
USER testeo

#Establezco un directorio en el que haré las instalaciones y copiaré el task.yaml
WORKDIR /home/testeo

#Actualizo pip pues es el instalador de paquetes que voy a usar
RUN python -m pip install --upgrade pip

#Instalo el task runner
RUN pip3 install --user pypyr

#Copio el código con las tareas del task runner
COPY task.yaml ./

#Configuro path para que encuentre pypyr
ENV PATH=$PATH:/home/testeo/.local/bin

#Instalo dependencias del proyecto
RUN pypyr task installdeps

#Cambio a un directorio exclusivo para pasar los test
WORKDIR /app/test

ENTRYPOINT ["pypyr","task","test"]
