import requests
import json 
web_hook_url= 'https://hooks.slack.com/services/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'

slack_msg = {'text':'Alert from python'}

requests.post(web_hook_url,data=json.dumps(slack_msg))
