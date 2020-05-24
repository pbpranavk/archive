function getData(){
    let logChain = ""
    var request = new XMLHttpRequest()
    const promise = new Promise(function(resolve,reject){
        logChain += "Promise started";
        logChain += "Promise is fetching data from the api";
        request.open("GET","http://localhost:5000/a",true)

        request.onload = function(){
            response = this.response;
            console.log(this.response);
            if(request.status >= 200 && request.status < 400) {
                resolve(response);
            }else{
                reject(response);
            }
        }

        request.send();
    });
    promise.then(successcallback,errorcallback);
}

function successcallback(resp){
    console.log(typeof resp)
    val = JSON.parse(resp)
    document.getElementById("txt").innerHTML = val['1']+" "+ val['2']+" "+val['3'];
}

function errorcallback(resp){
    document.getElementById("txt").innerHTML = "Some error occured......";
}