# Bot de Telegram de Ofertas de Amazon

<img src="https://brandemia.org/contenido/subidas/2022/11/logo-amazon-2000-actualidad-1024x576.png" alt="logo" width=300>

Este proyecto es un bot de Telegranm conectado a un canal que muestra ofertas de Amazon en el mismo.

## Requisitos

### Instalación del script

En primer lugar, ejecutaremos ```script.sh``` desde el terminal para instalar todas las dependencias. Abrimos una terminal en el directorio que estamos trabajando y ejecutamos el siguiente comando ```bash script.sh```

### Manual de instalación

### **Si usaste el ```script.sh```, puedes saltar el siguiente paso.**

Debes completar los siguientes pasos: 

- Crea un bot de telegram (https://core.telegram.org/bots)
- Crea un amazon de afiliados (https://afiliados.amazon.es/welcome)
- Pon todas las keys (Amazon y Telegram API Keys) en el código, definiremos como hacerlo después.

- **Instalando paquetes**:
En el root del proyecto ejecutable:
```bash
pip3 install -r requirements.txt
cd paapi5-python-sdk
python3 setup.py build
python3 setup.py install
cd ..
```

## Estructura del proyecto

El proyecto está estructurado de la siguiente manera:

- **bot.py**
  - Contiene el código de inicio del bot

- **consts.py**
  - **AQUÍ DEBES PONER TUS CLAVES Y PARÁMETROS API DE TELEGRAM Y TUS CLAVES Y PARÁMETROS API DE AMAZON**
  - **EL NOMBRE DEL CANAL DEBE COMENZAR POR @ (por ejemplo @nombreDelCanal)**
  

- **amazon_api.py**
  - Contiene la función api de amazon para buscar productos


- **response_parser.py**
  - Funciones utiles que analizan la respuesta api de amazon


- **create_messages**
  - funciones de creación de mensajes

## ¿Cómo funciona?
El bot se ejecuta en un bucle while, puede definir sus parámetros favoritos para:
- Horas de actividad
- Tiempo de pausa entre mensajes
- Categorías de búsqueda en Amazon
- Buscar palabras clave



El bot está activo si el tiempo está entre **MIN_HOUR** y **MAX_HOUR** (_puedes desactivar eso durante la noche por ejempolo_), podrás definir estos parámetros en el código.

El hacer una pausa para definido **PAUSE_MINUTE** después de enviado un mensaje.

También podrás editar el cuerpo del mensaje en ```create_messages.py```.

El bot hace todas las peticiones http a la API de Amazon al inicio, guarda una lista de todos los resultados en la RAM y mientras haya elementos en la lista de resultados:
1. ENVIAR MENSAJE DE OFERTA
2. PAUSA DURANTE PAUSE_MINUTES
3. ENVIAR OTRO MENSAJE

Durante todo el tiempo de actividad. Cuando se han enviado todos los resultados, reinicia su bucle.

### **NOW YOU CAN SEARCH OVER MULTIPLE CATEGORIES** : _in `bot.py` you need to specify your categories and a list of keywords for each category. The corresponding variable is `categories`, it accept a dictionary like:_ 
```python
{
  "1_CATEGORY_NAME":[LIST OF KEYWORD],
  "2_CATEGORY_NAME":[LIST OF KEYWORD]
}
```
  
## Usage

After cloning the repository, define all parameters in the code, install all packages and then start bot with command:
```python bot.py``` or ```python3 bot.py```
  
## Support 
If you need support for the installation and usage of the library you can write to:
- tgofferbot@gmail.com
  
In order to mantain and improve the library consider to contribute:
  
[![paypal](https://user-images.githubusercontent.com/33979978/187162516-5a6576a0-b44d-4e01-bcc6-fd0c262e683a.png)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=7HWMJSGMCCTB6)

## Message Structure

![image](https://user-images.githubusercontent.com/33979978/109800731-dbe44c80-7c1d-11eb-8316-fd5275cb5b46.png)

This is a generated telegram channel message example, you can edit the message structure on  ```create_messages.py``` code.

## Author

Pablo Nicolás
