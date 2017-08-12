import group
import group_id
import user
import sys
import datetime
'''Creates CSV file with deleted Member ID,Member Name and Member Email ID for channel name passed in argument'''
channel_name=sys.argv[1]
channel_id=group_id.group_id(channel_name)
attrition_csv=open("attrition.csv", 'r+')
head=("Member ID","Member Name", "Member Email ID","Last Date   " )
attrition_csv.write(",".join(head).encode('utf-8') + "\n")
for i in group.group_info(channel_id):
    user_info=user.user(i)
    if user_info["user"]["deleted"]==True:
        last_update=datetime.datetime.fromtimestamp(user_info["user"]["updated"])
        line=(i,user_info["user"]["profile"]["real_name"],user_info["user"]["profile"]["email"], str(last_update))
        attrition_csv.write(",".join(line).encode('utf-8')+ "\n")

attrition_csv.close()