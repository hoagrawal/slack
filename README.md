**Intro**

This small python program helps fetch Slack Member ID, Member Name and Email ID for SLACK channel name (private) passed as argument on command line.

Assumption: user is member of private channel


**System Requirements**

python 2.7

python **requests** module

generate SLACK_TOKEN for your SLACK team ;refer https://api.slack.com/docs/oauth)

**Execution**
git clone 
cd slack_member
update SLACK_TOKEN in .env 

`SLACK_TOKEN=<insert oauth access token>`

Run below from command line

To get the active members list

`python group_details_csv.py "<channel name>"`


To get the deleted members list (attrition)

`python attrition.py "<channel name>"`

It will generate group_details.csv file which will have Member ID, Member Name and Email ID
