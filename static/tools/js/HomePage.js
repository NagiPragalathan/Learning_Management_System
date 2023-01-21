
var quote ="creativity is seeing What<br>Others see and thinking What<br>one else ever thought <br>&emsp13;<span style='margin-left: 170px;'>-Albert Einstein</span>"; 

document.getElementById("quote").innerHTML=quote;


function about(){
    window.location="ToolMenu";    
}

function change(){
    var quote1 = document.getElementById("text").value;
    var author = document.getElementById("pass").value;
    const fs = require("fs");
    fs.open("home.txt",quote1,(err,file)=>{
        if(err) throw err;
        console.log(file)
    })
}