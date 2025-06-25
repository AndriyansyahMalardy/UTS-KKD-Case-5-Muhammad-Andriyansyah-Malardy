import socket
import json

data_anak = {}
jumlah = int(input("Masukkan jumlah anak (max 6): "))

for _ in range(min(jumlah, 6)):
    nama = input("Nama anak: ")
    makanans = input("Makanan favorit (pisahkan dengan koma): ").split(",")
    data_anak[nama] = [m.strip() for m in makanans]

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

client_socket.send(json.dumps(data_anak).encode())
hasil = client_socket.recv(4096).decode()
client_socket.close()

hasil_kalori = json.loads(hasil)
print("\n--- Total Kalori Setiap Anak ---")
for anak, kal in hasil_kalori.items():
    print(f"{anak}: {kal} kkal")
