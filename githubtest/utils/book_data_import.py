__author__ = 'wanderknight'
__time__ = '2020/2/12 16:28'

"""将豆瓣爬取的数据books_subject.xlsx文件数据提取出来，放入数据库
# todo:部分导入数据错误未解决，具体查看导入输出错误
"""
import os
from apps.book.models import Book
import xlrd
""" 导入 top_order中文.xlsx 图书数据"""
def import_top_order():
    book_subject_data_path_top_order = os.path.join(os.getcwd(), 'utils/top_order中文.xlsx')

    xlsx = xlrd.open_workbook(book_subject_data_path_top_order)
    table = xlsx.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    # 获取图书详细信息所有字段
    for row_i in range(1, nrows):
        row = table.row_values(row_i)
        # row[0]如果空数据，类型为字符串，否则为float型
        if not isinstance(row[0], str):
            abook = Book()
            abook.title = row[2]
            abook.title_cn = row[5]
            abook.author_name_str = row[3]
            abook.author_name_str_cn = row[6]
            abook.guten_id = int(row[1])
            abook.guten_down_nums = row[4]

            # 封面图片路径 media/images_cover/
            # 将爬取的图片放入此目录即可
            # abook.cover_img = 'images_cover/' + abook.douban_subject_id + '.jpg'

            try:
                abook.save()
            except Exception as e:
                print(row_i, abook.title, e)
                continue
        else:
            print(row_i, row)
        # print(table.row_types(row_i, 0, 4))
        # if row_i >2 :
        #     break
"""从 book_level5658.xlsx 中，根据id 插入图书难度数据"""
def add_book_level():
    book_subject_data_path_top_order = os.path.join(os.getcwd(), 'utils/book_level5658.xlsx')

    xlsx = xlrd.open_workbook(book_subject_data_path_top_order)
    table = xlsx.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    for row_i in range(1, nrows):
        row = table.row_values(row_i)
        if not isinstance(row[0], str):
            abook = Book.objects.get(guten_id=int(row[1]))
            abook.words_hard_level = row[7]
            abook.frequnce_hard_score = row[4]
            abook.words_nums = row[2]
            abook.aword_nums = row[3]
            try:
                abook.save()
            except Exception as e:
                print(row_i, abook.title, e)
                continue
        else:
            print(row_i, row)
# 如果执行报错，可以使用 alt-b 模式可以执行。
import_top_order()
add_book_level()