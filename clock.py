from apscheduler.schedulers.blocking import BlockingScheduler
import tweet

twische = BlockingScheduler()

@twische.scheduled_job('interval',minutes=15)
def timed_job():
    tweet.puttweet_now()

if __name__ == "__main__":
    twische.start()
