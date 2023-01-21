var count = 0;

function rorait(){
    doc_C = document.querySelector(".menu_c");
    doc_l1 = document.querySelector(".l1");
    doc_l2 = document.querySelector(".l2");
    doc_l3 = document.querySelector(".l3");
    console.log(count)
    if(count%2 == 1){
        doc_l1.style.left = "-109px";
        doc_l1.style.top = "22px";
        doc_l2.style.left = "-73px";
        doc_l2.style.top = "-54px";
        doc_l3.style.top = "-109px";
        doc_l3.style.left = "-6px";
        doc_l1.style.transform = 'rotate(-360deg)';
        doc_l2.style.transform = 'rotate(-360deg)';
        doc_l3.style.transform = 'rotate(-360deg)';
        doc_C.style.transform = 'rotate(360deg)';
    }else{
        doc_l1.style.left = "0px";
        doc_l1.style.top = "0px";
        doc_l2.style.left = "0px";
        doc_l2.style.top = "0px";
        doc_l3.style.top = "0px";
        doc_l3.style.left = "0px";
        doc_l1.style.transform = 'rotate(360deg)';
        doc_l2.style.transform = 'rotate(360deg)';
        doc_l3.style.transform = 'rotate(360deg)';
        doc_C.style.transform = 'rotate(-360deg)';
    }

    if(count>5){
        count = 0;
    }
    count++;
}

function choose_file(x) {
    // fetch("/python-api", {
    //     method: "POST",
    //     body: JSON.stringify({ ip: x }),
    //   }).then((_res) => _res.json())
    //   .then(_data => {
    //       window.location.href = "render/"+_data.path.ip
    //   });
    window.location.href = "render/"+x
}