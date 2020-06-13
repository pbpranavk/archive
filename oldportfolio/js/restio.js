

  function regdb() {
          var fname = (document.getElementById ('a')).value;
          var email = (document.getElementById ('b')).value;
          var message = (document.getElementById ('c')).value;
          var db = new restdb("593f8c814b84c62d01db8b3e ");
          var p = new db.contact({"name": fname,"email": email,"message": message});
          p.save();
          alert('Thank you!!! We shall get back to you soon.');
          //alert(fname);
          //alert(email);
          //alert(message);
        }
     
