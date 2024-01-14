# Tutorial para Navegación Autónoma en Simulación
Navegación Autónoma para el robot Turtlebot 2 dentro del mapa de la EPSIII, Universidad de Alicante.

(ENLACE A LA DEMO DEL PROYECTO: https://drive.google.com/file/d/1eLg4ecjoHnvMDJPgnpjWYGwZV419vazV/view?usp=sharing)


Pasos para el corrector funcionamiento en simulación (solo funciona en Linux, es necesario tener descargado ROS):

# Paso 1
Si no tienes descargado ROS, Aquí tienes un tutorial de como descargarlo: https://wiki.ros.org/es/ROS/Installation

Descargar las dependencias correspondientes para su uso:
<pre>
  pip install smach
  pip install actionlib
</pre>

# Paso 2
Crear un directorio. Para ello, abrir una terminal y poner los siguientes comandos:

<pre>
  mkdir nombre_del_directorio
  cd nombre_del_directorio
  mkdir src
  catkin_make
</pre>

# Paso 3

Descargar la carpeta *Navigation_stage* dentro de la carperta `src` del directorio creado. Puedes hacerlo directamente copiando el repositorio actual mediante el comando:

<pre>
  git clone https://github.com/tc50ua/navegacionautonoma.git
</pre>

# Paso 4

Ejecutar:
<pre>
  catkin_make
  source devel/setup.bash
</pre>
En el directorio `nombre_del_directorio`

# Paso 5

Abrir *Rviz* y *Stage* mediante el comando
<pre>
  roslaunch navigation_stage mi_navigation.launch
</pre>

# Paso 6
Abrir una terminal nueva, en ella entrar a la carpeta `src` de *navigation_stage* y ejecutar el codigo **navegacionAutonoma.py**. Para ello:
<pre>
  cd nombre_del_directorio/src/navigation_stage/src
  python navegacionAutonoma.py
</pre>

# Paso 7
Escribir una de las posiciones [**ROBOTICA - ELECTRONICA - AUTOMATICA - ENTRADA - RECEPCION**] a las que puede ir el robot.
