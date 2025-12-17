import snap7
from snap7.util import *
from snap7.snap7types import *

PLC_IP = "192.168.1.1"  # Cambia con l'IP del tuo PLC
RACK = 0
SLOT = 1

client = snap7.client.Client()
client.connect(PLC_IP, RACK, SLOT)

if client.get_connected():
    print("Connesso al PLC!")
    # Esempio: leggere DB1, 4 byte dall'offset 0
    data = client.db_read(1, 0, 4)
    value = get_int(data, 0)
    print("Valore letto:", value)
else:
    print("Connessione fallita")
