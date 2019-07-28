import UIKit

func love(hisName:String,herName:String)->String{
    let num = Int.random(in: 0...100)
    if num > 80{
        return "你们的匹配度为：\(num)%，你们很配，早生贵子"
    }else if num > 40 && num <= 80{
        return "你们的匹配度为：\(num)%，你们之间还可以"
    }else{
        return "你们的匹配度为：\(num)%，你们不合适"
    }
//    return num
}
print(love(hisName: "allen", herName: "shiqian"))

