# Repo para EIEC - DevOps - UNIR

Este repositorio nos servirá para demostrar el uso de Git en la asignatura de EIEC y muchas cosas mas.

---

Los comandos del Makefile funcionarán en Linux y MacOS. En caso de usar Windows, necesitarás adaptarlos o ejecutarlos en una máquina virtual Linux.

## Ejecución


python3 main.py <filename> <dup> <order>
  filename: **ruta** al fichero que contiene la lista de palabras, una por línea
  dup: **yes|no**, yes para eliminar palabras duplicadas, no para mantener la lista
  order: **asc|desc**, asc para ordenar ascendente, desc para descendente



## Ejemplo de uso


Para ejecutar la aplicación con un archivo de palabras y todos los parámetros, usa el siguiente comando:

  python3 main.py words.txt yes asc

Esto ordenará las palabras del archivo words.txt, eliminará duplicados y las mostrará en orden ascendente.

Para mantener duplicados y mostrar en orden descendente:

  python3 main.py words.txt no desc

Recuerda que los tres parámetros son obligatorios.


## Participación en la actividad grupal

**Desarrollador 2:** Gonzalo Torres del Fierro

Se realiza aporte al proyecto mediante uso de fork, rama propia, commits y pull request, siguiendo flujo colaborativo en GitHub.

## Participante Nro 3 Actividad Grupal 

Desarrollador 3: Jhon Gabriel Campos Zambrano

Actividades realizadas:

* Realizar fork desde el repositorio el administrador hacia mi cuenta personal
* Hacer copia (git clone)  del proyecto desde mi cuenta hacia mi maquina
* Generar una nueva rama (jcampos-python-mejora)
* Realizar la edición de uno de los archivos
* Agregar los cambios guardar los cambios en mi repositorio (Commit):
    * git add
    * git commit
    * git push
* Subir cambios al repositorio del administrador, con ayuda del pull request desde mi rama.  

## Participante Nro 5 - Jose Humberto Ochoa

* Se realiza el fork en 
* Se clona el repo en local.
* Se crea la rama nueva *git checkout -b joseochoa*
* Se implementa los cambios de la primera actividad, actualizar README.md.
* Se realiza commit de los cambios 
        - *git add -A*
        - *git commit -m "feat(JOSEOCHOA): Se actualiza readme"*
        - Se implementa funcionalidad de ordenamiento y se ajusta el readme.
        - Se crea archivo de ejemplo para probar funcionalidad de ordenamiento y eliminacion de duplicados archivo words.txt
        - Se adicionan los cambios al repo
        - *git add -A*
        - *git commit -m "feat(JOSEOCHOA): Se crea nuevo parametro al script main.py para ordenar asc/desc y se crea archivo words.txt para pruebas. Se ajusta el README.md para explicar el uso del nuevo parametro"*
        
