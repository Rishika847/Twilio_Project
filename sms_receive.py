import xlrd
from twilio.rest import Client
import xlsxwriter

# To Do: mask keys
account_sid = ''
auth_token = ''

file_location = "/Users/rishikasharma/desktop/RishikaCode/demo/copa_info.xlsx"

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
all_messages = client.messages.list()
some_messages = client.messages.list(limit=100)
print('Here are the last 100 messages in your account:')

# 3. write data to xlsx file

#create file workbook and worksheet

outWorkbook = xlsxwriter.Workbook("out.xlsx")
outSheet = outWorkbook.add_worksheet()

#write headers
#outSheet.write("A1","Phone Number")
outSheet.write("A1","ID")
outSheet.write("B1","Message")
outSheet.write("C1","Direction")
outSheet.write("D1","Date_Sent")

i = 1;
for m in some_messages:
     one_row = []
     message = client.messages(m.sid).fetch()
     #print(message.direction + ", " + message.body + ", " + message.from_)
     #one_row.append(message.from_)
     one_row.append(copaH.get(message.from_, "user does not exist in copa info"))
     one_row.append(message.body)
     one_row.append(message.direction)
     one_row.append(message.date_sent.isoformat())
     #print("curent list is ", one_row)


     outSheet.write(i,0,one_row[0])
     outSheet.write(i,1,one_row[1])
     outSheet.write(i,2,one_row[2])
     outSheet.write(i,3,one_row[3])
     #outSheet.write(i,4,one_row[4])
     i = i+1

outWorkbook.close()






