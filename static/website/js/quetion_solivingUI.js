fetch('/static/website/js/question.json')
.then(response => response.json())
.then(data => {

    questions = data;

   
    document.getElementById("totalQuestions").innerText =
    questions.length;

createPalette();
loadQuestion();

});
let questions =[];
let currentQuestion = 0;
let answers = {};
let reviewQuestions = {};



function loadQuestion() {

    let q = questions[currentQuestion];

    document.getElementById("questionNumber").innerText =
        `Question ${currentQuestion + 1} of ${questions.length}`;

    document.getElementById("questionText").innerText =
        q.question;

    let html = "";

    q.options.forEach((option, index) => {

        html += `
<div class="option ${answers[currentQuestion] === index ? 'selected' : ''}"
onclick="selectOption(${index})">

<div class="d-flex align-items-center">

<input
type="radio"
class="form-check-input me-3"
${answers[currentQuestion] === index ? 'checked' : ''}
>

<span>${option}</span>

</div>

</div>
`;

    });

    document.getElementById("options").innerHTML = html;

    updatePalette();
    updateSummary();

}

function selectOption(index) {

    answers[currentQuestion] = index;

    loadQuestion();

}

function nextQuestion() {

    if (currentQuestion < questions.length - 1) {

        currentQuestion++;
        loadQuestion();

    }

}

function previousQuestion() {

    if (currentQuestion > 0) {

        currentQuestion--;
        loadQuestion();

    }

}

function jumpQuestion(index) {

    currentQuestion = index;
    loadQuestion();

}

function createPalette() {

    let html = "";

    questions.forEach((q, index) => {

        html += `
<button
class="btn btn-outline-primary palette-btn"
onclick="jumpQuestion(${index})">

${index + 1}

</button>
`;

    });

    document.getElementById("questionPalette").innerHTML =
        html;

}

function updatePalette() {

    const buttons =
        document.querySelectorAll(".palette-btn");

    buttons.forEach((btn, index) => {

        btn.classList.remove(
            "current",
            "answered",
            "review"
        );

        if (answers[index] !== undefined) {
            btn.classList.add("answered");
        }

        if (reviewQuestions[index]) {
            btn.classList.add("review");
        }

        if (index === currentQuestion) {
            btn.classList.add("current");
        }

    });

}

function markForReview() {

    reviewQuestions[currentQuestion] = true;

    updatePalette();

    if (currentQuestion < questions.length - 1) {

        currentQuestion++;
        loadQuestion();

    }

}

function updateSummary() {

    let attempted =
        Object.keys(answers).length;

    document.getElementById("attemptedCount")
        .innerText = attempted;

    document.getElementById("remainingCount")
        .innerText =
        questions.length - attempted;

}

function submitTest() {

    let correct = 0;
    let wrong = 0;
    let attempted = Object.keys(answers).length;
    let total = questions.length;

    questions.forEach((q, index) => {

        if (answers[index] !== undefined) {

            if (answers[index] === q.answer) {
                correct++;
            } else {
                wrong++;
            }

        }

    });
let skipped = questions.filter((q, i) => answers[i] === undefined).length;

    let percentage = (correct / total) * 100;

    let score = correct; // or marks system

    // 🔥 SAVE TO LOCALSTORAGE
    let resultData = {
        correct,
        wrong,
        skipped,
        attempted,
        total,
        percentage,
        score
    };

    localStorage.setItem("testResult", JSON.stringify(resultData));

    // redirect
    window.location.href = "/Test_result/"; // your result page
}

let time = 1800;

let timerInterval = setInterval(() => {

    let minutes =
        Math.floor(time / 60);

    let seconds =
        time % 60;

    document.getElementById("timer").innerText =
        `${minutes}:${seconds
            .toString()
            .padStart(2, '0')}`;

    time--;

  if (time < 0) {
    clearInterval(timerInterval);
    submitTest();
}

}, 1000);