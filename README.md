# **GUIDE FOR TESTANGAN.PY**
This is a python-based computer vision that uses the cv2 and mediapipe libraries.and I have also configured this testangan.py into the arduino project, so you can try to turn on the led light using your hand movements.


I will show you how to install and run this code, not only that I will also provide a debugging file to check for errors/mistakes in installing the library
### follow step by step:
1. You must install python 3.11 or below, why? Because that version supports cv2. link: [python v3.10](https://www.python.org/downloads/release/python-3100/)
2. After that you must have pip, usually pip is integrated with python, but if you don't have it, please reinstall your python because there is something wrong with the package.
3. Once you have all of that, the next step is to install CV2 and Medipipe. Follow these commands:
   - python -m pip install CV2
   - python -m pip install Mediapipe
4. and yup, you did it. now you can test you computer vision (hand tracker).

## OPTIONAL STEP(COMBO WITH ARDUINO) handino.py
Well, this is where the fun part is, follow these steps:
1. you must install new library for connect your code(py) to serial(arduino), it is Serial
2. Follow this command and paste it into your cmd:
   - _python -m pip install pyserial_ and
   - _python -m pip install time_
Listen to me, this is not Serial, not serial, nor any other serial, be careful of making mistakes.
3. Build your project which is an Arduino and 1 LED, then see what serial you have and attach it to the serial configuration in the handino.py file which says _('COM3', 9600)_
4. If successful, you can run the hand tracker with the Arduino combo.if dont success, let try this tutorial:

## DEBUGGING
The first time I made this, I was surprised by many strange phenomena that appeared in the terminal, starting from error codes and libraries that couldn't be used even though I had installed them.

i will continue this readme soon

