function init() {
    var num=document.getElementById("num")
    num.value=0
    num.disabled="disabled"
    // var n1=document.getElementById("n1")
    // n1.onclick=function () {
    //     alert("123")
    // }
    var oButton=document.getElementsByTagName('input')
    var btn_num1
    var fh
    for (var i=0; i<oButton.length; i++){
        oButton[i].onclick=function () {
            if (is_num(this.value)){
                num.value=(num.value+this.value)*1
            }else {
                var btn_num=this.value
                switch (btn_num) {
                    case "+":
                        btn_num1=Number(num.value)
                        num.value=0
                        fh="+"
                        break
                    case "-":
                        btn_num1=Number(num.value)
                        num.value=0
                        fh="-"
                        break
                    case "X":
                        btn_num1=Number(num.value)
                        num.value=0
                        fh="X"
                        break
                    case "/":
                        btn_num1=Number(num.value)
                        num.value=0
                        fh="/"
                        break
                    case ".":
                        num.value=is_dot(num.value)
                        break
                    case "<-":
                        num.value=back(num.value)
                        break
                    case "AC":
                        num.value=0
                        break
                    case "+/-":
                        num.value=sign(num.value)
                        break
                    case "=":
                        switch (fh) {
                            case "+":
                                num.value=btn_num1+Number(num.value)
                                break
                            case "-":
                                num.value=btn_num1-Number(num.value)
                                break
                            case "X":
                                num.value=btn_num1*Number(num.value)
                                break
                            case "/":
                                if (Number(num.value)==0){
                                    num.value=0
                                    alert("除数已经为0，结果为0")
                                }else {
                                    num.value=btn_num1/Number(num.value)
                                }
                                break
                        }
                        break
                }
            }
        }
    }
}
function is_num(num) {
    return !isNaN(num);
}
// 小数点
function is_dot(n) {
    if (n.indexOf('.')==-1){
        n=n+'.'
    }
    return n
}
// 判断输入框内的数字是否为0，或为空
function isNull(n) {
    if (n=="0" || n.length==0){
        return true
    }else {
        return false
    }
}
// 退位键
function back(n) {
    n=n.substr(0,n.length-1)
    if (isNull(n)){
        n=0
    }
    return n
}
// 正负号
function sign(n) {
    // if (n.indexOf('-')==-1){
    //     n='-'+n
    // }else{
    //     n=n.substr(1,n.length)
    // }
    n=Number(n)*-1
    return n
}