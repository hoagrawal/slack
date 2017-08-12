import requests
import json
import config

def group_info(channel_id):
    '''Returns Member list for requested channel'''
    url = "https://slack.com/api/groups.info"

    querystring = {"token":config.read_config("SLACK_TOKEN"),"channel":channel_id}

    response = requests.request("GET", url, params=querystring)
    resp_dict = json.loads(response.content)
    return resp_dict["group"]["members"]