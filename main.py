import os
import time
import datetime as dt


LOGFILE_PATH = os.environ.get('SIMPLE_LOGFILE_PATH', '/var/log/simple.log')


def main():
    with open(LOGFILE_PATH, 'w') as fd:
        while True:
            print(dt.datetime.now().isoformat(), file=fd, flush=True)
            time.sleep(10)

if __name__ == "__main__":
    main()
