# EyeCatcher
> This is a subproject for the CoWF, its completly required to run this project.

![swappy-20240409_194925](https://github.com/QcTL/CoWF-EyeCatcher/assets/71326643/e8b4cbd9-df04-4480-b6ae-b3a418c7bc6a)

This projects aims to create a Web interface to see the obsererd variables over the CoWF project. Once added in the web program, the
user can observe the graf and its progretions since it was added. The user can also dowload a .CSV file showing the values
and the timestaps of any of the recoreded variables.

## Prerequisites:
Before running the main.py file, ensure that in the local enviroment the following libraries are installed:

- Python 3.x
- Flask
- Flask-SocketIO
- Matplotlib

pip install flask flask-socketio matplotlib

## Project structure:

```
CoWF-EyeCatcher/
│
├── main.py              # Main Flask application
├── templates/          # HTML templates for rendering views
│   └── index.html
│   └── p_graphEye.html
│   └── p_lEyes.html
└── src/             # Source files
    └── runner/
            └── Eye/ # Code for the eyes
                └── Eye.py
                └── EyeContainer.py   
        └── EyeCatcher.py   # Receiver of the socket from CoWF
    └── web/
        └── AppWebEye.py  # Code for Web Application
```
## Communication package:

Its based on sending the package of 3 values:
- Int: Value of the Atribute
- Int: Timestamps of the new value
- char\[32\]: The String that contains the name of the variable, filled with " " until end.

The chars is usually composed with **NAME_OBJECT_RECORDED-ATTR_RECORDED**. With the "**-**" separating it in the String.

## Dependencies:
Flask: Used for creating the web application and handling HTTP requests.
Flask-SocketIO: Enables bidirectional communication between the Flask server and clients using WebSockets.
Matplotlib: Library for creating static, animated, and interactive visualizations in Python.

