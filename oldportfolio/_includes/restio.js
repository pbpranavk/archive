
  function regdb() {
	
          var fname = (document.getElementById ('name')).value;

          var email = (document.getElementById ('email')).value;
          var state = (document.getElementById ('message')).value;
          var db = new restdb("593f8c814b84c62d01db8b3e ");
         
          var p = new db.contact({"name":name,"email":email,"message":message});
          p.save();
          alert('Thank you!!! We shall get back to you soon.');
        }

