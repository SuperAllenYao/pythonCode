import UIKit
import AVFoundation


//作用域--scope--在大括号里面定义的变量，出了大括号是没法使用的
class ViewController: UIViewController{

    var player:AVAudioPlayer!//创建一个播放器（类似于CD机）
    let sounds = ["note1","note2","note3","note4","note5","note6","note7"]//全局变量
    
    //页面加载时执行
    override func viewDidLoad() {
        super.viewDidLoad()
    }

    //用户按下按钮时执行
    @IBAction func notePressed(_ sender: UIButton) {

        play(tag:sender.tag)//调用函数
        
    }
    
    //创建一个发出声音的功能函数
    func play(tag: Int){
        //找到音频文件（类似于拿出一张CD光盘）-局部变量
        let url = Bundle.main.url(forResource: sounds[tag-1], withExtension: "wav")
        
        do{
            player = try AVAudioPlayer(contentsOf: url!)//在CD机里面放入CD光盘
            player.play()//按下播放按钮
        }catch{
            print(error)//放入的CD光盘可能有损坏导致CD机读不出来，我们需要用docatch来捕捉可能的错误，防止App闪退
        }
    }
    
    
    
  

}

