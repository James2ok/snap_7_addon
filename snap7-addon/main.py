import snap7
from snap7.util import get_int
from snap7.snap7types import *

PLC_IP = "192.168.1.100"  # Cambia con l'IP del tuo PLC
RACK = 0
SLOT = 1

client = snap7.client.Client()
client.connect(PLC_IP, RACK, SLOT)

if client.get_connected():
    print("Connesso al PLC!")
    data = client.db_read(1, 0, 4)
    value = get_int(data, 0)
    print("Valore letto:", value)
else:
    print("Connessione fallita")
