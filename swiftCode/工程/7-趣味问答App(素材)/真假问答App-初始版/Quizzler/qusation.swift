//
//  qusation.swift
//  Quizzler
//
//  Created by 尧伟伦 on 4/6/19.
//  Copyright © 2019 rongcosme. All rights reserved.
//

import Foundation

class Question{
    var anwer: Bool
    var questText: String

    init(text: String, correctAnswer: Bool) {
        anwer = correctAnswer
        questText = text
    }

}
//Question(text: Allen, correctAnser: true)
//初始化也就叫实例化，从class到Object的过程
class hum{
    let name: String
    let sex: String
    
    init(myName: String, mySex: String) {
        name = myName
        sex = mySex
    }
    
}

let Allen = hum(myName: "Allen", mySex: "男")
