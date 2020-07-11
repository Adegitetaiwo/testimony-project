let newDate = new Date();
let hrs = newDate.getHours();

var greeting;

if (hrs < 12){
    greeting = `Good Morning! <i class="icon-brightness_low" style="color:rgb(255, 243, 70);"></i>`; 
} else if (hrs >= 12 && hrs <=16 ){
    greeting = `Good Afternoon! <i class="icon-wb_sunny" style="color:rgb(255, 243, 70);"></i>`
} else if (hrs >= 16 && hrs <= 24){
    greeting = `Good Evening! <i class="icon-brightness_3" style="color:rgb(255, 243, 70);"></i>`
}

document.getElementById('greet').innerHTML = greeting;