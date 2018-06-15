# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class QiubaiPipeline(object):
    def __init__(self):
        self.sql = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='mini1314520', db='qsbk', charset='utf8')
        self.cursor = self.sql.cursor()

    def process_item(self, item, spider):
        '''
        item接受的数据是一条一条的保存的，对每一条数据进行逐个处理
        :param item:
        :param spider:
        :return:'''
        # print(type(item))
        # <class 'qiubai.items.QiubaiItem'>
        # print(item)
        # print(len(item))
        # print(item.table_name)
        # 如果'table_name'属性存在，则返回true
        if not hasattr(item, 'table_name'):
            return item
        cols, values = zip(*item.items())
        # print(cols, values)
        # join的使用只能是字符串的拼接
        sql = 'insert into {}({})VALUES({})'.format(item.table_name, ",".join(cols), ','.join(["'%s'"]*len(values)) % values)
        self.cursor.execute(sql)
        self.sql.commit()
        return item
    def close(self):
        self.cursor.close()
        self.sql.close()


'''
关于字典 和 zip小解
lt = {1:1, 2:3}
clos, values = zip(*lt.items())
print(clos) ------  (1, 2)
print('33333') ------
print(values) ------(1, 3)

lt1 = ['a','b','c']
lt2 = [1,2,3]
lt3 = list(zip(lt1,lt2)) 
print(lt3)  ------ [('a', 1), ('b', 2), ('c', 3)]
print(dict(lt3))  ---- {'a': 1, 'b': 2, 'c': 3}

关于※号的使用
c, d =  [1, 2]    
a, b = [1,2,3]  ---- 报错
a, *b = [1,2,3]
print(a,b)  --- 1 [2, 3]  b是一个列表
print(c, d)  ----  1 2

print(lt.items()) ----- dict_items([(1, 1), (2, 3)])
print(type(lt.items()))  ---- <class 'dict_items'>
print(*lt.items())   ----(1, 1) (2, 3)
'''
