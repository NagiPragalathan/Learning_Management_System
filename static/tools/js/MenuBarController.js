var count = 0;
    function btn(){
       if(count>5){
           count = 0;
       }
       var a = document.querySelector(".nav_");
       var b = document.querySelector(".nav_ li")
       var c = document.querySelector(".p_nav_btn")
       if(count%2 == 0){
            a.style.width = "0px";
            a.style.marginLeft = "-300px";
            b.style.marginLeft = "-300px";
            c.style.marginLeft = "0px";
            c.style.transform = 'rotate(-360deg)';
            c.style.transition = "all 2s ease-in-out";
            count++;
       }
       else{
            a.style.width = "250px";
            a.style.marginLeft = "0px";
            b.style.marginLeft = "15px";
            c.style.marginLeft = "260px";
            c.style.transform = 'rotate(360deg)';
            c.style.transition = "all 2s ease-in-out";
            count++;
       }
    }