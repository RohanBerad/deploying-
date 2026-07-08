function toggleStory(card){

    document.querySelectorAll('.student-card')
    .forEach(item => {
        if(item !== card){
            item.classList.remove('active');
        }
    });

    card.classList.toggle('active');
}


function openResult(btn){

    const card = btn.closest(".resultItem");

    document.querySelectorAll(".resultItem")
    .forEach(item=>{
        if(item !== card){
            item.classList.remove("active");
        }
    });

    card.classList.toggle("active");
}