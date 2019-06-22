## Shell 命令 (bash)

#### 1. echo 方法（类似python的print）

```bash
echo 'Hello World'
```

#### 2. ls,cd,cd..

```bash
ls 				# 看当前目录的文件列表
cd fliename 	# 改变路径 cd+空格+文件或文件夹名
cd .. 			# 返回上一级文件夹 cd+空格+..(这是两个英文小点)
```

#### 3. 多条命令

```bash
# 用分号隔开
cd ..; ls
```

#### 4. pwd 和 ~ 和 ls . 和 ls ..

```bash
pwd		# 打印出当前目录的路径
cd ～	# 回到默认路径
ls .	# 当前目录下的文件列表
ls .. 	# 上一级目录的文件列表
```

#### 5. ls -l

```python
ls -l									# 可查看此目录下的文件的详细信息
ls -l /Users/superallen/downloads		# 后面加上路径，则可以查看指定路径的文件列表详情
ls -l /Users/superallen/downloads/*pdf	# 路径后加上 /*文件后缀，则可以筛选特定文件类型
```

#### 6. 创建文件 和 批量处理文件

```bash
mkdir desktop/截图/file0001			# 创建文件夹：关键字后面加上路径，最后一个为要创建的文件名
mv /Users/superallen/Desktop/截图/Xnip2018-09-12_10-33-05.png desktop	# 移动文件：路径+空格+要移动的目标路径
mv /Users/superallen/Desktop/截图/*.png desktop 						# 移动某一类文件：路径+/文件后缀+空格+要移动的目标路径
```

#### 7. 打开网页和下载网页

```bash
curl 'www.baidu.com' 或 curl -L 'www.baidu.com'		 #打开网页
curl -L -o desktop/baidu.html 'www.baidu.com'		 #下载网页到指定路径 '-o' 是下载的意思，后面紧跟存储路径和文件后缀类型+网址
```

#### 8. 打开文件

```bash
cat desktop/163.txt		# 打开此文件
less desktop/163.txt	# 打开此文件（仅一屏），键盘按‘Q’,退出
```

#### 9. touch

```bash
touch 163.txt 		# 当前目录下创建一个文件
touch 1.txt 2.txt	# 可创建多个
```

#### 10. 删除文件与文件夹（无法撤销）

```bash
rm 1.txt		# 删除文件
rm -i 1.txt		# 加一个确认操作才可以删除文件
rmdir flie001	# 删除文件夹
```

#### 11. 写文件

```bash
nano 1.txt		# 新建一个文件，并进入编写界面
```

#### 12. grep和pipe（ | ）

```bash
grep baidu 1.txt			# 在1.txt文件中搜索‘baidu’字符串，并输出所在行
grep baidu 1.txt | less 	# 将前一个命令的结果传递到下一个命令中去
```

#### 13. 命令的联合使用

```bash
curl -L 'www.163.com' | grep -c new
curl -L 'www.163.com' | grep new | wc
```

#### 14. 菜单

```bash
man rm # 可查看 rm 的用法
```

#### 15. 本地版本比较

```bash
diff 1.txt 2.txt # 进入到当前目录，输入diff命令
```

------

## Git的使用

#### 新建git仓库

```bash
git init # 首先进入到目标目录后再使用此命令，使用此命令会新建一个隐形的文件仓库
```

#### 提交文件

```bash
# 先进入此文件的目录
git add						# 先输入此命令
git commit 					# 输入此命令即可提交文件。
git commit -m "输入记录" 	  # 此操作不会再弹出记事本来
```

#### 新增跟踪文件

```bash
git add 1.txt # 此文件就会被跟踪
```

#### 其他

```bash
git log  # 查看提交的版本的特征码
git diff e80ed3ef139cb0af453fe96fd73f0b70e106671d e80ed3ef139cb0af453fe96fd73f0b70e106671d   # 将两个特征码的版本之间的差别
```

#### 回到某一文件

```bash
git reset --hard # 对工作区和缓冲区进行重置，从仓库重置回最近一个版本
```

#### 查看与新建分支

```bash
git branch 				# 查看分支
git branch test 		# 新建了一个test分支
git chechout test 		# 切换到test分支
```

#### 分支开发与合并

```bash
git merge master test	# 将test分支合并到master中ca
```

#### 解决冲突

> 打开文件，修改为最终版本，提交即可

#### 拉取文件

```bash
git pull origin master
```

#### 克隆代码

```bash
git clone https://github.com/SuperAllenYao/ItChat.git 
```

------

