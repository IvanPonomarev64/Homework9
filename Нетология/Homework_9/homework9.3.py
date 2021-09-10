import requests

from pprint import pprint

def get_questions():
    PARAMS = {
        'fromdate' : '2021-09-07',
        'todate' : '2021-09-09',
        'tagged' : 'Python',
        'site' : 'stackoverflow'
    }
    url = "https://api.stackexchange.com/2.3/questions"
    response = requests.get(url, params = PARAMS)
    for question in response.json().get('items'):
        pprint('Question:'  + question['title'])
        pprint('Tags: ' + str(question['tags']))

get_questions()

