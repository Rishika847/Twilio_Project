from twilio.rest import Client
import xlrd

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

# TO_DO: Mask these keys
account_sid = ''
auth_token = ''

client = Client(account_sid, auth_token)

message_body = "Hi, we are still awaiting your blood pressure readings.- This message is being sent to you as a part of the Copa Health-ASU research study"
message_from = ''
message_to_list_copa = []

# read copa info file
# read the phone numbers column
# extract all the phone numbers in the list as string

file_location = "/Users/rishikasharma/desktop/RishikaCode/demo/copa_info.xlsx"
workbook= xlrd.open_workbook(file_location)
sheet= workbook.sheet_by_index(0)

# add all the phone numbers in the list
for i in range(1,sheet.nrows):
     message_to_list_copa.append(sheet.cell_value(i,1))
     #print(sheet.cell_value(i,0))
     #print(sheet.cell_value(i,1))

     
print("### printing phone numbers copa list started: ")
for i in range(0, len(message_to_list_copa)):   
     print(message_to_list_copa[i])

print("### printing phone numbers copa list completed")

def get_responders_set():
     responder_set = {"", "", ""}

     all_messages = client.messages.list()
     some_messages = client.messages.list(limit=100)

     for m in some_messages:
          message = client.messages(m.sid).fetch()
          time = message.date_sent
          sender = message.from_
          body = message.body
          direction = message.direction

          if() :
               responder_set.add(sender)
     return responder_set

responder_set = get_responders_set()
for phone_number in message_to_list_copa:

     if phone_number not in responder_set:
          print("### sending message to phone number", phone_number)
          message = client.messages \
                    .create(
                         body= message_body,
                         from_= message_from,
                         to= phone_number
                    )

          print(message.sid)
















