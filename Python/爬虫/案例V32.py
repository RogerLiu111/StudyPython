from lxml import etree

# 只能读取xml格式内容，html报错
html = etree.parse("./案例V29.xml")
print(type(html))

rst = html.xpath('//book')
print(type(rst))
print(rst)

print("*"*30)
# xpath的意思是，查找带有category属性值为sport的book元素，正确用法需要增加方括号[]
rst = html.xpath('//book/@category="sport"')
print(type(rst))
print(rst)
print("*"*30)
# xpath的意思是，查找带有category属性值为sport的book元素，上面是个错误例子，不是我们想要得到的结果
rst = html.xpath('//book[@category="sport"]')
print(type(rst))
print(rst)
print("*"*30)
# xpath的意思是，查找带有category属性值为sport的book元素下的year
rst = html.xpath('//book[@category="sport"]/year')
print(rst)
rst = rst[0]
print(type(rst))
print(rst)
print(rst.tag)
print(rst.text)