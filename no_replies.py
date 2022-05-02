import xlrd
import re
from datetime import datetime, timedelta
from twilio.rest import Client
import xlsxwriter
import pytz

# To Do: mask keys
account_sid = ''
auth_token = ''

file_location = "/Users/rishikasharma/desktop/RishikaCode/demo/copa_info.xlsx"

twilio_phone_number = ''
to_date_time = datetime.now()
from_date_time = to_date_time - timedelta(days = 7);

tz_ph= pytz.timezone('America/Phoenix')

from_date_time_timezone = tz_ph.localize(from_date_time)
to_date_time_timezone = tz_ph.localize(to_date_time)

print("from_date_time: " + from_date_time.strftime("%c") + " to_date_time " + to_date_time.strftime("%c"))

# 1. create dictionary from xls file
workbook= xlrd.open_workbook(file_location)
sheet= workbook.sheet_by_index(0)

copaH={}
for i in range(1,sheet.nrows):
     #print(sheet.cell_value(i,0))
     #print(sheet.cell_value(i,1))
     key = sheet.cell_value(i,1)
     value = sheet.cell_value(i,2)
     #print("key is: ",key)
     #print("value is: ",value)
     copaH[key]=value
     #print("Dictionary is: ",copaH)

print("Final Dictionary is: ",copaH)

# 2. read messages from twilio
client = Client(account_sid, auth_token)
all_messages = client.messages.list(
     limit=20)
#print("all messages list is ", all_messages)


# 3. write data to xlsx file

#create file workbook and worksheet

outWorkbook = xlsxwriter.Workbook("no_replies_list " + to_date_time.strftime("%c")+".xlsx")
outSheet = outWorkbook.add_worksheet()

#write headers
outSheet.write("A1","ID")
outSheet.write("B1","From Date")
outSheet.write("C1","To Date")
user_replied_set = set()

for m in all_messages:
     message = client.messages(m.sid).fetch()
     #print(message.direction + ", " + message.body + ", " + message.from_)
     print("message is ", message.body)
     print("did regex matched?", bool(re.match("[0-9]+\/[0-9]+", message.body)))
     if(message.direction == "inbound" and 
          message.date_sent > from_date_time_timezone and message.date_sent < to_date_time_timezone and 
          re.match("[0-9]+\/[0-9]+", message.body)):
          print("User reply is valid")
          user_replied_set.add(message.from_)
     
print("Final set of users who replied is ", user_replied_set)
i = 1;
for key in copaH:
     print("current key is ", key)
     if(key not in user_replied_set):
          outSheet.write(i,0,copaH.get(key))
          outSheet.write(i,1,from_date_time.isoformat())
          outSheet.write(i,2,to_date_time.isoformat())
          i = i+1

     
outWorkbook.close()






