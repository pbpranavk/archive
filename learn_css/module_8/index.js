function myFunction(){
    var x = document.getElementById("myNavBar");
    if(x.className === "navbar"){
       //alert("1");
        x.className += " responsive";
    }else{
       //alert("2");
        x.className = "navbar";
    }
}