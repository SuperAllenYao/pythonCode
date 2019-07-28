import UIKit
import AVFoundation

class ViewController: UIViewController {
    
    var player:AVAudioPlayer!
    let sounds = ["note1","note2","note3","note4","note5","note6","note7"]
    override func viewDidLoad() {
        super.viewDidLoad()
    }


    
    
    @IBAction func notePressed(_ sender: UIButton) {
        music(tag: sender.tag)
    }

    // 发出声音的函数
    func music(tag: Int){
        let url = Bundle.main.url(forResource: sounds[tag-1], withExtension: "wav")
        
        do {
            player = try AVAudioPlayer(contentsOf: url!)
            player.play()
        }catch {
            print(error)
        }
        
        
        
        
//        print(sender.tag)
//        if sender.tag == 1{
//            //用户按的是第一个按钮
//        }else if sender.tag == 2{
//            //用户按的是第二个按钮
//        }
//
        
    }
    
  

}

