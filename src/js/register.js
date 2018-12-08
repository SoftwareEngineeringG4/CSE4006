   function validate() {
       var re = /^[a-zA-Z0-9]{4,8}$/ // 아이디와 패스워드가 적합한지 검사할 정규식
       var re2 = /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/i;
       // 이메일이 적합한지 검사할 정규식
       alert("HiHi");
       var id = document.getElementById("id");
       var name = document.getElementById("name");
       var pw = document.getElementById("password");
       var checkpw = document.getElementById("passwordCheck");
       var email = document.getElementById("email");
       var num2 = document.getElementById("id_number");
       var agree = document.getElementById("agree");
       

       var arrNum1 = new Array(); // 주민번호 앞자리숫자 6개를 담을 배열
       var arrNum2 = new Array(); // 주민번호 뒷자리숫자 7개를 담을 배열

       // ------------ 이메일 까지 -----------

       if(!check(re,id,"아이디는 4~8자의 영문 대소문자와 숫자로만 입력")) {
           return false;
       }

       if(!check(re,pw,"패스워드는 4~8자의 영문 대소문자와 숫자로만 입력")) {
           return false;
       }

       if(join.pw.value != join.checkpw.value) {
           alert("비밀번호가 다릅니다. 다시 확인해 주세요.");
           join.checkpw.value = "";
           join.checkpw.focus();
           return false;
       }
           // -------------- 주민번호 -------------

        for (var i=0; i<6; i++) {
            arrNum1[i] = num2.value.charAt(i);
        } // 주민번호 앞자리를 배열에 순서대로 담는다.
 
        for (var i=6; i<13; i++) {
            arrNum2[i] = num2.value.charAt(i);
        } // 주민번호 뒷자리를 배열에 순서대로 담는다.
 
        var tempSum=0;
 
        for (var i=0; i<6; i++) {
            tempSum += arrNum1[i] * (2+i);
        } // 주민번호 검사방법을 적용하여 앞 번호를 모두 계산하여 더함
 
        for (var i=0; i<12; i++) {
            if(i>=2) {
                tempSum += arrNum2[i] * i;
            }
            else {
                tempSum += arrNum2[i] * (8+i);
            }
        } // 같은방식으로 앞 번호 계산한것의 합에 뒷번호 계산한것을 모두 더함
 
        if((11-(tempSum%11))%10!=arrNum2[6]) {
            alert("올바른 주민번호가 아닙니다.");
            num1.value = "";
            num2.value = "";
            num1.focus();
            return false;
        }

       if(email.value=="") {
           alert("이메일을 입력해 주세요");
           email.focus();
           return false;
       }

       if(!check(re2, email, "적합하지 않은 이메일 형식입니다.")) {
           return false;
       }

       if(name.value=="") {
           alert("이름을 입력해 주세요");
           name.focus();
           return false;
       }
       
    
    alert("회원가입이 완료되었습니다.");
}

function check(re, what, message) {
    if(re.test(what.value)) {
        return true;
    }
    alert(message);
    what.value = "";
    what.focus();
    //return false;
}