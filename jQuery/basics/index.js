$('h1').addClass('big-title margin-50'); // changing styles
$('h1').text('bye');    // changing text
$('button').html("<em>hey</em>") // changing text
console.log($('img').attr('src'))
$('a').attr('href',"https://www.youtube.com") // changing attribute value

// adding event listener

$('h1').click(function(){
    $('h1').css('color','purple')
})

$('button').click(function(){
    $('h1').css('color','purple')
})

$('input').keypress(function(event){
    console.log(event.key)
});

$(document).keypress(function(event){
    $('h1').text(event.key);
});

$('h1').on('mouseover',function(){
    $('h1').css('color','purple');
})

$('h1').before('<button>newbutton</button>');
$('h1').after('<button>newbutton</button>');
$('h1').prepend('<button>newbutton</button>');
$('h1').append('<button>newbutton</button>');
$('button')[0].remove()

// adding animations
// $('h1').hide()
// $('h1').show()
// $('h1').toggle()
// $('h1').fadeOut()
// $('h1').fadeIn()
// $('h1').fadeToggle()
// $('h1').slideUp()
// $('h1').slideDown()
// $('h1').slideToggle()
// $('h1').toggleClass('dimmed')

$('button').on('click',function(){
    $('h1').animate({opacity: 0.5});
})
$('button').on('click',function(){
    $('h1').animate({opacity: 0.5});
})
$('button').on('click',function(){
    $('img').slideUp().slideDown().animate({opacity: 0.5});
})



