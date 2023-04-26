import time
from datetime import datetime

while True:
    time.sleep(5)
    now = datetime.now().strftime('%H:%M:%S')
    print(now)
