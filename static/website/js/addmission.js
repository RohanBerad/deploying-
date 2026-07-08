
function showAdmissionInfo() {

    document
        .getElementById("admissionPopup")
        .style.display = "flex";

}

function closeAdmissionInfo() {

    document
        .getElementById("admissionPopup")
        .style.display = "none";

}

window.onclick = function (e) {

    const popup =
        document.getElementById("admissionPopup");

    if (e.target === popup) {

        popup.style.display = "none";

    }

}

document
    .getElementById("admissionForm")
    .addEventListener("submit", function (e) {

        e.preventDefault();

        alert(
            "🎉 तुमचा प्रवेश अर्ज यशस्वीरित्या सबमिट झाला आहे."
        );

        this.reset();

    });
