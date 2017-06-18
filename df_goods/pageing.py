#coding=utf-8
from models import *

# 返回判断上一页下一页显示对象,显示页码数量的列表,每页显示数据条数
class Paging(object):

    def __init__(self,data_object_list,count,pages):
        # 保存对象列表
        self.data = data_object_list
        # 每页展示的商品条数
        self.count = int(count)
        # 显示的页码个数
        self.pages=int(pages)
        self.pre=1


    # 计算总页数
    def jspages(self):
        # 计算总页数
        num1 = len(self.data) % self.count
        num2 = len(self.data) / self.count

        if num1 != 0:
            pages = num2 + 1
        else:
            pages = num2
        return pages


    # 判断是否有上一页,有返回True,没有返回False
    # 参数page为当前页
    def has_pre(self,dpage):

        dpage=int(dpage)
        self.pre = dpage - 1
        # 计算总页数
        pages = self.jspages()
        # 判断如果总页数-当前页等于总页数-1,则表示没有前一页
        #if pages-dpage==pages-1:
        if self.pre < 1:
            return False
        else:
            return True



    # 判断是否有下一页,有返回True,没有返回false
    # 参数page为当前页
    def has_next(self,dpage):
        dpage=int(dpage)
        self.pre = dpage + 1
        pages = self.jspages()
        print pages,'总页数'
        print self.pre,'下一页'
        print dpage,'当前页'
        # 如果当前页等于总页数表示最后一页
        if self.pre > pages:
            return False
        else:
            return True



    # 返回当前页的所有商品的对象列表
    # 参数为当前的页码
    def current_page(self,dpage):
        dpage=int(dpage)
        # 获取上一页的页码
        #self.pre = dpage - 1

        # 获取当前页全部商品的起始位置
        start = (dpage-1)*self.count
        # 获取当前页全部商品的结束位置
        end = dpage*self.count


        if end<len(self.data):
            #print start, 'start'
            dataPages = self.data[start:end]

        else:

            dataPages=self.data[start:]

            print dataPages
        return dataPages

    # 显示页码
    def d_pages(self,dpage):
        dpage=int(dpage)

        # 获取总页数
        zpages = self.jspages()
        page_list = []
        # 获取商品总条数
        # nums = len(self.data)
        # 列表切片,取出当前页商品对象列表
        # if dpage>zpages-self.pages:
        #     for i in range(zpages-self.pages,zpages+1):
        #         page_list.append(i)

        # 如果总页数-当前页数>设定的显示页数
        if zpages-dpage>=self.pages:
            # 创建一个从当前页数到显示页数+当前页数的一个列表,此时的列表长度为5
            for i in range(dpage,self.pages+dpage):
                page_list.append(i)

        else:
            # 否则创建一个当前页到最后一页的列表
            for i in range(dpage,zpages+1):
                page_list.append(i)
        return page_list


