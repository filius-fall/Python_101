# import subprocess

# args = ["ping", "www.yahoo.com"]
# process = subprocess.Popen(args, stdout=subprocess.PIPE)
# data=process.communicate()

# for i in data:
#     print(i)


import subprocess
from threading import Timer
kill = lambda process: process.kill()
cmd = ['ping', 'www.google.com']
ping = subprocess.Popen(
    cmd, stdout=subprocess.PIPE)
my_timer = Timer(5, kill, [ping])
try:
    my_timer.start()
    stdout = ping.communicate()
    for i in stdout:
        print(i)
finally:
    my_timer.cancel()