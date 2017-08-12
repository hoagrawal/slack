import group
import group_id
import user
import sys
import datetime
'''Creates CSV file with deleted Member ID,Member Name and Member Email ID for channel name passed in argument'''
channel_name=sys.argv[1]
channel_id=group_id.group_id(channel_name)
group_detail_csv=open("attrition.csv", 'w')
head=("Member ID","Member Name", "Member Email ID" )
group_detail_csv.write(",".join(head).encode('utf-8') + "\n")
for i in group.group_info(channel_id):
    user_info=user.user(i)
    if user_info["user"]["deleted"]==True:
        last_update=datetime.datetime.fromtimestamp(user_info["user"]["updated"])
        print last_update
        line=(i,user_info["user"]["profile"]["real_name"],user_info["user"]["profile"]["email"], str(last_update))
        group_detail_csv.write(",".join(line).encode('utf-8')+ "\n")
group_detail_csv.close()