from base64 import encode
import socket
import time


#host ve port isim ve ağlarının tanımlanması
host_name = "localhost"
port_name = 7777

#ip ve port numarasının yanyana yazılmasıyla olusturulan iletisim kanalı port'tur.
#socket olusuturulmasi / host ismi ve port'un socket'e baglanmasi
internet_socket = socket.socket()
internet_socket.connect((host_name,port_name))

#bir connection olustuguna dair atılan print:
print("{}:{} baglanti saglandi.".format(host_name,port_name))

#ilk olay client'tan baslayacagı ıcın bır mesaj yollanılması gerekıyor:
message = input("-->")
print("server bekleniyor...")


while message != "cikis":
    internet_socket.send(message,encode())
    coming_data = internet_socket.recv(1024).decode()

    print("SERVER: " + coming_data)

    message = input("-->")
    print("Server bekleniyor...") #input'tan sonra server kısmına gecis yaptıgımızı belirten mesaj.



internet_socket.close()

