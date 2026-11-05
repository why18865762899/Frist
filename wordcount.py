# -*- coding :utf_8-*-
"""
第一周练习：词频统计
练习点：变量/字典/循环/函数/文件读写/异常处理

用法：
    python word count.py        #用下面自带的示例文本
    python wordcount。py 某个文件.txt #统计个人自己的文本文件
"""

import sys      #用户来读取命令行参数
import re       #用来按规则切分单词

DEMO_TEXT = """"
the cat sat on the mat 
the dog sat on the log
a cat and a dog  and a mat 
the end off the beginning and the beginning of the end
"""

def count_words(text):
    """统计每个单词出现的次数，返回一个字典：{单词：次数}"""
    counts =  { } #空字典，用来存结果
    wrds = re.findall(r"[a-zA-Z]+",text.lower())    #转小写后按字母切词
    for w in wrds:
        counts[w] = counts.get(w,0)+1
    return counts



def top_n(counts,n=5):
    #按出现次数从高拍的到低，取前n个
    #sorted 的 key参数：告诉它“按字典的值（次数）排”
    items = sorted(counts.itens(),key=lambda kv: kv[1],reverse=True)
    return items[:n]

def main():
    '''主函数：拿到文本->统计->打印'''
    if len (sys.argv)>1:                 #用户传了文件名
        path = sys.argv[1]
        try:
            with open(path,"r",encoding="utf-8") as f:
                text = f.read()
        except FileNotFoundError:
            print ("找不到文件：",path)
            return                      #出错就提前结束
    else :                              #没传就用示例文本
        text = DEMO_TEXT


    counts = count_words(text)          #统计词频
    print ("一共",len(counts),"个不同的单词")
    print ("-" * 30)
    for word,times in top_n(counts,5):
        print (f"{word:<10}{times:>3}次")
    print ("-"*30)


    if __name__=="__main__":        #只有直接运行这个文件时才执行main()
        main()