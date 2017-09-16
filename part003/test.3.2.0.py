# encoding: utf-8
# 处理json数据
# 3.2.0

import json

json_data = open('data-text.json').read()

data = json.loads(json_data)

for item in data:
	print item