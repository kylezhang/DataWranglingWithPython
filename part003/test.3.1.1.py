# encoding: utf-8
# mechine readable data 供机器读取的数据

# 3.1.1 处理CSV数据
# 数据来源
# http://apps.who.int/gho/athena/data/data-text.csv?target=GHO/WHOSIS_000002,WHOSIS_000001,WHOSIS_000015&profile=text&filter=COUNTRY:*;REGION:AFR;REGION:AMR;REGION:SEAR;REGION:EUR;REGION:EMR;REGION:WPR;SEX:*
import csv

csvfile = open('data-text.2.csv', 'rb')
reader = csv.reader(csvfile)

for row in reader:
	print row
