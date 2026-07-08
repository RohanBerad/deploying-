function toggleUpdate(element){

    let body = element.nextElementSibling;
    let plus = element.querySelector(".plus");

    body.classList.toggle("show");

    if(body.classList.contains("show")){
        plus.innerHTML = "−";
    }else{
        plus.innerHTML = "+";
    }
}


function toggleFeature(card){

    document.querySelectorAll('.feature-card')
    .forEach(item => {
        if(item !== card){
            item.classList.remove('active');
        }
    });

    card.classList.toggle('active');
}