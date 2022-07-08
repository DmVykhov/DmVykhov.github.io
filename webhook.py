import requests
import json

webhook_url = "http://127.0.0.1:5000/webhook"
data = {
    "project": 0,
    "url": "https://DmVykhov.github.io",
    "send_payload": True,
    "send_for_all_actions": True,
    "headers": {},
    "is_active": True,
    "actions": ['ANNOTATION_CREATED','ANNOTATION_UPDATED','ANNOTATIONS_DELETED']
}
r = requests.post(webhook_url, data=json.dumps(data), headers = {'Content-Type':'application/json'})
