import ntplib 
import time
from datetime import datetime, timezone
c = ntplib.NTPClient()
#file = open("C:\\Users\\Amir Sabzi\\Desktop\\covert_channel\\covert_channel\\testlog.txt", "w")
#file = open("/home/amirs97/covert_channel/testlog.txt", "w")
for i in range(1):
    start = time.time()
    print(datetime.fromtimestamp(c.request('0.au.pool.ntp.org', version=3).tx_time).strftime("%S:%f")[:-3])
    finish = time.time()
    print(finish-start)
#file.close()


