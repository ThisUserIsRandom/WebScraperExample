function enterText(sauce){
    j = Number(sessionStorage.getItem("images"));
    k=j;
    if(j>1){
        document.getElementById('butt')
    }
    fetch('/fetch/'+sauce,{mode:'no-cors'})
    .then(blob => blob.text())
    .then(data => {
        for(let i=j;i<j+15;i+=1){
            sessionStorage.setItem("images",i+1);
            console.log(i);
            document.getElementById('uniqueDiv').innerHTML += `
            <a href='/ecchi/g/${sauce}/${i}'><img style="width:90%;height:50%px;" class = "imagS" loading="lazy"  src="${JSON.parse(data)[i]}" alt=""></a>`;
        }
    })
    .catch(e => {
    console.log(e);
    return e;
    });

}
{/*  */}
