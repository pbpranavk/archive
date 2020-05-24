var btnList = []

$('document').ready(function(){
btnList = document.getElementsByClassName('btn')
console.log(btnList )
for (var i = 0; i < btnList.length; i++) {
    console.log("Inside for......")
    btnList[i].addEventListener("click", function() {
    console.log("Triggered......")
    var current = document.getElementsByClassName("active");
    if (current.length > 0) {
      current[0].className = current[0].className.replace(" active", "");
    }
    this.className += " active";
    });
  }
});