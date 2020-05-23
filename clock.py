"""from apscheduler.schedulers.blocking import BlockingScheduler
from optimized import *

sched = BlockingScheduler()



@sched.scheduled_job('interval', minutes=30)
def index():
	#sc.run_pending()
	main()



sched.start()
"""

#clock: python clock.py