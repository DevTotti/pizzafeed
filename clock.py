from apscheduler.schedulers.blocking import BlockingScheduler
from data import *

sched = BlockingScheduler()



@sched.scheduled_job('interval', minutes=30)
def index():
	#sc.run_pending()
	main()
	time.sleep(90)
	major()
	time.sleep(300)


sched.start()
