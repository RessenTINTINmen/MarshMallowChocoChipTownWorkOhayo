from apscheduler.schedulers.blocking import BlockingScheduler
import tweet

twische = BlockingScheduler()

@twische.scheduled_job('interval',minutes=1)
def timed_job():
    tweet.puttweet_now()

if __name__ == "__main__":
    twische.start()