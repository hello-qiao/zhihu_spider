# a = """upgrade-insecure-requests: 1
# user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36
# accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
# referer: https://www.baidu.com/link?url=m1f2ZnzCvchX9XJm5_bNQX8ppONkJ5N1b2uK7YL_WHPrsYkNSPzn7nQRT6PRD1cRLom1qkRA__qPXi41xXDZ1U4fVm9heOV-0J9r4arQ6k7&wd=&eqid=eb2dc00700009071000000035bc00877
# accept-encoding: gzip, deflate, br
# accept-language: zh-CN,zh;q=0.9
# Pragma: no-cache
# Cache-Control: no-cache
# """
# header = {}
# b = a.split('\n')
# for c in b :
#     if not c:
#         continue
#     d = c.split(':')
#     # print d
#     header[d[0]] = d[1]
#
# # print header

#codig:utf-8
import requests,json

header = {
    'upgrade-insecure-requests': '1',
    'accept-language': 'zh-CN,zh;q=0.9',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'referer': 'https',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}
num = 22619469
start_urls = ['https://www.zhihu.com/question/']
for i in range(10000):
    page_num = num + i
    url = 'https://www.zhihu.com/question/' + str(page_num)
    # print url
    # res = requests.get(url=url,headers=header,verify =False,timeout=15)
    # print res.text