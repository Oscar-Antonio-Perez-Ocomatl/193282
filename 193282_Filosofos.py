import time
import random
import queue
import threading

turno = queue.Queue(maxsize = 5)
filosofos = ['Filosofo1', 'Filosofo2', 'Filosofo3', 'Filosofo4', ' Filosofo5']
cont = 0

def Cenar():
    global cont
    while cont < 5:
        if not turno.full():
            filosofo = random.choice(filosofos)
            filosofos.remove(filosofo)
            turno.put(filosofo)
            print(f'el {filosofo} esta cenando')
            cont+=1
            time.sleep(random.randint(1,3))

def Terminar():
    global cont
    while cont <= 5:
        if not turno.empty():
            termino = turno.get()
            turno.task_done()
            print(f'el {termino}, ha terminado de cenar\n')
            time.sleep(random.randint(1,3))

if __name__=="__main__":
    thread_productor =  threading.Thread(target=Cenar)
    thread_consumidor = threading.Thread(target=Terminar)
    thread_productor.daemon = True
    thread_consumidor.daemon = True
    thread_productor.start()
    thread_consumidor.start()
    aux = 5

    while True:
        if cont == aux:
            time.sleep(2)
            exit()
