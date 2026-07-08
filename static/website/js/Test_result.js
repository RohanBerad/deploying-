window.onload = function () {

    let data = JSON.parse(localStorage.getItem("testResult"));

    if (!data) return;

    document.getElementById("correct").innerText = data.correct;
    document.getElementById("wrong").innerText = data.wrong;
    document.getElementById("skipped").innerText = data.skipped;

    document.getElementById("score").innerText = data.score;

    document.getElementById("percentage").innerText =
        data.percentage.toFixed(2) + "%";

    let progress = document.getElementById("progressBar");
    progress.style.width = data.percentage + "%";
    progress.innerText = data.percentage.toFixed(2) + "%";

    // ✅ clear AFTER rendering
    localStorage.removeItem("testResult");
};