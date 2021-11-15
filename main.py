from pyrogram import Client
import schedule
import time
import pytz


def biotxt():
    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M", curr_time)
    return curr_clock


app = Client("my_account",
             api_id= ********,
             api_hash='********************'
             )
app.start()

print("connected to telegA SOCSESFULLY    :)")
def sendmsg():
    #app.send_message("me", "تابع در حال اجراست")
    time=biotxt()  
    #time="12:21"
    text="بازدید شما در ساعت {} ثبت شد✅ (خیخییخی)" .format(time)
    app.update_profile( bio=text)



try:
    schedule.every(30).seconds.do(sendmsg)
except:
    print('unfortunately there was an error :(')

# Loop so that the scheduling task
# keeps on running all time.
while True:
  
    # Checks whether a scheduled task 
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)

# Update bio



