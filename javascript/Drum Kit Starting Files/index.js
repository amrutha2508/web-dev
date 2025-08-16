var numofdrumbuttons = document.querySelectorAll('.drum').length;

apath = {
    'w': './sounds/tom-1.mp3',
    'a': './sounds/tom-2.mp3',
    's': './sounds/tom-3.mp3',
    'd': './sounds/tom-4.mp3',
    'j': './sounds/snare.mp3',
    'k': './sounds/kick-bass.mp3',
    'l': './sounds/crash.mp3'
}

for(let i=0; i<numofdrumbuttons; i++){
    document.querySelectorAll('.drum')[i].addEventListener("click",function (){
        makeSound(this.classList[0]);
        buttonAnimation(this.classList[0]);
        // resetButtonAnimation(this.classList[0])
    })
}

document.addEventListener('keypress',function(event){
    makeSound(event.key);
    buttonAnimation(event.key);

})

function buttonAnimation(buttonKey){
    var button = document.querySelector('.'+buttonKey);
    if (button){
        button.classList.add('pressed');
        setTimeout(function(){
            button.classList.remove('pressed');
        },100)
    }
}

function makeSound(key){
    var audio = new Audio(apath[key]);
    audio.play();
}
// function Instrument(name, pathToAudioFile, pathToImageFile){
//     this.name = name;
//     this.pathToAudioFile = pathToAudioFile;
//     this.pathToImageFile = pathToImageFile;
//     this.playAudio = function(){
//         var audio = new Audio(this.pathToAudioFile)
//         audio.play()
//     }
// }

// var w = new Instrument('w',apath['w'])
// var a = new Instrument('a',apath['a'])
// var s = new Instrument('s',apath['s'])
// var d = new Instrument('d',apath['d'])
// var j = new Instrument('j',apath['j'])
// var k = new Instrument('k',apath['k'])
// var l = new Instrument('l',apath['l'])



