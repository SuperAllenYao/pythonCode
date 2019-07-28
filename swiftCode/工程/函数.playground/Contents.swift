////买牛奶功能
//func getMilk(){
//    print("去商店")
//    print("买两箱牛奶")
//    print("给钱")
//    print("回家")
//}
////调用买牛奶功能
//getMilk()

//定义方法时的是形式参数
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
