from email import message
from shutil import which
import socket
import time

#host ve port isim ve ağlarının tanımlanması
host_name = "localhost"
port_name = 7777

#ip ve port numarasının yanyana yazılmasıyla olusturulan iletisim kanalı port'tur.
#socket olusuturulmasi / host ismi ve port'un socket'e baglanmasi
internet_socket = socket.socket()
internet_socket.bind((host_name,port_name))
#socket'in dinlenmesi icin:
internet_socket.listen(1)

#socket.accept metodu ile connection ve adres alınır. bunlarla işlem yapılır.
connection, address = internet_socket.accept()

#bir connection olustuguna dair atılan print:
print(str(address) + " baglanti saglandi.")

#while dongusu: devamlı donecek. client kısmından gelen dataları kontrol edecek.
#coming_data kısmında konsolda yazdırılacagı ıcın str turune cevrım yapılıyor.
#connection'un recv metodu var. bu metod donus degerını temsıl eden nesnedir.
#icerisine belli bir bytesize alır. sonrasında decode edilir.
#encode olarak gonderılır. decode edılerek alınır.

while True:
    while True:
        try:
            coming_data = str(connection.recv(1024).decode())
            print("client sunu yolladi: " + coming_data)
            break
        except ConnectionResetError: #hata alınırsa tekrardan baglantı kurulup saglanılacak.
            time.sleep(2)
            connection, address = internet_socket.accept()      
            print(str(address) + " baglanti saglandi.")
    if coming_data == "cikis": #cikis yazılırsa program quit ediliyor.
        break
    else: #karsi tarafa(client tarafına) mesaj yollanmak istenir.
        message = input("-->")
        print("Client bekleniyor...") #input'tan sonra client kısmına gecis yaptıgımızı belirten mesaj.
        connection.send(message.encode()) #client'a mesaj encode'lanıp(sıfrelenıp) atılır.

#1.dongu client'a yollanacak veri(mesaj) ıcın donuyor. 
#2.dongu client'dan gelen bir veri(mesaj) var mı yok mu sorgusu ıcın donuyor.
#donguler de bıttıkten sonra baglantı kapatılır.
connection.close()

