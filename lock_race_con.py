import threading

balance = 1000

def worker(): #without lock 
    global balance
    for i in range(100):
        temp = balance
        balance = temp- 10

threads = []

for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)
for i in threads:
    i.join()
print("balance without lock:",balance) 


balance2 = 1000

lock = threading.Lock()

def worker(): #without lock 
    global balance2
    for i in range(100):
        with lock:
            temp = balance2
            balance2 = temp- 10

threads = []

for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)
for i in threads:
    i.join()
print("balance with lock:",balance2) 
