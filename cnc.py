import serial
import time
from flask import Flask

app = Flask(__name__)
# Open grbl serial port
s = serial.Serial('/dev/cu.usbserial-A104OEIO',115200)

# Wake up grbl
s.write("\r\n\r\n".encode()) # lo paso a bits con encode
time.sleep(2)   # Wait for grbl to initialize 
s.flushInput()  # Flush startup text in serial input


@app.route("/")
def bienvenido():
    return "bienvenido al CNC!"

@app.route("/movete")
def move():
    s.write('G21G91G1X-20F3000\n'.encode()) # Send g-code block to grbl
    return "<p>me movi 20 mm a la izquierda</p>"
