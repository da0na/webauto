# coding=utf-8
from util.ShowapiRequest import ShowapiRequest
# import base64

# r = ShowapiRequest("http://route.showapi.com/184-4", "62626", "d61950be50dc4dbd9969f741b8e730f5")
r = ShowapiRequest("http://route.showapi.com/184-4","85060","624075410c1f4901b124f1110b93b90e")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_ipg", "0")
# r.addBodyPara("needMorePrecise", "0")
r.addFilePara("image", r"/Users/daona/PycharmProjects/webauto/imooc1.png")
res = r.post()
print(res.text)
