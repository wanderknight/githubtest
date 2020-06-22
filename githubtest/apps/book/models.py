from django.db import models
from db.base_model import BaseModel


# Create your models here.
class Book(BaseModel):
    """图书模型类
    ref:https://book.douban.com/subject/4255374/"""
    status_choices = (
        (1, '小学'), (2, '初中'), (3, '高中'), (4, '四级'),
        (5, '考研'), (6, '六级'), (7, '专四'), (8, '专八'),
    )
    title = models.CharField(max_length=200, verbose_name='书名')  # 英文书名 The Monkey's Paw
    title_cn = models.CharField(max_length=100, verbose_name='中文书名', blank=True)  # 中文书名 猴爪

    # cover_img = models.ImageField(upload_to='images_cover/', verbose_name='图书封面', blank=True)  # 图书封面
    author_name_str = models.CharField(max_length=2000, verbose_name='作者名', blank=True)  # 作者:Edgar Allan Poe
    author_name_str_cn = models.CharField(max_length=2000, verbose_name='作者名', blank=True)  # 作者: 爱伦坡
    subtitle = models.CharField(max_length=200, verbose_name='副标题', blank=True)  # 副标题: 巴巴爸爸经典系列

    words_hard_level = models.SmallIntegerField(choices=status_choices, verbose_name='词级难度', default=4, blank=True,
                                                null=True)  # 默认四级
    frequnce_hard_score = models.DecimalField(max_digits=6, decimal_places=4, verbose_name='词频难度', blank=True,
                                              null=True)  # hard_score
    words_nums = models.IntegerField(verbose_name='单词数', blank=True, null=True)  # words_length
    aword_nums = models.IntegerField(verbose_name='不同词数', blank=True, null=True)  # aword_length
    guten_id = models.IntegerField(verbose_name='引用id', blank=True, null=True)  # excel id
    guten_down_nums = models.IntegerField(verbose_name='下载次数', blank=True, null=True)  # excel extra
    # 以下为备选字段，暂时不使用
    publisher_name = models.CharField(max_length=100, verbose_name='出版社名', blank=True)  # 出版社: 接力出版社
    publisher_co_name = models.CharField(max_length=100, verbose_name='出品方', blank=True)  # 浦睿文化
    translator_name = models.CharField(max_length=100, verbose_name='译者名', blank=True)  # 任战
    time_str = models.CharField(max_length=20, verbose_name='出版时间字符', blank=True)
    time = models.DateField(verbose_name='出版时间', blank=True, null=True)  # 出版年: 2010-1
    page_num_str = models.CharField(max_length=20, verbose_name='页数字符', blank=True)
    page_num = models.SmallIntegerField(verbose_name='页数', blank=True, null=True)  # 页数: 30
    price_str = models.CharField(max_length=20, verbose_name='定价字符', blank=True, )  # 定价: 12.00元
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='定价', blank=True, null=True)  # 定价: 12.00元
    binding = models.CharField(max_length=50, verbose_name='装帧', blank=True)  # 装帧: 平装
    # 丛书: 巴巴爸爸经典系列·度假篇
    isbn = models.CharField(max_length=15, verbose_name='ISBN', blank=True)  # ISBN: 9787544810807
    douban_score = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='豆瓣评分', blank=True,
                                       null=True)  # 9.4
    douban_score_num = models.IntegerField(verbose_name='人数', blank=True, null=True)  # 179
    content_intro = models.TextField(max_length=10000, verbose_name='内容简介', blank=True)  #
    author_intro = models.TextField(max_length=10000, verbose_name='作者简介', blank=True)  #

    douban_subject_id = models.CharField(max_length=15, verbose_name='豆瓣ID', blank=True)  # 34778306
    douban_pid_id = models.CharField(max_length=15, verbose_name='豆瓣图片ID', blank=True)  # s33445293
    douban_series_id = models.CharField(max_length=10, verbose_name='丛书id', blank=True)  # 丛书id：49867

    author = models.ManyToManyField('Author', through='BookAuthor', verbose_name='作者', blank=True)  # 作者: (法)缇森 / (法)泰勒

    info_comp = models.NullBooleanField(verbose_name='信息完整', default=False)  # 完整:True; 不完整：False

    # @property
    # def cover_img_url(self):
    #     if self.cover_img and hasattr(self.cover_img, 'url'):
    #         return '/' + self.cover_img.url

    class Meta:
        db_table = 'book'
        verbose_name = '图书'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title + ' ' + str(self.publisher_name) + ' ' + str(self.time_str)


class Author(BaseModel):
    """作者信息
    ref:https://book.douban.com/author/104119/"""
    status_choices = (
        (True, '女'),
        (False, '男'),
    )
    first_name = models.CharField(max_length=20, verbose_name='first_name')
    last_name = models.CharField(max_length=20, verbose_name='last_name', blank=True)
    gender = models.NullBooleanField(choices=status_choices, verbose_name='性别', default=False)  # 女:True; 男：False
    birth = models.DateField(verbose_name='出生日期', blank=True, null=True)  # 出生日期: 1954年
    country = models.CharField(max_length=20, verbose_name='国家/地区', blank=True)  # 国家/地区: 美国

    class Meta:
        db_table = 'author'
        verbose_name = '作者'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.first_name + self.last_name


class BookAuthor(BaseModel):
    """多对多表"""
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    translator = models.BooleanField(verbose_name='译者', default=False)  # True:译者; False:作者

    class Meta:
        db_table = 'bookauthor'
        verbose_name = '图书作者'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.book) + ' ' + str(self.author)
