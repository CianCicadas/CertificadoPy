import socket
import os
from nacl.signing import SigningKey

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((socket.gethostname(),1234))

while True:
    nArchivo = "Archivo.txt"
    tArchivo = os.path.getsize(nArchivo)

    with open(nArchivo, "rb") as archivo:
        contenido = archivo.read(1024)
        llaveFir = SigningKey.generate()
        firma = llaveFir.sign(contenido)
        llaveVer = llaveFir.verify_key
        llaveVerX = llaveVer.encode()
        cliente.send(llaveVerX)
        cliente.send(firma.signature)
        cliente.send(contenido)