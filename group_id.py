import requests
import json
import config

def group_id(channel_name):
    '''Returns Group/channel id for given channel name'''
    url = "https://slack.com/api/groups.list"

    querystring = {"token":config.read_config("SLACK_TOKEN")}

    response = requests.request("GET", url, params=querystring)
    resp_dict = json.loads(response.content)["groups"]
    for group in range(len(resp_dict)) :
        if resp_dict[group]["name"]==channel_name:
            break
    return resp_dict[group]["id"]