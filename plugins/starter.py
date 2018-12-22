from function.submit2LUISandGetPrediction import get_prediction
# GRP ADD BEGIN
from function.EntitiesSwitch import *
from function.submit2QnAGetAns import *

import time
import json

# GRP ADD END

from none import on_natural_language,NLPSession


SUBSCRIPTION_KEY_ENV_NAME = "36fb4cae87a246169da2edf98e082113"


@on_natural_language(keywords=('',), only_to_me=False)  # 关掉only_to_me可应答群消息
async def get_massage(session: NLPSession):

    start = time.clock()  # 测试总查询用时
    # 获取用户提问
    question = str(session.msg_text.strip())
    # 将问题发送给LUIS,获取prediction
    prediction = get_prediction(SUBSCRIPTION_KEY_ENV_NAME, question)
    # print("得到的划分为：")
    print(prediction.as_dict())  # 将数据库读取结果作为字典进行输出
    # print ("得到的划分:\n" + prediction.as_dict())

    ans = ""
    print(len(prediction.entities))

    # print (prediction.entities[0].as_dict()['entity'])
    # 判断有无实体
    if len(prediction.entities) > 0:
        # GRP ADD BEGIN
        # entities_index = entities_match(prediction.entities)
        entities_index = entities_module_match(prediction.entities)
        if entities_index == -1:
            ans = ""
            # 在这里可以添加一个对管理员的反馈，此时两端的实体识别不一致，出现了匹配的缺失
        else:
            # ans = entities_ans(entities_index)
            ans = entities_module_ans(entities_index)
        # GRP ADD END
        pass
    else:
        query = {
            'question': question,
            'top': 1
        }
        # content = query.get('question')
        # print("content= "+content)
        # 将prediction发送给QnA maker
        # result = get_answers(content)
        # print (pretty_print(result))
        # ans = pretty_print(result).encode('utf-8').decode('unicode_escape').split('answer')[2].split('"')[2]
        print("ques"+question)
        ans = get_answers_from_file(question)
        print ("ans"+ans)
        # 将ans返回给用户
        if ans=="No answer":
            pass
        else:
            end = time.clock()
            await session.send(ans)




