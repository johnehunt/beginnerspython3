from multiprocessing import Process, Event
from time import sleep


def wait_for_event(event):
    print('wait_for_event - Entered and waiting')
    event_is_set = event.wait()
    print('wait_for_event - Event is set: ', event_is_set)


def set_event(event):
    print('set_event - Entered but about to sleep')
    sleep(5)
    print('set_event - Waking up and setting event')
    event.set()
    print('set_event - Event set')


print('Starting')

# Create the event object
e = Event()

# Start a Process to wait for the event notification
t1 = Process(target=wait_for_event, args=[e])
t1.start()

# Set up a process to set the event
t2 = Process(target=set_event, args=[e])
t2.start()

# Wait for the first process to complete
t1.join()

print('Done')
