buttonColors = ['green', 'red','yellow','blue']
gamePattern = []
userPattern = []
win = true
level = 1

function nextSequence(){
    var randomColor = buttonColors[Math.floor(Math.random()*4)]
    gamePattern.push(randomColor)
    console.log(gamePattern)
    return gamePattern
}

function animateSequence(){
    for(let i = 0;i<gamePattern.length;i++){
        setTimeout(()=>{
        flashButton(gamePattern[i]);
        makeSound(gamePattern[i]);}, i*600)
    }
    console.log('completed animateSequence')
}

function flashButton(buttonId, fadeDuration = 50) {
    const button = $('#' + buttonId);

    // Fade out the button
    button.fadeOut(fadeDuration, function() {
        // Change background to black while invisible
        button.css('background-color', 'black');

        // Fade in
        button.fadeIn(fadeDuration, function() {
            // Restore original color (red) after fade in
            button.css('background-color', buttonId);
        });
    });
}

function makeSound(buttonId){
    apath = "./sounds/"+buttonId+'.mp3';
    var audio = new Audio(apath);
    audio.play()

}


function userSequence() {
    console.log('will take user input');
    let input = [];
    let patternLength = gamePattern.length;

    // Remove old click handlers, then add a new one
    $('.btn').off('click').on('click', function () {
        input.push(this.id);          // record clicked button's id
        console.log("Current input:", input);

        if (input.length === patternLength) {
            console.log("User sequence complete:", input);

            // Compare input with gamePattern here
            if (arraysEqual(input, gamePattern)) {
                console.log("✅ Correct sequence!");
                level++;
                setTimeout(() => {
                    nextRound();
                }, 1000);
            } else {
                $('h1').html('Game Over<br>Score level: ' + level + '<br>Press any key to restart the game')
                console.log("❌ Wrong sequence. Game Over.");
                win = false;
                gamePattern=[]
                userPattern=[]
            }
        }
    });
}

function arraysEqual(a, b) {
    return a.length === b.length && a.every((val, i) => val === b[i]);
}
function nextRound() {
    if (!win) return;

    console.log("⭐ Level " + level);
    $('h1').text('⭐ Level '+level);
    nextSequence();             // add a new random color
    animateSequence();          // show pattern
    userSequence();             // then wait for user input
}


// Start game on keypress
$(document).on('keypress', function () {

    console.log('Game started');
    win = true;
    gamePattern = [];
    level = 1;
    nextRound();
});


