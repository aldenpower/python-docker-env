from time import sleep
from sys import stderr

i = 0
while True:
    print(f"[stdout] Tick {i}", flush=True)
    print(f"[stderr] Tick {i}", file=stderr, flush=True)
    i += 1
    sleep(1)
