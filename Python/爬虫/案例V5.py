'''
利用parse模块模拟post请求
分析百度词典
分析步骤：
1.打开F12
2.尝试输入单词girl，发现每敲一个字母后都有请求
3.请求地址是：http://fanyi.baidu.com/sug
4.利用Network->ALL->Headers，查看发现FormData的值是kw：gril
5.检查返回格式内容，发现返回的是json格式内容->需要用到json包
'''


from urllib import request,parse
# 负责处理json格式的模块
import json

'''
大致流程是：
1.利用data构造内容，然后urlopen打开
2.返回一个json格式的结果
3.结果就应该是girl的释义
'''

baseurl = 'http://fanyi.baidu.com/sug'


kw = input("Input your keyword:")
# 存放用来模拟form的数据一定是dict格式
data = {
    # girl是翻译输入的英文内容,应该是由用户输入,此处使用硬编码
    #"kw":"girl"
    "kw":kw # 之后自行修改的结果
}

data = parse.urlencode(data).encode()
print(data)

# 我们需要构造一个请求头，请求头应该至少包含传入的数据的长度
# request要求传入的请求头是一个dict格式
headers = {
    # 因为使用post，至少应该包含content-length字段
    'Content-Length':len(data)
}

# 有了headers，data，url，就可以尝试发出请求了
# urlopen中没有headers这个参数，无法满足隐藏身份的需求
rsp = request.urlopen(baseurl,data=data)

# 解码后是乱码,并不是UTF-8编码
json_data = rsp.read().decode()
#print(json_data)

# 把json字符串转化成字典
json_data = json.loads(json_data)
print(type(json_data))
print(json_data)

# 解开KV对
for item in json_data["data"]:
    print(item["k"],"-->",item['v'])