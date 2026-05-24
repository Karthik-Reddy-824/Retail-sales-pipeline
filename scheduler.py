from apscheduler.schedulers.blocking import BlockingScheduler
import threading

def run():
    pass

scheduler = BlockingScheduler()
scheduler.add_job(run, 'interval', hours=9) # Run every 9 hours

# Run scheduler in a separate thread
t = threading.Thread(target=scheduler.start)
t.daemon = True  # This is the key - daemon thread dies when main program exits
t.start()

try:
    print("⏳ Scheduler started...")
    while True:
        pass  # Keep main thread alive
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
    print("🔴 Scheduler stopped.")