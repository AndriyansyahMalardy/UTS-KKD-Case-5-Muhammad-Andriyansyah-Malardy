import socket
import json

kalori_makanan = {
    'nasi goreng': 350,
    'ayam goreng': 250,
    'tempe': 150,
    'sayur': 100,
    'sate': 300,
    'bakso': 400,
    'mie goreng': 370,
    'telur': 200
}

def hitung_kalori(data):
    hasil = {}
    for anak, makanans in data.items():
        total = sum(kalori_makanan.get(m.lower(), 0) for m in makanans)
        hasil[anak] = total
    return hasil

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("App-2 (Server) siap menerima koneksi...")

conn, addr = server_socket.accept()
print("Terhubung dengan:", addr)

data = conn.recv(4096).decode()
input_data = json.loads(data)
hasil_kalori = hitung_kalori(input_data)

conn.send(json.dumps(hasil_kalori).encode())
conn.close()
