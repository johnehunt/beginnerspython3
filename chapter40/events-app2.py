from threading import Thread, Event
from time import sleep


def wait_for_event(e):
    print('wait_for_event - entered and waiting')
    event_is_set = e.wait()
    print('wait_for_event - Event is set: ', event_is_set)


def set_event(e):
    print('set_event - entered but about to sleep')
    sleep(5)
    print('set_event - Waking up and setting event')
    e.set()
    print('set_event - Event set')


print('Starting')
e = Event()
t1 = Thread(target=wait_for_event, args=[e])
t1.start()
t2 = Thread(target=set_event, args=[e])
t2.start()
t1.join()
print('Done')