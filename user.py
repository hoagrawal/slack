import requests
import json
import config


def user(userid):
    url = "https://slack.com/api/users.info"
    querystring = {"token":config.read_config("SLACK_TOKEN"),"user":userid}
    response = requests.request("GET", url, params=querystring)
    resp_json=json.loads(response.content)
    return resp_json
