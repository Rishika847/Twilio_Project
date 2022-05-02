#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

import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)

SENDGRID_API_KEY = ''


message = Mail(
    from_email='',
    to_emails='',
    subject='Reminder email for COPA Health Hypertension Home Monitoring project.',
    html_content='''<strong>Dear Supervisor,
We at ASU are thrilled to let you know that the COPA Health Hypertension Home Monitoring project is functioning well.
We have attached the following data for your reference,
List of patient’s blood pressure values for this week (Highlighted in red are the abnormal values).
List of the patient’s who did not respond to the texts in the last 2 weeks.
Thank you for taking your time in working through this.

Regards,
Team ASU.
</strong>''')



try:
    with open('out.xlsx', 'rb') as f:
        f_data = f.read()
        f_encoded = base64.b64encode(f_data).decode()
        f.close()
except Exception as e:
    raise e
myattachment1 = Attachment()
myattachment1.file_content = FileContent(f_encoded)
myattachment1.file_name =  FileName('out.xlsx')
myattachment1.file_type = FileType("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
myattachment1.disposition =  Disposition("attachment")

try:
    with open('no_replies_list.xlsx', 'rb') as f:
        f_data = f.read()
        f_encoded = base64.b64encode(f_data).decode()
        f.close()
except Exception as e:
    raise e
myattachment2 = Attachment()
myattachment2.file_content = FileContent(f_encoded)
myattachment2.file_name =  FileName('no_replies_list.xlsx')
myattachment2.file_type = FileType("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
myattachment2.disposition =  Disposition("attachment")



message.attachment = [myattachment1, myattachment2]

try:
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
