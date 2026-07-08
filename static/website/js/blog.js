
const topics={

affairs:{
title:"📰 चालू घडामोडी",
short:"राष्ट्रीय, आंतरराष्ट्रीय, क्रीडा, अर्थव्यवस्था आणि महाराष्ट्रातील महत्त्वाच्या चालू घडामोडी.",
full:"चालू घडामोडी हा स्पर्धा परीक्षेतील सर्वात महत्त्वाचा भाग आहे. दररोज वर्तमानपत्र, सरकारी योजना, क्रीडा स्पर्धा, पुरस्कार, विज्ञान आणि तंत्रज्ञान यांचा अभ्यास करणे आवश्यक आहे."
},

tips:{
title:"📖 अभ्यास टिप्स",
short:"अभ्यासाचे योग्य नियोजन आणि वेळेचे व्यवस्थापन.",
full:"दररोज ठराविक वेळ अभ्यासासाठी द्या. मागील प्रश्नपत्रिका सोडवा. नोट्स तयार करा आणि आठवड्याला एक Mock Test द्या."
},

strategy:{
title:"🎯 यशस्वी रणनीती",
short:"Police Bharti, MPSC, Talathi परीक्षांसाठी मार्गदर्शन.",
full:"सिलेबस पूर्ण समजून घ्या. कमकुवत विषयांवर अधिक लक्ष द्या. वेळ व्यवस्थापन आणि नियमित सराव हे यशाचे मुख्य सूत्र आहे."
},

calendar:{
title:"📅 परीक्षा दिनदर्शिका",
short:"महत्त्वाच्या परीक्षा आणि अर्जाच्या तारखा.",
full:"Police Bharti, MPSC, Talathi, ZP Bharti आणि इतर स्पर्धा परीक्षांच्या अर्ज, प्रवेशपत्र आणि निकालाच्या तारखा येथे उपलब्ध असतात."
}

};

function showTopic(type,btn){

document
.querySelectorAll('.knowledgeMenu')
.forEach(item =>
item.classList.remove('active'));

btn.classList.add('active');

document.getElementById("knowledgeRight")
.innerHTML=`

<span>Latest Updates</span>

<h2>${topics[type].title}</h2>

<p>${topics[type].short}</p>

<button onclick="openPopup('${type}')">
अधिक वाचा
</button>

`;

}

function openPopup(type){

document.getElementById("infoPopup")
.style.display="flex";

document.getElementById("popupData")
.innerHTML=`

<h3>${topics[type].title}</h3>

<p>${topics[type].full}</p>

`;

}

function closePopup(){

document.getElementById("infoPopup")
.style.display="none";

}

window.onclick=function(e){

const modal=
document.getElementById("infoPopup");

if(e.target===modal){

modal.style.display="none";

}

}
