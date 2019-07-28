//
//  Question.swift
//  Quizzler
//
//  Created by liujun on 2018/11/10.
//  Copyright © 2018 rongcosme. All rights reserved.
//

import Foundation

class Question{
    
    let answer: Bool
    let questionText: String
    
    init(text:String,correctAnswer:Bool) {
        questionText = text
        answer = correctAnswer
    }
    
}
//初始化--实例化。从class-->object的过程
//Question(text: "马云是中国首富吗", correctAnswer: true)



class People{
    let name: String
    let gender: String
    
    init(detailName:String,detailGender:String) {
        name = detailName
        gender = detailGender
    }
    
    
}

let zhangsan = People(detailName: "张三", detailGender: "男")


class User{
    let name:String
    let avatar:String
    let follows = 0
    let followed = 0
    
    init(userName:String,userAvatar:String) {
        name = userName
        avatar = userAvatar
    }
}

let wangsicong = User(userName: "王思聪", userAvatar: "http://weibo.com/dajhshfgjwhe.jpg")
