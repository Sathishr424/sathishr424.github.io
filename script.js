

window.onscroll = function() {myFunction()};

$(() => {
    document.body.scrollTop = document.documentElement.scrollTop = 0;
    disableScrolling();
})

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
    let timeline0 = new TimelineMax();

    // timeline0
    // .set('#cover-image-parent', {opacity: 0, ease: Sine.easeInOut})
    // .to('#cover-image-parent', 0.5, {opacity: 1, ease: Sine.easeInOut, scale: 1})
    // .from('#cimage', 0.5, {
    //     css: {transform: 'rotateY(90deg)', opacity: 0, scale: 0.3},
    //     ease: Sine.easeInOut
    //     , onComplete: () => {
    //         console.log("Finished");
    //         enableScrolling();
    // }}, '-=0.5')
    
    timeline0
    .set('#cover-image-parent', {opacity: 0, onComplete: () => {disableScrolling(); 
        document.getElementById('dummy-placeholder').style.height = '0px';
        document.body.scrollTop = document.documentElement.scrollTop = 0;}})
    .set('#cimage', {css: {transform: 'rotateY(0deg)'}})
    .set('#cimage', {y: 200, z: -100, scale: 0.2, opacity: 0})
    .to('#cover-image-parent', 1, {opacity: 1, ease: Sine.easeInOut})
    .to('#cimage', 1, {scale: 0.5, opacity: 1, ease: Sine.easeIn}, '-=1')
    .to('#cimage', 0.5, {scale: 1, z: 0, y: 0, ease: Sine.easeIn, onComplete: () => {
                console.log("Finished");
                enableScrolling();
    }}, '-=0.5')

    let scene0 = new ScrollMagic.Scene({
        triggerElement: '#cover-image-parent',
        triggerHook: 1,
        reverse: false
    }).setTween(timeline0)
    .addTo(controller);

    let timeline1 = new TimelineMax();

    timeline1
    // .set('#cimage', {css: {transform: 'rotateY(0deg)'}})
    // .set('#cimage', {y: 0, z: 0, scale: 1, opacity: 1})
    // .from('#cover-image-parent', 0, {opacity: 0, ease: Sine.easeInOut})
    // .to('#cover-image-parent', 4, {opacity: 1, ease: Sine.easeInOut}, '+=2')
    // .from('#cimage', 8, {
    //     css: {transform: 'rotateY(90deg)', opacity: 0, scale: 0.3},
    //     ease: Sine.easeInOut
    // }, '-=1')
    .to('#cimage', 4, {
        css: {transform: 'rotateY(90deg)', opacity: 0},
        ease: Sine.easeInOut
    }, '+=4')
    .to('#cover-image-parent', 4, {opacity: 0, ease: Sine.easeInOut})

    let scene1 = new ScrollMagic.Scene({
        triggerElement: '#cover-image-parent',
        triggerHook: 0,
        duration: '200%',
    }).setTween(timeline1)
    .addTo(controller)
    .setPin('#cover-image-parent')
    .on('leave', (el) => {
        if (el.scrollDirection == "FORWARD") window.scrollBy(0, window.innerHeight);
        else window.scrollBy(0, -(window.innerHeight));
    });

    let timeline2 = new TimelineMax();

    timeline2
    .from('#section-two', 4, {opacity: 0, ease: Sine.easeInOut})
    .from('.welcome-text', 4, {x: -200, opacity: 0, ease: Sine.easeInOut}, '-=4')
    .from('.welcome-text2', 4, {x: 200, opacity: 0, ease: Power4.easeInOut}, '-=4')
    .from('.welcome-text3', 4, {x: -200, opacity: 0, ease: Sine.easeInOut})
    .from('.welcome-text4', 4, {x: 200, opacity: 0, ease: Sine.easeInOut}, '-=4')
    .to('.welcome-text', 2, {x: -200, opacity: 0, ease: Sine.easeInOut}, '+=8')
    .to('.welcome-text2', 2, {x: 200, opacity: 0, ease: Sine.easeInOut}, '-=1')
    .to('.welcome-text3', 2, {x: -200, opacity: 0, ease: Sine.easeInOut}, '-=1')
    .to('.welcome-text4', 2, {x: 200, opacity: 0, ease: Sine.easeInOut}, '-=1')
    .to('#section-two', 2, {opacity: 0, ease: Sine.easeInOut}, '-=1');

    let scene2 = new ScrollMagic.Scene({
        duration: '200%',
        triggerElement: '#section-two',
        triggerHook: 0
    }).setTween(timeline2)
    .setPin('#section-two').addTo(controller)
    .on('leave', (el) => {
        if (el.scrollDirection == "FORWARD") window.scrollBy(0, window.innerHeight);
        else window.scrollBy(0, -(window.innerHeight));
    });

    let timeline3 = new TimelineMax();

    timeline3
    .from('#section-three', 4, {opacity: 0, ease: Sine.easeInOut})
    .from('.section-three2', 4, {x: -200, opacity: 0, ease: Sine.easeInOut}, '-=4')
    .from('.section-three3', 4, {css: {transform: 'translateZ(-200)', opacity: 0}, ease: Bounce.easeInOut})
    .from('.section-three4', 4, {x: -200, opacity: 0, ease: Sine.easeInOut}, '-=4')
    .from('.section-three5', 4, {x: 200, opacity: 0, ease: Sine.easeInOut}, '-=4')
    .to('.section-three2', 2, {x: -200, opacity: 0, ease: Sine.easeInOut}, '+=4')
    .to('.section-three3', 2, {css: {transform: 'translateZ(-200)', opacity: 0}, ease: Sine.easeInOut}, '-=2')
    .to('.section-three4', 2, {x: -200, opacity: 0, ease: Sine.easeInOut}, '-=2')
    .to('.section-three5', 2, {x: 200, opacity: 0, ease: Sine.easeInOut}, '-=2')
    .to('#section-three', 2, {opacity: 0, ease: Sine.easeInOut}, '-=2');

    let scene3 = new ScrollMagic.Scene({
        duration: '200%',
        triggerElement: '#section-three',
        triggerHook: 0
    }).setTween(timeline3)
    .setPin('#section-three').addTo(controller)
    .on('leave', (el) => {
        if (el.scrollDirection == "FORWARD") window.scrollBy(0, window.innerHeight);
        else window.scrollBy(0, -(window.innerHeight));
    });

    let timeline4 = new TimelineMax();

    timeline4
    .from('#section-four2', 4, {css: {transform: 'translateZ(-200)', opacity: 0}, ease: Sine.easeInOut})
    .to('#section-four2', 2, {css: {transform: 'translateZ(-200)', opacity: 0}, ease: Sine.easeInOut}, '+=4')

    let scene4 = new ScrollMagic.Scene({
        duration: '200%',
        triggerElement: '#section-four',
        triggerHook: 0
    }).setTween(timeline4)
    .setPin('#section-four').addTo(controller)
    .on('leave', (el) => {
        if (el.scrollDirection == "FORWARD") window.scrollBy(0, window.innerHeight);
        else window.scrollBy(0, -(window.innerHeight));
    });

    let timeline5 = new TimelineMax();

    timeline5
    .from('#section-five', 4, {opacity: 0, ease: Sine.easeInOut})
    .from('.section-five-image1', 6, {opacity: 0, ease: Sine.easeInOut}, '-=2')
    .from('.section-five-image2', 6, {opacity: 0, ease: Sine.easeInOut}, '-=6')
    .to('.section-five-image1', 4, {x:-200, opacity:0.5, ease: Sine.easeInOut}, '+=4')
    .to('.section-five-image2', 4, {x:200, opacity:0.5, ease: Sine.easeInOut}, '-=4')
    .from('.section-five2', 4, {css: {transform: 'translateZ(-200)', opacity: 0}, ease: Sine.easeInOut}, '-=2')
    .from('.section-five3', 4, {css: {transform: 'translateZ(-200)', opacity: 0}, ease: Sine.easeInOut}, '-=4')
    .to('.section-five2', 2, {css: {transform: 'translateZ(-200)', opacity: 0}, ease: Sine.easeInOut}, '+=4')
    .to('.section-five3', 2, {css: {transform: 'translateZ(-200)', opacity: 0}, ease: Sine.easeInOut}, '-=2')
    .to('.section-five-image1', 2, {x:0, opacity: 0, ease: Sine.easeInOut}, '-=1')
    .to('.section-five-image2', 2, {x:0, opacity: 0, ease: Sine.easeInOut}, '-=2')
    .to('#section-five', 2, {opacity: 0, ease: Sine.easeInOut}, '-=2');

    let scene5 = new ScrollMagic.Scene({
        duration: '400%',
        triggerElement: '#section-five',
        triggerHook: 0
    }).setTween(timeline5)
    .setPin('#section-five').addTo(controller)
    .on('leave', (el) => {
        if (el.scrollDirection == "FORWARD") window.scrollBy(0, window.innerHeight);
        else window.scrollBy(0, -(window.innerHeight));
    });

    let timeline6 = new TimelineMax();

    timeline6
    .from('#section-six', 4, {opacity: 0, ease: Sine.easeInOut})
    .from('.section-six-image', 2, {opacity: 0, x:100, ease: Sine.easeInOut}, '-=4')

    .from('.section-six2', 4, {css: {transform: 'translateZ(-200)', opacity: 0}, ease: Sine.easeInOut})
    .from('.section-six3', 4, {x:-100, opacity: 0, ease: Sine.easeInOut}, '-=4')
    .from('.section-six4', 4, {x:100, opacity: 0, ease: Sine.easeInOut}, '-=4')

    .to('.section-six-image', 2, {opacity: 0, x:100, ease: Sine.easeInOut}, '+=4')
    .to('.section-six2', 2, {css: {transform: 'translateZ(-200)', opacity: 0}, ease: Sine.easeInOut}, '-=2')
    .to('.section-six3', 2, {x:-100, opacity: 0, ease: Sine.easeInOut}, '-=2')
    .to('.section-six4', 2, {x:100, opacity: 0, ease: Sine.easeInOut}, '-=2')
    .to('#section-six', 2, {opacity: 0, ease: Sine.easeInOut}, '-=2');

    let scene6 = new ScrollMagic.Scene({
        duration: '300%',
        triggerElement: '#section-six',
        triggerHook: 0
    }).setTween(timeline6)
    .setPin('#section-six').addTo(controller)
    .on('leave', (el) => {
        if (el.scrollDirection == "FORWARD") window.scrollBy(0, window.innerHeight);
        else window.scrollBy(0, -(window.innerHeight));
    });
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
        var x = document.getElementById("front-cover");
    
        x.addEventListener('animationend', function abc(event){
            x.removeEventListener('animationend', abc);
            x.style.display = 'none';
            startPage();
        })
    });
})(jQuery);