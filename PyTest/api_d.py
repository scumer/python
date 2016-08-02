# coding=utf-8

from requests import get, post


url_pfx = r'http://pacs.winning.com.cn/pat_test/'


# cards
ret = get(url_pfx+'api/cards', params={'openid':'123456'})
print ret.text


# reports
ret = get(url_pfx+'api/reports', params={'openid':'123456'})
print ret.text


# queues
ret = get(url_pfx+'api/queues', params={'openid':'123456'})
print ret.text

[{"card": "1234567890", "city": "\u5e38\u5dde", "hospital": "\u536b\u5b81", "name": "\u7329\u7ea2\u5973\u5deb", "sex": "\u5973"}, {"card": "0987654321", "city": "\u5e38\u5dde", "hospital": "\u516d\u9662", "name": "\u7eff\u5de8\u4eba", "sex": "\u7537"}]
[{"hospital": "\u536b\u5b81\u516d\u9662", "id": "121", "name": "\u7329\u7ea2\u5973\u5deb", "reportdesc": "CT", "reporttime": "2016-06-11"}, {"hospital": "\u4e0a\u6d77\u516d\u9662", "id": "171", "name": "\u7329\u7ea2\u5973\u5deb", "reportdesc": "DX", "reporttime": "2016-05-11"}]
[{"item": "CT\u80f8\u90e8\u5e73\u626b", "name": "\u9ed1\u5be1\u5987", "queueno": "\u5e73\u626b008", "queuenum": "17", "sex": "\u5973"}, {"item": "CT\u80f8\u90e8\u5e73\u626b", "name": "\u5965\u521b", "queueno": "\u666e\u653e009", "queuenum": "30", "sex": "\u7537"}]