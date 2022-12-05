document.body.scrollTop = document.documentElement.scrollTop = 0;

window.onscroll = function() {myFunction()};

function myFunction() {
  var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
  var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  var scrolled = (winScroll / height) * 100;
  document.getElementById("scroll-status").style.width = scrolled + "%";
}

const disableScrolling = () => {
    $('body').addClass('stop-scrolling');
    $('body').bind('touchmove', function(e){e.preventDefault()})
}

const enableScrolling = () => {
    $('body').removeClass('stop-scrolling');
    $('body').unbind('touchmove');
}

let controller = new ScrollMagic.Controller();

const startPage = () => {
    enableScrolling();
    let timeline1 = new TimelineMax();

    timeline1.to('#cimage', 2, {
        css: {transform: 'rotateY(90deg)', opacity: 0},
        scale: 0.3,
        autoAlpha: 0,
        onComplete: function(){
            // $('#cover-image').hide();
        }
    })

    let scene1 = new ScrollMagic.Scene({
        duration: '100%',
        triggerElement: '#cover-image',
        triggerHook: 0
    }).setTween(timeline1)
    .setPin('#cover-image').addTo(controller);

    let timeline2 = new TimelineMax();

    timeline2.from('.welcome-text', 1, {x: -200, opacity: 0, ease: Power3.easeInOut})
    .from('.welcome-text2', 1, {x: 200, opacity: 0, ease: Power4.easeInOut}, '-=1')
    .from('.welcome-text3', 1, {x: -200, opacity: 0, ease: Power3.easeInOut})
    .from('.welcome-text4', 1, {x: 200, opacity: 0, ease: Power3.easeInOut}, '-=1')
    .to('.welcome-text', 1, {x: -200, opacity: 0, ease: Power3.easeInOut}, '+=1')
    .to('.welcome-text2', 1, {x: 200, opacity: 0, ease: Power3.easeInOut}, '-=1')
    .to('.welcome-text3', 1, {x: -200, opacity: 0, ease: Power3.easeInOut}, '-=1')
    .to('.welcome-text4', 1, {x: 200, opacity: 0, ease: Power3.easeInOut}, '-=1');

    let scene2 = new ScrollMagic.Scene({
        duration: '200%',
        triggerElement: '#section-two',
        triggerHook: 'onLeave'
    }).setTween(timeline2)
    .setPin('#section-two').addTo(controller);

    let timeline3 = new TimelineMax();

    timeline3.from('.section-three2', 2, {x: -200, opacity: 0, ease: Power3.easeInOut})
    .from('.section-three3', 2, {css: {transform: 'translateZ(-200)', opacity: 0}, ease: Bounce.easeInOut})
    .from('.section-three4', 2, {x: -200, opacity: 0, ease: Power3.easeInOut}, '-=2')
    .from('.section-three5', 2, {x: 200, opacity: 0, ease: Power3.easeInOut}, '-=2')
    .to('.section-three2', 2, {x: -200, opacity: 0, ease: Power3.easeInOut}, '+=1')
    .to('.section-three3', 2, {css: {transform: 'translateZ(-200)', opacity: 0}, ease: Power3.easeInOut}, '-=2')
    .to('.section-three4', 2, {x: -200, opacity: 0, ease: Power3.easeInOut}, '-=2')
    .to('.section-three5', 2, {x: 200, opacity: 0, ease: Power3.easeInOut}, '-=2');

    let scene3 = new ScrollMagic.Scene({
        duration: '200%',
        triggerElement: '#section-three',
        triggerHook: 'onLeave'
    }).setTween(timeline3)
    .setPin('#section-three').addTo(controller);

    let timeline4 = new TimelineMax();

    timeline4.from('#section-four2', 2, {css: {transform: 'translateZ(-200)', opacity: 0}, ease: Power3.easeInOut}).to('#section-four2', 2, {css: {transform: 'translateZ(-200)', opacity: 0}, ease: Power3.easeInOut}, '+=2')

    let scene4 = new ScrollMagic.Scene({
        duration: '200%',
        triggerElement: '#section-four',
        triggerHook: 'onLeave'
    }).setTween(timeline4)
    .setPin('#section-four').addTo(controller);

    let timeline5 = new TimelineMax();

    timeline5.from('.section-five-image1', 2, {opacity: 0, ease: Power3.easeInOut})
    .from('.section-five-image2', 2, {opacity: 0, ease: Power3.easeInOut}, '-=2')
    .to('.section-five-image1', 2, {x:-200, ease: Power3.easeInOut})
    .to('.section-five-image2', 2, {x:200, ease: Power3.easeInOut}, '-=2')
    .from('.section-five2', 2, {css: {transform: 'translateZ(-200)', opacity: 0}, ease: Power3.easeInOut}, '-=1')
    .from('.section-five3', 2, {css: {transform: 'translateZ(-200)', opacity: 0}, ease: Power3.easeInOut}, '-=2')
    .to('.section-five-image1', 2, {x:-200, opacity: 0, ease: Power3.easeInOut}, '+=1')
    .to('.section-five-image2', 2, {x:200, opacity: 0, ease: Power3.easeInOut}, '-=2')
    .to('.section-five2', 2, {css: {transform: 'translateZ(-200)', opacity: 0}, ease: Power3.easeInOut}, '-=2')
    .to('.section-five3', 2, {css: {transform: 'translateZ(-200)', opacity: 0}, ease: Power3.easeInOut}, '-=2')

    let scene5 = new ScrollMagic.Scene({
        duration: '300%',
        triggerElement: '#section-five',
        triggerHook: 'onLeave'
    }).setTween(timeline5)
    .setPin('#section-five').addTo(controller);

    let timeline6 = new TimelineMax();

    timeline6.from('.section-six-image', 2, {opacity: 0, x:100, ease: Power3.easeInOut})

    .from('.section-six2', 2, {css: {transform: 'translateZ(-200)', opacity: 0}, ease: Power3.easeInOut})
    .from('.section-six3', 2, {x:-100, opacity: 0, ease: Power3.easeInOut}, '-=2')
    .from('.section-six4', 2, {x:100, opacity: 0, ease: Power3.easeInOut}, '-=2')

    .to('.section-six-image', 2, {opacity: 0, x:100, ease: Power3.easeInOut}, '+=2')
    .to('.section-six2', 2, {css: {transform: 'translateZ(-200)', opacity: 0}, ease: Power3.easeInOut}, '-=2')
    .to('.section-six3', 2, {x:-100, opacity: 0, ease: Power3.easeInOut}, '-=2')
    .to('.section-six4', 2, {x:100, opacity: 0, ease: Power3.easeInOut}, '-=2')

    let scene6 = new ScrollMagic.Scene({
        duration: '200%',
        triggerElement: '#section-six',
        triggerHook: 'onLeave'
    }).setTween(timeline6)
    .setPin('#section-six').addTo(controller);
}

(function($) {
    var loadImages = new Promise(function(done) {
        var loading = $("img").length;
        $("img").each(function() {
            $("<img/>")
                .on('load', function() {
                    loading--;
                    if (!loading) done();
                })
                .on('error', function() {
                    loading--;
                    if (!loading) done();
                })
                .attr("src", $(this).attr("src"))
        });
    });
    loadImages.then(function() {
        // console.log("IMAGE LOADED")
        disableScrolling();
        var x = document.getElementById("front-cover");
    
        x.addEventListener('animationend', function abc(event){
            // console.log("Animation ended")
            x.removeEventListener('animationend', abc);
            x.style.display = 'none';
            let img = document.getElementById('cimage');
            img.style.animation = 'cover-image-animation 2s ease-in-out 1s forwards';

            img.addEventListener('animationend', function abc(event){
                img.removeEventListener('animationend', abc);
                let p = document.getElementById('cover-image-parent');
                p.innerHTML = `<div id="cover-image" class="w-full h-[100vh] flex justify-center items-center overflow-hidden">
                <img id="cimage" style="height:80%; transform: rotateY(0deg) scale(1);" src="cover.jpg" class="h-[80%]"/>
            </div>`;
            
                startPage();
            })
        })
    });
})(jQuery);