import time
def timeDate(times):
	time_local = time.localtime(times)
	 # %H:%M:%S
	return time.strftime("%Y-%m-%d",time_local)