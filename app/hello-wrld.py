import time
import datetime
import atexit
import signal
import sys

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
app = Flask(__name__)

if len(sys.argv[1]) >= 2:
    fileName = sys.argv[1]
else:
    fileName = "/tmp/test.txt"






def print_date_time():

    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))
    try:
        ts = str(int(time.time()))
        f = open(fileName, "a")
        f.write(ts + " Hello World!" + "\n")
        f.close();
    
    except IOError: 
        print ("Error: File  does not appear to exist.")

scheduler = BackgroundScheduler()
    
scheduler.add_job(func=print_date_time, trigger="interval", seconds=10)
    
scheduler.start()


@app.route("/")
def hello():
    return "Hello World!"
  
  

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5081)
    
atexit.register(lambda: scheduler.shutdown())