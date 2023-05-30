from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler,FileSystemEventHandler

import sys
import time
import logging

'''
if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    path = Path(path)
    print(f"{path=}")
    print(f"{path.exists()=}")
    print(f"{path.is_dir()=}")


    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
'''


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        #print(f'event type: {event.event_type}  path : {event.src_path}')
        if(event.src_path[-4:] == '.xml'):
        	with open(event.src_path,'r') as f: # The with keyword automatically closes the file when you are done
        		print('XXXXSTARTXMLXXX')
        		print(f.read())
        		print('XXXENDXMLXXX')



if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    path = Path(path)
    print(f"{path=}")
    print(f"{path.exists()=}")
    print(f"{path.is_dir()=}")

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
