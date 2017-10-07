# encoding: utf-8
# 处理Excel文件

# 4.3 开始解析
import pprint
import xlrd
book = xlrd.open_workbook('SOWC 2014 Stat Tables_Table 9.xlsx')
sheet = book.sheet_by_name('Table 9 ')
# for sheet in book.sheets():
#   print sheet.name
# print dir(sheet)
# print sheet.nrows
# print sheet.ncols

nrows = sheet.nrows
rows = sheet.row_values

data = {}
# 这一段的逻辑不准确
# for i in range(nrows):
#   if i < 10 and i >= 14:
#     row = rows(i)
#     country = row[1]
#     data[country] = {}
# print data

# {u'Afghanistan': {}, u'Albania': {}, u'Angola': {}, u'Algeria': {}, u'Andorra': {}, u'Austria': {}, u'Australia': {}, u'Antigua and Barbuda': {}, u'Armenia': {}, u'Argentina': {}}
# version 0.0.1
# count = 0
# for i in xrange(nrows):
#   if count < 10:
#     if i >= 14:
#       row = rows(i)
#       country = row[1]
#       data[country] = {}
#       count += 1
# print data


# version 0.0.2
data = {}
for i in xrange(14, nrows):
    row = rows(i)
    country = row[1]

    data[country] = {
      'child_labor': {
        'total': [row[4], row[5]],
        'male': [row[6], row[7]],
        'female': [row[8], row[9]],
      },
      'child_marriage': {
        'married_by_15': [row[10], row[11]],
        'married_by_18': [row[12], row[13]],
      }
    }

    if country == 'Zimbabwe':
        break


# print data
pprint.pprint(data)
