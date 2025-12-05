# SCHEDULING
# CRON - this functioning linux and macOS not function in windows.
# AIRFLOW
# even while loop you can use
import time
# 1. scheduling:

# initially install the linux and ubuntu in windows.
# open the ubuntu terminal
# 1. show the projects comment - ( ls -lstr )
# 2. open the file or project  comment - ( vi (file or project))
# 3. if not show the file then create the file - ( vi filename.py ) enter
# 3.1 press (i) insert the code save and exit the page.( esc :wq ) enter
# 4. open the crontab page comment - ( crontab -e )
# 5. insert the file directory and schedule formula - */2 **** /home/jerry0104/filename
# 6 .formula - ( *2/ ***** ) for one time run after 2 minutes.
# 7. save and exit - (Ctrl+X) and  enter.
# 8. show the schedular time comment - ( cat filename )
# 9. enter the linux comment because how many times run the schedular - ( tail -f filename )
# 10.comment the line - #
# 11.again save and exit - (Ctrl+X) and  enter.

from datetime import datetime

print(datetime.now())

# Use while loop case for schedular:-

import time

def task():
    with open("time_log.txt","a") as file:
        file.write(f"Script ran at :{datetime.now()}\n")
        print(f"Task ran at :{datetime.now()}")

# run forever

while True:
    task()
    time.sleep(30)
    break

# 1.show the scheduler run foreground comment -  python3  filename.py
# 2.kill the schedular - Ctrl+C
# 3.show the scheduler run background comment -  nohup  python3  filename.py >> data.log &
# 3.1 double enter the comment
# 3.2 type the comment ( ls -lstr )
# 3.3 show the all scheduler for background run -  tail -f filename.txt
# 3.4 Kill the file - Ctrl+C
# 4. after kill the file show the background run the file comment - ( ps -aux )
# 5. kill the background run the file comment - ( kill -9 (file pid number) )
# 6. after type the comment ( ps -aux ) - it will not run the comment.
