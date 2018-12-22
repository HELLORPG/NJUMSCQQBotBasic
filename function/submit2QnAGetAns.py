
# -*- coding: utf-8 -*-

import http.client, urllib.parse, json, time
import random
from pprint import pprint
# a valid host name.
host = "se-service-robot.azurewebsites.net"

endpoint_key = "31d46bf3-7424-4f6f-812e-ba0b536c503c"

# a valid knowledge base ID.
# Make sure you have published the knowledge base with the
# POST /knowledgebases/{knowledge base ID} method.


question = {
    'question': '你是谁呀',
    'top': 1
}


def pretty_print(content):
    # Note: We convert content to and from an object so we can pretty-print it.
    # print ("content"+content)
    return json.dumps(json.loads(content), indent=4)


def get_answers(content):
    kb = "d4e8a182-75a4-4fd5-a07f-3709a969d63a"

    path = "/qnamaker/knowledgebases/" + kb + "/generateAnswer"

    print ('Calling ' + host + path + '.')
    headers = {
        'Authorization': 'EndpointKey ' + endpoint_key,
        'Content-Type': 'application/json',
        'Content-Length': len(content)
    }
    conn = http.client.HTTPSConnection(host)
    conn.request ("POST", path, content, headers)
    response = conn.getresponse()

    return response.read()


def get_answers_from_file(content):
    with open("files/qna.json","r",encoding="UTF-8") as qna:
        qna_list = json.load(qna)
        for item in qna_list["qna"]:
            if item["intent"] == content:
                return item["answers"][random.randint(0, len(item["answers"]) - 1)]
        return "No answer"

# Convert the request to a string.
# content = json.dumps(question)
# result = get_answers_from_file("你好")
# print(result)
# print(pretty_print(result).encode('utf-8').decode('unicode_escape'))
