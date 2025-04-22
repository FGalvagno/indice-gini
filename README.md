# Índice Gini

Como parte de la cursada de Sistemas de Computación, se planea utilizar un stack completo de Python, C y Assembler para consultar datos en una API del banco mundial. Este proyecto proporciona herramientas para interactuar con la API, obteniendo el Índice de Gini, una medida de dispersión estadística utilizada comúnmente para representar la distribución del ingreso o la riqueza en una población.

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
3. (Opcional) Si se desean compilar las librerias de C y assembler usando make

```bash
sudo apt install build-essential nasm gcc-multilib g++-multilib
```
4. [Entornos basados en Red-Hat] existe una version alternativa de la libreria de compresion zlib que incorporan los sistemas de proxima generacion, para solucionar problemas de compilacion se instala
```bash
sudo dnf install zlib-ng-compat.i686
```   
## Uso

Correr el programa ejecutando app.py
```
python app.py
```



