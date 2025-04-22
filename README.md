# Índice Gini

Como parte de la cursada de Sistemas de Computación, se planea utilizar un stack completo de Python, C++ y Assembler para consultar datos en una API del banco mundial. Este proyecto proporciona herramientas para interactuar con la API, obteniendo el Índice de Gini, una medida de dispersión estadística utilizada comúnmente para representar la distribución del ingreso o la riqueza en una población.

## Características

- Cálculo del coeficiente de Gini a partir de conjuntos de datos.
- Estructurado con un `makefile` para facilitar la construcción y ejecución del proyecto.

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/FGalvagno/indice-gini.git
 cd indice-gini
```

2. Instalar las dependencias de Python
  
  
  ```bash
  pip install -r requirements.txt
  ```
3. (Opcional) Si se desean compilar las librerias de C++ y assembler usando make

```bash
sudo apt install build-essential nasm gcc-multilib g++-multilib
```

## Uso

Correr el programa ejecutando app.py
```
python app.py
```



