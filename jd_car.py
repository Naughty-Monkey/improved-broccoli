# !/usr/bin/python
# encoding:utf-8

import requests
'''
东东工厂互助码api
http://api.turinglabs.net/api/v1/jd/ddfactory/create/互助码/
查看上车人数
http://api.turinglabs.net/api/v1/jd/ddfactory/count/
京喜工厂互助码api
http://api.turinglabs.net/api/v1/jd/jxfactory/create/互助码/
查看上车人数
http://api.turinglabs.net/api/v1/jd/jxfactory/count/
种豆提交互助码api
http://api.turinglabs.net/api/v1/jd/bean/create/互助码/
查看上车人数
http://api.turinglabs.net/api/v1/jd/bean/count/
农场提交互助码api
http://api.turinglabs.net/api/v1/jd/farm/create/互助码/
查看上车人数
http://api.turinglabs.net/api/v1/jd/farm/count/
萌宠提交互助码api
http://api.turinglabs.net/api/v1/jd/pet/create/互助码/
查看上车人数
http://api.turinglabs.net/api/v1/jd/pet/count/
京东赚赚小程序互助码api (由@C_Hiang提供) 
https://code.chiang.fun/api/v1/jd/jdzz/create/助力码/
查看上车人数 (由@C_Hiang提供)
https://code.chiang.fun/api/v1/jd/jdzz/count
疯狂的joy随机互助 互助码提交api  
https://code.chiang.fun/api/v1/jd/jdcrazyjoy/create/助力码/
查看上车人数 
https://code.chiang.fun/api/v1/jd/jdcrazyjoy/count
查看数据库清空时间
http://api.turinglabs.net/api/v1/jd/cleantimeinfo/
'''

ddfactory = 'http://api.turinglabs.net/api/v1/jd/ddfactory/create/'
ddfactorydata = [
    'P04z54XCjVWnYaS5m9cZ2T8jHtClo3r5O6-Eb8',
    'P04z54XCjVWnYaS5m9cZ2Tx1HxDxPs74NYHUoM'
]

jxfactory = 'http://api.turinglabs.net/api/v1/jd/jxfactory/create/'
jxfactorydata = ['8updD7dNNEL5tBKxpTFNkA==', '851ud6_c5-m_3airK6G8sA==']

bean = 'http://api.turinglabs.net/api/v1/jd/bean/create/'
beandata = [
    'e7lhibzb3zek2dktkljvmo43uohuhjqugn6cyoq',
    'e7lhibzb3zek2ges5ohy5fuslnkzpnpvp6pbq5q'
]

farm = 'http://api.turinglabs.net/api/v1/jd/farm/create/'
farmdata = [
    '4b51eaf8933d44abb12b0ff10970f29f', 'e08aaa769c69449cb6e44b637405a96c'
]

pet = 'http://api.turinglabs.net/api/v1/jd/pet/create/'
petdata = [
    'MTAxODc2NTEzMjAwMDAwMDAyOTU1NjE0MQ==',
    'MTAxODc2NTE0NzAwMDAwMDAzMDM0NDY1Nw=='
]

jdzuanzuan = 'https://code.chiang.fun/api/v1/jd/jdzz/create/'
zuanzuandata = ['AUWE5m6nByj0LCDL72X0flg', 'AUWE5m6SZzTxZDmL7iX9Oww']

crazyjoy = "https://code.chiang.fun/api/v1/jd/jdcrazyjoy/create/"
crazydata = [
    'sngyJDZUUCeLzVpFOk1Koqt9zd5YaBeE', 'bMjQ1EEe5lt3muWcWb5DHKt9zd5YaBeE'
]


def get(link, data):
    for i in data:
        url = link + i
        print(url)
        r = requests.get(url)
        print(r.text)


get(ddfactory, ddfactorydata)
get(jxfactory, jxfactorydata)
get(bean, beandata)
get(farm, farmdata)
get(pet, petdata)
get(jdzuanzuan, zuanzuandata)

print("finished")
