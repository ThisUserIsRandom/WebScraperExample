function enterText(sauce){
    j = Number(sessionStorage.getItem("index"));
    fetch('/fetch/'+sauce,{mode:'no-cors'})
    .then(blob => blob.text())
    .then(data => {
        //  ${JSON.parse(data)[i]}
        // above statement is address of images returned at ith address ,for this cause
        // lets derieve i from sessionStorage
        document.getElementById('imgDiv').innerHTML = `<img src="${JSON.parse(data)[j]}" style="align-self:center;margin-left:37%;width:25%;height:98%;" alt="End of comic">`
    })
    .catch(e => {
    console.log(e);
    return e;
    });

}

function NextImage(sauce){
    if(Number(sessionStorage.getItem("index"))>1){
        sessionStorage.setItem("index",Number(sessionStorage.getItem("index"))+1);
        enterText(sauce)
    }
}

function PrevImage(sauce){
    if(Number(sessionStorage.getItem("index"))>1){
        sessionStorage.setItem("index",Number(sessionStorage.getItem("index"))-1);
        enterText(sauce)
        }
}
