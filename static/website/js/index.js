
const demoModal =
document.getElementById('demoModal');

const openDemoBtn =
document.getElementById('openDemoBtn');

const closeDemoBtn =
document.getElementById('closeDemoBtn');

/* OPEN */

openDemoBtn.addEventListener('click', () => {

    demoModal.classList.add('active');

});

/* CLOSE */

closeDemoBtn.addEventListener('click', () => {

    demoModal.classList.remove('active');

});

/* OUTSIDE CLICK CLOSE */

window.addEventListener('click', (e) => {

    if(e.target === demoModal){

        demoModal.classList.remove('active');
    }

});


const counters =
document.querySelectorAll('.counter');

const startCounter = () => {

    counters.forEach(counter => {

        const target =
        +counter.getAttribute('data-target');

        let count = 0;

        const increment =
        target / 120;

        const updateCounter = () => {

            count += increment;

            if(count < target){

                counter.innerText =
                Math.ceil(count) + "+";

                requestAnimationFrame(updateCounter);

            }else{

                counter.innerText =
                target + "+";
            }
        }

        updateCounter();

    });

}

/* =========================================
   INTERSECTION OBSERVER
========================================= */

const statsSection =
document.querySelector('.academy-stats');

let started = false;

const observer =
new IntersectionObserver((entries)=>{

    entries.forEach(entry=>{

        if(entry.isIntersecting && !started){

            startCounter();

            started = true;
        }

    });

},{
    threshold:0.3
});

observer.observe(statsSection);
