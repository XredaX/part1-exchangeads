import schedule
import requests


def send_msg():
   url="https://api.telegram.org/bot5102702091:AAFI9FISwdHRjdQYLPxkcD2DGpWnQHYqwbg/sendMessage?chat_id=-1001654861712&parse_mode=Markdown&text="
   request = url+"Start"
   requests.get(request)

def job1():
    send_msg()

print("Start remember")
schedule.every().day.at("11:00").do(job1)
schedule.every().day.at("20:00").do(job1)
while True:
   schedule.run_pending()
