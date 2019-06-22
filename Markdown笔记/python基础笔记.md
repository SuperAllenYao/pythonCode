# 基础知识

##### 1. 函数

> 函数(参数)，参数可以有多个
>
> ```python
> print() # \n可以换行输出
> ```
>
> ###### 1. 函数技巧
>
> ```python
> #!/usr/bin/env python3
> # -*- coding: utf-8 -*-
> 
> # 函数的使用技巧
> # 1. 为形参数设置默认参数的时候，只需要在形参后加=和默认值即可
> def exchage(amt, scoure="CNY", tagert="USD"):
>     if scoure == "CNY" and tagert == "USD":
>         result = amt / 6.75
>         return result
>     elif scoure == "CNY" and tagert == "EUR":
>         result = amt / 7.7512
>         return result
>     else:
>         none = '无对应货币'
>         return none
> 
> # 2.以形参数形式传参(关键字传参)
> def heath_check(name, age, height, weight, hr, hbp, lbp, glu):
>     print('您的健康状况良好')
> heath_check(name='Allen', age=26, height=170,
>             weight=140, hr=100, hbp=90, lbp=100, glu=20)
> 
> # 3. 要求使用关键字传参加*，*号后面的参数必须用关键字来传参(混合传参)
> def heath_check1(name, age, *, height, weight, hr, hbp, lbp, glu):
>     print('您的健康状况良好')
> ```
>
> 

##### 2. 字符串常用方法

![image-20190417224231583](../截图/image-20190417224231583.png)

> 1. ###### 格式化字符串— 使用 format( ) 函数
>
> ```python
> # 中括号为占位符，后面的参数会放进占位符里面，也可以按索引放位置
> "{} {} you".format("I", "love")					#将产生"I love you"字符串
> "{2}.{1}.{0}".format("com", "imooc", "www")		#将产生"www.imooc.com"	
> "{p1}, {p2}, {p3}, 一起好".format(p1='你好'， p2='我好', p3='大家好') #可以赋予参数别名
> #================================ 分割线 ===================================
> # 实例
> name = "伟伦"
> age = 25
> heghit = 170
> str1 = "我叫{}，我今年{}岁了，我的身高是{}厘米".format(name, age, heghit)
> print(str1) #结果为：我叫伟伦，我今年25岁了，我的身高是170厘米
> ```
>
> ###### 2. 格式化数字
> ```python
> format(1234.567, '0.2f') #小数保留两位，返回的是字符串类型的数据
> format(1234.567, ',') #千分位分隔符
> # ================================
> num = 1234.567
> str4 = format(num, '0.2f')
> print(str4)
> print('========================分割线=====================')
> cur = 123456789
> str5 = format(cur, '0,.2f')
> print(str5)
> print('========================分割线=====================')
> account = 440911
> atm = 123456789
> str6 = "请您向{}账户，转账¥{:0,.2f}元".format(account, atm) #冒号是分割参数与格式的符号
> print(str6)
> ```
>
> ###### 3. 删除空白格
>
> ```python
> str1 = " 你好啊～ " 
> str2 = str1.strip() # 删除两边的空白格，将输出 你好啊～
> str2 = str1.lstrip() # 删除字符字符串左边的空白格
> str2 = str1.rstrip() # 删除右边的空白格
> ```
>
> ###### 4. 缩进与换行
>
> ```python
> print('\t你好啊～')		# 将在此缩进符的位置插入4个空格
> print('\n你好啊～')		# 将在此换行符的位置进行换行
> ```
>
> ###### 5. 字符串的查找与替换
>
> ```python
> str1 = 'Nice to meet you'
> strFind = str1.find("ee")		#将返回首次匹配的字符的索引位置
> #========================================
> #还可以指定查找位置，起始位置和结束位置
> strFind = str.find('ee', 2, 6)
> #=============================== in 关键字
> str1 = 'Nice to meet you'
> strFind = "e" in str1
> print(strFind)		# 将返回True
> #============字符串的替换
> strReplace = str1.replace('e', 'A', 2)	# replace(原始串，目标串，替换次数)，不指定替换次数的时候，会替换所有符合条件的目标字符串
> ```
>

---



