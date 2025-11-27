import socket as sk
import json

mensajes=[]
sock=sk.socket(sk.AF_INET,sk.SOCK_DGRAM)
sock.bind(("127.0.0.1",5000))
while True:
    datos,direccion=sock.recvfrom(1024)
    mensaje=datos.decode()

    mensaje.append([mensaje,direccion[0]])

    respuesta={
        "total_,ensaje":len(mensajes),
        "ultimo_mensaje":mensaje
    }
    sock.sendto(json.dumps(respuesta).encode(),direccion)