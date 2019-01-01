'''
  Copyright (c) 2018 antzhi@163.com, 书上蚂蚁
   
  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

    任何获得本软件副本及相关文档文件(下面简称为“软件”)的个人都可以免费获得不受限制处置本软件的权限，包括不受限制地使用、复制、修改、合并、出版、分发、重新许可或者销售本软件的副本，并且在满足下述条件时，允许本软件的受让人获得下述权限：

    在本软件的所有或者重要部分中包含上述版权公告信息和本权限公告信息。

    本软件不提供保证，不包含任何类型的保证(无论是明指的还是暗喻的)，包含但不限于关于本软件的适销性、特定用途的适用性和无侵权保证。在任何情况下，无论是否签订了合约、存在侵权行为还是在其他情况下，本软件作者或版权持有人不对由本软件直接或间接产生的或由使用本软件或处置本软件所产生的任何索赔、损坏或者其他责任负责。

'''
import sys
import json

#  改变python的默认递归深度
sys.setrecursionlimit(10000)

'''
成语数据库
来自：https://github.com/pwxcoo/chinese-xinhua
''
dict = []a

# 输出
buffer = []

def recus(head_chr, count):
  '''
    计算成语接龙的递归函数
    
      head_chr : 成语首汉字
      count : 接龙的成语数量
  '''
  if count == 0:
    return True
  for _w in dict:
    if _w[0] == head_chr and not _w in buffer:
      buffer.append(_w)
      if recus(_w[-1], count - 1):
        return True
  buffer.pop()
  return False    

usage = '''
  usage:
    solitaire.py <成语> <数量>
'''
if __name__ == '__main__':
   if len(sys.argv) != 3:
     print(usage)
     exit(1)

   f = open('idiom.json')
   dict = json.load(f)
   f.close()

   head_chr = sys.argv[1][-1]
   count = int(sys.argv[2])
   if not recus(head_chr, count):
     print('** 找不到')
     exit(1)
   print(sys.argv[1], ' ')
   for w in buffer:
     print(w, end=' ')
   print('\n')
