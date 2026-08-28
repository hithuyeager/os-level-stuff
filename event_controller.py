import threading
import time


def global_work(name,event:threading.Event):
    i = 0
    while True:
        event.wait()
        if (i % 5) == 0 and i != 0:
            time.sleep(0.5)
            print(f"{name} worker finshed {i} operations")
        i+=1


event1 = threading.Event()
event2 = threading.Event()
event3 = threading.Event()
events = [event1,event2,event3]

t1 = threading.Thread(target=global_work,args=("API WORKER",event1))
t2 = threading.Thread(target=global_work,args=("DATABASE WORKER",event2))
t3 = threading.Thread(target=global_work,args=("CACHING WORKER",event3))
threads = [t1,t2,t3]

for i in threads:
    i.start()
event1.set()

time.sleep(2)

event2.set()

time.sleep(2)

event3.set()

time.sleep(2)
event1.clear()
time.sleep(2)
event2.clear()
time.sleep(2)
event3.clear()
time.sleep(0.5)
print("stoped all the workers")



            

