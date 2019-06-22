# swift学习笔记

---

[TOC]

---

### 1. 变量的声明

```swift
var x = 0  
```

---

### 2. 常量的声明

```swift
let x = 0
```

---

### 3. 数组的声明

```swift
let x = ["1","2","3"]   //
```

---

### 4. 函数的声明

```swift
func name (){
    //代码块
}
```

#### 4.1 函数的调用

```swift
name()//直接输入方法名
```

#### 4.2 函数-参数和返回值

> 参数设置：     变量名：数据类型
>
> 返回值：	->数据类型

```swift
func getMilk(num: Int,total: Int)->Int{
        print("去商店")
        print("买\(num)箱牛奶")
    let price: Int = 10 * num
        print("给\(price)块钱")
        print("回家")
        return total-price
}
//调用时的是实际参数
let res = getMilk(num: 1,total: 100)
print("还剩\(res)块钱")
```

---

