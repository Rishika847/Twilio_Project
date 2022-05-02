from twilio.rest import Client
import xlrd
import random

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

# TO_DO: Mask these keys
account_sid = ''
auth_token = ''

client = Client(account_sid, auth_token)


message_from = ''
message_to_list_copa = []
message_to_list_copa_test = []

m1 = "Congratulations from COPA health on taking this step towards your good health. May I know your blood pressure today?"
m2 = "COPA health hopes you get much better today. May I know your blood pressure today?"
m3 = "We at COPA health are thinking of your health and hoping you are  too. May I know your blood pressure today?"
m4 = "You are doing fantastic. We at COPA health are excited to see your progress. May I know your blood pressure today?"
m5 = "COPA health is  thrilled to say that we can do this together. May I know your blood pressure today?"
m6 = "We at COPA health think you are stronger than you believe. Keep going. May I know your blood pressure today?"
m7 = "COPA health is rooting for you to be steadier, stronger and better every day. May I know your blood pressure today?"
m8 = "COPA health is sending good, healthy vibes your way. May I know your blood pressure today?"
m9 = "COPA health wants you to take care of yourself. May I know your blood pressure today?"
m10 = "Just a reminder that everyone at COPA health is wishing for your good health. May I know your blood pressure today?"

message_template_list = [m1, m2, m3, m4, m5, m6,m7, m8, m9, m10]
message_body = random.choice(message_template_list)

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


for phone_number in message_to_list_copa:
     print("### sending message to phone number", phone_number)
     message = client.messages \
                    .create(
                         body= message_body,
                         from_= message_from,
                         to= phone_number
                    )

     print(message.sid)
















