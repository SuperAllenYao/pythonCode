import UIKit
func computeBMI(weight:Double,hight:Double)->String{
    let BMI = round(weight/(pow(hight, 2)))
    var messges = ""
    if BMI > 27{
        messges = "有点胖喔，注意身材。"
    }else if BMI < 27 && BMI > 24{
        messges = "标准身材，继续保持啊。"
    }else{
        messges = "有点瘦了，要补充营养啊。"
    }
    return "您的BMI为：\(BMI)，\(messges)"
}
print(computeBMI(weight: 71.5, hight: 1.70))
