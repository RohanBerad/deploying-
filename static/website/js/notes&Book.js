
const data = {

"Study Material":{
title:"📚 Study Material",
text:"पोलीस भरती, MPSC, तलाठी व सरळसेवा परीक्षांसाठी विषयनिहाय अभ्यास साहित्य उपलब्ध आहे."
},

"Notes Download":{
title:"📝 Notes Download",
text:"सर्व महत्वाच्या नोट्स PDF स्वरूपात डाउनलोड करण्यासाठी उपलब्ध आहेत."
},

"PDF Section":{
title:"📄 PDF Section",
text:"विविध विषयांचे PDF नोट्स, प्रश्नसंच आणि चालू घडामोडी उपलब्ध आहेत."
},

"Books":{
title:"📖 Books",
text:"शिफारस केलेली पुस्तके व अभ्यासासाठी उपयुक्त संदर्भ साहित्य उपलब्ध आहे."
},

"Previous Papers":{
title:"📑 Previous Papers",
text:"मागील वर्षांच्या प्रश्नपत्रिका व उत्तरपत्रिका डाउनलोड करा."
}

};

function openMaterial(el){

document.querySelectorAll(".menuItem")
.forEach(item=>item.classList.remove("active"));

el.classList.add("active");

const key = el.innerText.trim();

document.querySelector(".materialContent h3").innerHTML =
data[key].title;

document.querySelector(".materialContent p").innerHTML =
data[key].text;

}