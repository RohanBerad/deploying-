
const testData = {

    daily: {
        title: "📝 Daily Test",
        text: "दररोज नवीन प्रश्नसंच उपलब्ध. विद्यार्थ्यांनी नियमित सराव करून तयारी मजबूत करावी.",
        link: "/quetion_solvingUI/"
    },

    weekly: {
        title: "📅 Weekly Test",
        text: "आठवडाभराच्या अभ्यासाचे मूल्यांकन करणारी विशेष टेस्ट.",
        link: "/quetion_solvingUI/"
    },

    mock: {
        title: "🎯 Mock Test",
        text: "खऱ्या परीक्षेप्रमाणे अनुभव देणारी पूर्ण Mock Test.",
        link: "/quetion_solvingUI/"
    },

    analysis: {
        title: "📊 Result Analysis",
        text: "तुमचे गुण, चुका आणि सुधारणा करण्याच्या संधींचे विश्लेषण.",
        link: "/Test_result/"
    },

    leaderboard: {
        title: "🏆 Leaderboard",
        text: "राज्यभरातील विद्यार्थ्यांमध्ये तुमची रँक आणि स्थान पाहा.",
        link: "/#/"
    }

};

function showTest(type, btn) {
    console.log(type);

    document
        .querySelectorAll(".tabBtn")
        .forEach(tab => tab.classList.remove("active"));

    btn.classList.add("active");

    const currentTest = testData[type];

    document.getElementById("testInfo").innerHTML = `
        <h3>${currentTest.title}</h3>
        <p>${currentTest.text}</p>
        <a href="${currentTest.link}">
            सुरू करा
        </a>
    `;
}
console.log(showTest)
