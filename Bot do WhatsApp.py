import pywhatkit
from time import sleep

def send_msg (number: str, message: str, hour: int, min: int):
    pywhatkit.sendwhatmsg(number, message, hour, min)

send_msg('+5581973431677', 'ME DESBLOQUEIA, IGUAIRAAAAA', 10, 21)
send_msg('+5581995254823', 'BORA TOMAR MINOXIDIL?', 10, 23)
send_msg('+5581993289246', 'BORA VER METAL & CEGO?', 10, 25)
send_msg('+5581997451067', 'PIQUINIQUE COM OS SAGUINS', 10, 27)
