
const supportData = {

    inquiry: `
<div class="supportInfo">

<h3>📝 चौकशी फॉर्म</h3>

<p>
प्रवेश प्रक्रिया, कोर्स माहिती, फी स्ट्रक्चर आणि
बॅच वेळापत्रकाबद्दल चौकशी करा.
</p>

<button onclick="openInquiryForm()">
चौकशी करा
</button>

</div>
`,

    callback: `
<div class="supportInfo">

<h3>📞 Callback Request</h3>

<p>
आमची टीम तुम्हाला परत कॉल करून
संपूर्ण माहिती देईल.
</p>

<button onclick="openCallbackForm()">
कॉल बॅक मागवा
</button>

</div>
`,

    whatsapp: `
<div class="supportInfo">

<h3>💬 WhatsApp Support</h3>

<p>
तत्काळ मदतीसाठी WhatsApp वर संपर्क साधा.
</p>

<button onclick="window.open('https://wa.me/91100000000')">
WhatsApp उघडा
</button>

</div>
`,

    faq: `
<div class="supportInfo">

<h3>❓ वारंवार विचारले जाणारे प्रश्न</h3>

<div class="faqItem">
<h4>प्रवेश कधी सुरू होतात?</h4>
<p>नवीन बॅच प्रत्येक महिन्याच्या पहिल्या आठवड्यात सुरू होते.</p>
</div>

<div class="faqItem">
<h4>Demo Class उपलब्ध आहे का?</h4>
<p>होय, Demo Session पूर्णपणे मोफत उपलब्ध आहे.</p>
</div>

<div class="faqItem">
<h4>ऑनलाईन टेस्ट उपलब्ध आहेत का?</h4>
<p>होय, Daily Test आणि Mock Test उपलब्ध आहेत.</p>
</div>

</div>
`,

    contact: `
    <div class="supportInfo">
    
    <h3>📍 संपर्क माहिती</h3>
    
    <p>
    📞 +91 1000000000<br><br>
    📧 info@academy.com<br><br>
    📍 अहमदनगर, महाराष्ट्र
    </p>
    
    <button onclick="window.open('tel:+911000000000')">
    फोन करा
    </button>
    
    </div>
    `

};

function changeSupport(type, btn) {

    document
        .querySelectorAll(".supportItem")
        .forEach(item =>
            item.classList.remove("active"));

    btn.classList.add("active");

    document.getElementById("supportContent")
        .innerHTML = supportData[type];

}

function openInquiryForm() {

    document.getElementById("inquiryModal")
        .style.display = "flex";

}

function closeInquiryForm() {

    document.getElementById("inquiryModal")
        .style.display = "none";

}

function openCallbackForm() {

    document.getElementById("callbackModal")
        .style.display = "flex";

}

function closeCallbackForm() {

    document.getElementById("callbackModal")
        .style.display = "none";

}

window.onclick = function (e) {

    let inquiry =
        document.getElementById("inquiryModal");

    let callback =
        document.getElementById("callbackModal");

    if (e.target === inquiry) {
        inquiry.style.display = "none";
    }

    if (e.target === callback) {
        callback.style.display = "none";
    }

}

document.addEventListener("keydown", function (e) {

    if (e.key === "Escape") {

        closeInquiryForm();
        closeCallbackForm();

    }

});
