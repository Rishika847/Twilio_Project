print("This is from cron testing")
print("***Testing successful***")


#which python3: /opt/homebrew/bin/python3
#pwd: /Users/rishikasharma/Desktop/RishikaCode/demo
# cron test1: * * * * * /opt/homebrew/bin/python3 /Users/rishikasharma/Desktop/RishikaCode/demo/cron_test.py>/tmp/cronTest.log
# cron test2: send message: * * * * * /opt/homebrew/bin/python3 /Users/rishikasharma/Desktop/RishikaCode/demo/sms_send.py>/tmp/cronTest.log
# crontab -e: to open the file
# give mac permission: https://osxdaily.com/2020/04/27/fix-cron-permissions-macos-full-disk-access/
# check logs: /tmp/cronTest.log


#Monday: 00 13 * * 1 /opt/homebrew/bin/python3 /Users/rishikasharma/Desktop/RishikaCode/demo/sms_send.py
#Thursday: 00 13 ** 4 /opt/homebrew/bin/python3 /Users/rishikasharma/Desktop/RishikaCode/demo/sms_send.py
#Monday: 00 8 * * 1 /opt/homebrew/bin/python3 /Users/rishikasharma/Desktop/RishikaCode/demo/sms_send.py