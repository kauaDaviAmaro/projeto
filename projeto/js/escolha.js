var car = document.getElementById("car");

car.addEventListener("click", function(){
    const audio = new Audio('audio/car.mp3');
    audio.play();
})