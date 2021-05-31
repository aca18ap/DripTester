import gui
from dripReq import createReq
from multiprocessing import Process, Queue 


def startGui(q):
    try:
        g = gui.Gui(q)
    except:
        print("Something went wrong starting the GUI")


def startReqListener(q):
    while True:
        if q.empty():
            job = q.get()
            print(job, " job found")
            createReq(job)



def main():
    q = Queue()
    print("Queue created")
    print("GUI PROCESS starting")
    tp = Process(target=startGui, args=(q,))
    tp.start()
    ##tp.join()

    print("RREQUEST HANDLING PROCESS starting")
    qp = Process(target=startReqListener, args=(q,))
    qp.start()
    ##qp.join()

if __name__ == '__main__':
    main()