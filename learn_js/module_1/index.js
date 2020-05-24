function validate(){
    var email = document.getElementById("email");
    var pwd = document.getElementById("pwd");
    email.style.border = "";
    pwd.style.border = "";
    if(!isEmpty(email) && !isEmpty(pwd)){
        if(!validateEmail(email.value)){
            alert("Email not valid");
            return;
        }
        if(!validatePwd(pwd.value)){
            alert("Password not valid");
            return;
        }
        if(checkDB(email.value, pwd.value))
            document.getElementById("content").innerHTML = "Logged in @"+getDateTime();
        else
            document.getElementById("content").innerHTML = "Wrong Password....Not logged in";
    }
}

function getDateTime() {

    var days = new Map();
    days.set(1, "Monday");
    days.set(2, "Tuesday");
    days.set(3, "Wednesday");
    days.set(4, "Thursday");
    days.set(5, "Friday");
    days.set(6, "Saturdayy");
    days.set(7, "Sunday");
    var time = new Date();
    var date = days.get(time.getDay()) + " ";
    date += time.getDate() + "/";
    date += time.getMonth() + "/";
    date += time.getFullYear();
    var hour = time.getHours();
    var minute = time.getMinutes();
    var second = time.getSeconds();
    var temp = '' + ((hour > 12) ? hour - 12 : hour);
    if (hour == 0)
      temp = '12';
    temp += ((minute < 10) ? ':0' : ':') + minute;
    temp += ((second < 10) ? ':0' : ':') + second;
    temp += (hour >= 12) ? ' P.M.' : ' A.M.';
    return date + temp;
  }

function checkDB(email, pwd){
    return email === "pbpranav24@gmail.com" && pwd === "pranav@123";
}

function validateEmail(email){
    let pattern = new RegExp("[a-z0-9A-Z]+@[a-z]\.[^\s]+$");
    let regularExpRes = pattern.test(email);
    let size = email.length;
    let sizeRes = size>6;
    return regularExpRes && sizeRes;
}

function validatePwd(pwd){
    let size = pwd.length;
    let sizeRes = size >= 8 && size <= 12;
    let specialRes = false
    for(word in "! @ # $ % ^ & * ( ) . , < > ? / ' ` ~ "){
        specialRes = specialRes || pwd.includes(word);
        if(specialRes){
            break;
        }
    }
    let numCount = (pwd.match(/\d/g) || []).length;
    let numRes = numCount >= 2;
    return sizeRes && numRes;
}

function isEmpty(par){
    if(par.value === ""){
        par.style.border = "red 2px solid";
        alert(par.id +" is empty...");
        return true;
    }
    return false;
}