
    window.addEventListener("scroll",function(){
        var nav = document.querySelector("nav");
        var body = document.querySelector("#nav-bottom");
        
        if (window.scrollY > 380){
          // nav.classList.remove("navbar-dark");
          nav.classList.add("fixed-top","shadow");
          body.style.padding = "46px";
        }else {
          // nav.classList.add("navbar-dark");
          nav.classList.remove("fixed-top","shadow");
          body.style.padding = "0px";
        }
    });  
    document.getElementById(`{% block navID %}{% endblock navID %}`).classList.add("nav-active") 



        
            var i = 0;
            function read(id){
                
              console.log(id)  
              if(!i){
                    document.getElementById(`more-${id}`).style.display="inline";
                    document.getElementById(`dots-${id}`).style.display="none";
                    document.getElementById(`less-${id}`).style.display="none";
                    document.getElementById(`read-${id}`).innerHTML="read less";
                    i=1;
                }
                else{
                    document.getElementById(`more-${id}`).style.display="none";
                    document.getElementById(`dots-${id}`).style.display="inline";
                    document.getElementById(`less-${id}`).style.display="inline";
                    document.getElementById(`read-${id}`).innerHTML="read more";
                    i=0;
                }
            }
