import UIKit

func sellPhone(_ iPhone: Int){
    for time in (1...iPhone).reversed() { //循环变量的次数
        print("现在还有\(time)部iPhone，卖出一部，还有\(time-1)部")
    }
    print("全部卖完啦")
}

sellPhone(20)


