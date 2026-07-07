// =====================================
// AI Virtual Classroom JavaScript
// =====================================


// Page Load Message
window.onload = function () {

    console.log(
        "AI Virtual Classroom Loaded Successfully"
    );

};



// Confirm Actions
function confirmAction(message) {

    let result = confirm(message);

    return result;

}



// Student Registration Validation
function validateForm() {

    let name =
        document.getElementById("name");

    let usn =
        document.getElementById("usn");


    if(name && name.value.trim() === "") {

        alert("Please enter student name");

        return false;

    }


    if(usn && usn.value.trim() === "") {

        alert("Please enter USN");

        return false;

    }


    return true;

}



// Show Notification

function showNotification(message){

    alert(message);

}



// Quiz Timer

let quizTime = 300;


function startQuizTimer(){

    let timer =
        setInterval(function(){


            quizTime--;


            console.log(
                "Time Remaining: "
                + quizTime
                + " seconds"
            );


            if(quizTime <= 0){

                clearInterval(timer);

                alert(
                    "Quiz Time Completed!"
                );

            }


        },1000);

}




// Dashboard Card Animation

function animateCards(){

    let cards =
        document.querySelectorAll(".card");


    cards.forEach(function(card){


        card.addEventListener(
            "mouseover",
            function(){

                card.style.transform =
                "scale(1.03)";

            });


        card.addEventListener(
            "mouseout",
            function(){

                card.style.transform =
                "scale(1)";

            });


    });

}



document.addEventListener(
    "DOMContentLoaded",
    animateCards
);
