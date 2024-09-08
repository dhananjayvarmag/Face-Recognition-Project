from pushbullet import Pushbullet
from datetime import datetime

api_key = "o.WXXElm3TQbhtUsKMH6hEcJhQsxNAJ9sD"

pb = Pushbullet(api_key)

def sendMessage():
    temp = datetime.now()
    temp = temp.strftime('%d %b %Y  %X')
    msg = "New Unknown face is detected at " + temp
    push = pb.push_note('Alert', msg)

def sendStart():
    msg = "Security System Ready "
    push = pb.push_note('Alert', msg)


