#coding=utf-8
from models import *

# 返回判断上一页下一页显示对象,显示页码数量的列表,每页显示数据条数
class Paging(object):

    def __init__(self,data_object_list,count,pages):
        '''

        :param data_object_list: 接收数据库中取出的对象列表
        :param count: 每页显示的商品条数
        :param pages: 显示的页码条数
        '''
        self.data = data_object_list
        self.count = int(count)
        self.pages=int(pages)
        # 保存临时参数
        self.pre=1


    # 计算总页数,装饰器的作用是在调用函数的时候可以不写()
    @property
    def jspages(self):
        # 计算总页数
        # divmod()返回一个含有两个元素的元祖,第一个元素为商,第二个元素为余数
        nums = divmod(len(self.data), self.count)
        if nums[1] != 0:
            pages = nums[0] + 1
        else:
            pages = nums[0]
        return pages


    # 判断是否有上一页,有返回True,没有返回False
    # 参数dpage为当前页
    def has_pre(self,dpage):
        try:
            dpage=int(dpage)
        except:
            dpage=1
        # 保存前一页
        self.pre = dpage - 1
        if self.pre < 1:
            return False
        else:
            return True



    # 判断是否有下一页,有返回True,没有返回false
    # 参数dpage为当前页
    def has_next(self,dpage):
        try:
            dpage = int(dpage)
        except:
            dpage = 1
        self.pre = dpage + 1
        # 获取总页数
        pages = self.jspages
        if self.pre > pages:
            return False
        else:
            return True



    # 返回当前页的所有商品的对象列表
    # 参数为当前的页码
    def current_page(self,dpage):
        try:
            dpage = int(dpage)
        except:
            dpage = 1

        # 获取当前页全部商品的起始位置
        start = (dpage-1)*self.count
        # 获取当前页全部商品的结束位置
        end = dpage*self.count

        # 如果当前页的最后一个商品的个数<总商品的个数就显示start到end的商品
        if end<len(self.data):
            dataPages = self.data[start:end]
        else:
            dataPages=self.data[start:]
        return dataPages

    # 返回页码
    def pageList(self,dpage):
        try:
            dpage = int(dpage)
        except:
            dpage = 1

        # 根据当前页计算显示的起始位置
        start = dpage - self.pages / 2
        # 根据当前页计算显示的结束位置
        end = dpage + self.pages / 2
        # 计算最后一组页码的起始位置
        endstart = self.jspages - self.pages
        # 创建保存页码的列表
        page_list = []

        # 如果当前页<显示的页数的一半则点击的时候显示的为当前页
        if dpage<=self.pages/2:
            for i in range(1,self.pages+1):
                page_list.append(i)

        # 如果点击的当前页>总页数-显示页的一半的时候,点击的时候显示当前页
        elif dpage>=self.jspages-self.pages/2:
            print endstart,'endstart'
            print self.jspages,'self.jspages'
            for i in range(endstart+1,self.jspages+1):
                page_list.append(i)


        # 否则点击的当前页前面+显示页数的一半,后面+显示页数的一般
        # 当前页一直在中间
        else:
            for i in range(start, end + 1):
                page_list.append(i)
        return page_list
