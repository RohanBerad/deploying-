
const tabs =
document.querySelectorAll('.course-tab');

const contents =
document.querySelectorAll('.course-content');

const closeBtns =
document.querySelectorAll('.close-content');

/* TAB CLICK */

tabs.forEach(tab => {

    tab.addEventListener('click', () => {

        const target =
        tab.getAttribute('data-target');

        /* REMOVE ACTIVE */

        tabs.forEach(btn => {

            btn.classList.remove('active');

        });

        contents.forEach(content => {

            content.classList.remove('active');

        });

        /* ADD ACTIVE */

        tab.classList.add('active');

        document
        .getElementById(target)
        .classList.add('active');

    });

});

/* CLOSE BUTTON */

closeBtns.forEach(btn => {

    btn.addEventListener('click', () => {

        contents.forEach(content => {

            content.classList.remove('active');

        });

        tabs.forEach(tab => {

            tab.classList.remove('active');

        });

    });

});



const policeTabs =
document.querySelectorAll('.police-tab');

const policeContents =
document.querySelectorAll('.police-content');

policeTabs.forEach(tab => {

    tab.addEventListener('click', () => {

        const target =
        tab.getAttribute('data-police');

        /* REMOVE ACTIVE */

        policeTabs.forEach(btn => {

            btn.classList.remove('active');

        });

        policeContents.forEach(content => {

            content.classList.remove('active');

        });

        /* ADD ACTIVE */

        tab.classList.add('active');

        document
        .getElementById(target)
        .classList.add('active');

    });

});




const talathiTabs =
document.querySelectorAll('.talathi-tab');

const talathiContents =
document.querySelectorAll('.talathi-content');

talathiTabs.forEach(tab => {

    tab.addEventListener('click', () => {

        const target =
        tab.getAttribute('data-talathi');

        /* REMOVE ACTIVE */

        talathiTabs.forEach(btn => {

            btn.classList.remove('active');

        });

        talathiContents.forEach(content => {

            content.classList.remove('active');

        });

        /* ADD ACTIVE */

        tab.classList.add('active');

        document
        .getElementById(target)
        .classList.add('active');

    });

});




const careerTabs =
document.querySelectorAll('.career-tab');

const careerContents =
document.querySelectorAll('.career-content');

careerTabs.forEach(tab=>{

    tab.addEventListener('click',()=>{

        careerTabs.forEach(btn=>
            btn.classList.remove('active'));

        careerContents.forEach(content=>
            content.classList.remove('active'));

        tab.classList.add('active');

        document
        .getElementById(
            tab.dataset.target
        )
        .classList.add('active');

    });

});

/* SUB BUTTONS */

const subButtons =
document.querySelectorAll('.sub-btn');

const allInfos =
document.querySelectorAll('.career-info');

subButtons.forEach(button=>{

    button.addEventListener('click',()=>{

        const parent =
        button.closest('.career-content');

        parent.querySelectorAll('.sub-btn')
        .forEach(btn=>
            btn.classList.remove('active'));

        parent.querySelectorAll('.career-info')
        .forEach(info=>
            info.classList.remove('active'));

        button.classList.add('active');

        parent.querySelector(
            '#' + button.dataset.info
        )
        .classList.add('active');

    });

});
