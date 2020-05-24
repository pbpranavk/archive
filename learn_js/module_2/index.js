var clock = function startTime(){
    let dt = new Date();
    let h = dt.getHours();
    let m = dt.getMinutes();
    let s = dt.getSeconds();
    checkTime = s => (s < 10)? "0"+s : s;
    m = checkTime(m);
    s = checkTime(s);
    var concatTime = function() {
        return h+" : "+m+" : "+s;
    }

    return concatTime;
}

function getTime(){
    let myClock = clock();
    document.getElementById("txt").innerHTML = `The current time is : ${myClock()}`;
    setTimeout(getTime,500)
}