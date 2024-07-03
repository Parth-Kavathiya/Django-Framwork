// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();


//  owl carousel script
$(".owl-carousel").owlCarousel({
    loop: true,
    margin: 20,
    nav: true,
    navText: [],
    autoplay: true,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 1
        },
        1000: {
            items: 2
        }
    }
});

//    end owl carousel script 



/** google_map js **/
function myMap() {
    var mapProp = {
        center: new google.maps.LatLng(40.712775, -74.005973),
        zoom: 18,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}

// side-bar 
const login = document.querySelector(".navbar-nav .nav-item .login");
const sideBar = document.querySelector(".side-container .side-bar");
const close = document.querySelector(".side-container .side-bar #close");

login.addEventListener("click", () => {
    sideBar.classList.add("active");
})

close.addEventListener("click", () => {
    sideBar.classList.remove("active")
})

const otpButton = document.querySelector(".otp-button");
const otpGet = document.querySelector(".otp-get");

otpButton.addEventListener("click", () => {
    otpButton.classList.add("hide");
    otpGet.classList.remove("show");
})
