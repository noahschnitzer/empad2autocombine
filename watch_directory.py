from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

import sys
import time
import logging

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
