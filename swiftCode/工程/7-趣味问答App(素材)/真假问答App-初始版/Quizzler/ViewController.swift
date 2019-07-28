import UIKit

class ViewController: UIViewController {
    
    
    let question = [
        Question(text: "马云是中国首富", correctAnswer: true),
        Question(text: "刘强东最早是在中关村卖光盘的", correctAnswer: true),
        Question(text: "苹果公司是目前世界上最牛的科技公司", correctAnswer: true),
        Question(text: "只要坚持下去就能学好代码吗", correctAnswer: true),
        Question(text: "王思聪是80后", correctAnswer: true),
        Question(text: "在国内可以正常访问google.com吗", correctAnswer: false),
        Question(text: "敲完1万行代码之后可以成为编程高手吗", correctAnswer: true),
        Question(text: "撒贝宁说过清华还行吗", correctAnswer: false),
        Question(text: "一直听复昕学堂lebus的课可以变成大牛吗", correctAnswer: true),
        Question(text: "网上说苹果不好用安卓好用的人大多数都是水军吗", correctAnswer: true),
        Question(text: "豆瓣网是一个和你分享刚编的故事的网站吗", correctAnswer: false),
        Question(text: "优酷比B站牛", correctAnswer: false),
        Question(text: "我帅吗？", correctAnswer: true)
    ]
    
    @IBOutlet weak var questionLabel: UILabel!
    @IBOutlet weak var scoreLabel: UILabel!
    @IBOutlet var progressBar: UIView!
    @IBOutlet weak var progressLabel: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        questionLabel.text = question[0].questText
    }


    @IBAction func answerPressed(_ sender: UIButton) {
        if sender.tag == 1{
            if question[0].anwer == true{
                print("回答正确")
            }else{
                print("回答错误")
            }
        }else{
            if question[0].anwer == true{
                print("回答错误")
            }else{
                print("回答正确")
            }
        }
        question[1].questText
    }
    
    
    func updateUI() {
      
    }
    

    func nextQuestion() {
        
    }
    
    
    func checkAnswer() {
        
    }
    
    
    func startOver() {
       
    }
    

    
}
