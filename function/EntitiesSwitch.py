import random

def entities_match(data):
    """函数体，采用switch的方式对传入的data进行分析，识别其中的实体
       如果其中有和列表中实体相同的实体，则返回索引值
       否则，返回-1作为异常标志"""
    entities_list = ["活动部","校运会","技术部","宣传部"]
    # 可以在entities中增加足够多的实体，来完成不同的实体识别
    for entity in data:
        if entity.as_dict()["entity"] in entities_list:
            return entities_list.index(entity.as_dict()["entity"])
    return -1


def entities_ans(index):
    """函数体，采用索引来寻找对应的回答"""
    ans_list = [
        "活动部是搞事情的呀！",
        "校运会的时间是2018.11.2 ~ 2018.11.4",
        "技术部的都很帅",
        "宣传部的都是漂亮的小姐姐和小哥哥",
    ]
    return ans_list[index]

def entities_module_match(data):
    """前面的函数虽然实现了一定的功能，但是在同一大类的实体识别的时候，运维十分的繁琐
       或许可以增加一个以大类进行识别的方式"""

    ask_weather = ["天气","温度"]
    technology_team = ["技术部","技术队","技术家园"]
    activity_team = ["活动部","活动队"]
    #2018.12.16 预备更新，为即将到来的天气预报做准备，将其仍然耦合在原有的结构中

    entities_module_list = [ask_weather, technology_team, activity_team ]
    #2018.12.16 注意天气的问询就成为了特殊的0号索引，在下一部分的函数调用的时候需要小心这一点


    """
    曾用代码：
    for entity in data:
        if entity.as_dict()["entity"] in entities_list:
            return entities_list.index(entity.as_dict()["entity"])
    """
    # entity_module_find = 0
    power = 0.0000000
    # ret_list = ["NULL"]
    ret_index = -1


    for entity_module in entities_module_list:
        for entity in data:
            if entity.as_dict()["entity"] in entity_module:
                # print(float(entity.as_dict()["score"]))
                # return entities_module_list.index(entity_module) #如果是直接返回的话，忽略了权重这一个指标
                if float(entity.as_dict()["score"]) > power:
                    ret_index = entities_module_list.index(entity_module)
    return ret_index


def entities_module_ans(index):
    """与上面的模式化匹配实体相对应，模式化的回应"""
    if index == 0:
        #此时是特殊的天气查询
        return "天气预报"#天气查询的函数

    else:
        index -= 1#此时为了匹配固定位置上的回复函数，采用这样的方法进行重新定位

    technology_team_ans = [
        "技术部都是帅哥靓女",
        "技术部的都是大佬",
        "怎么，据我所知，他们可不会修电脑"
    ]

    activity_team_ans = [
        "活动部是搞事情的呀！",
        "喜欢活动部的小可爱吗？",
        "悄悄告诉你个秘密，我也是活动部的呢",
        "我也喜欢活动部呀",
    ]

    ans_list = [technology_team_ans, activity_team_ans]

    return ans_list[index][random.randint(0, len(ans_list[index]) - 1)]
