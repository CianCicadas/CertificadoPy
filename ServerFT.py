import socket
import PRNGnacl
from Crypto.Cipher import AES
from nacl.signing import VerifyKey

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(),1234))
formato = "utf-8"
tamanio = 1024

server.listen(5)

while True:
    cliente, direccion = server.accept()
    print(f'Conexion desde {direccion} establecida')

    bytes_clave = cliente.recv(32)
    firma = cliente.recv(64)
    verificar = VerifyKey(bytes_clave)

    with open("Archivo.txt","rb") as archivo:
        verificar.verify(archivo.read(),firma)

    with open("CC-"+archivo,"wb") as archivo:
        contenido = cliente.recv(1024)
        clave = PRNGnacl.prng(16)
        cifrador = AES.new(clave, AES.MODE_EAX)
        textoCifrado, etiqueta = cifrador.encrypth_and_digest(contenido)
        archivo.write(textoCifrado)
