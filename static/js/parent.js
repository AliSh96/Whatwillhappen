// Members section - playing videos functions
const members = document.querySelectorAll('#members li');

members.forEach(member => {
  const video = member.querySelector('.member-video');
  member.addEventListener('mouseenter', () => {
    video.play();
  });
  member.addEventListener('mouseleave', () => {
    video.pause();
    video.currentTime = 0;
  });
});

// Contact section ajax function
$(document).on('submit', '#contact-form', function(event){
  event.preventDefault()
  
  let email = $('#email').val()
  let wallet = $('#wallet').val()

  $.ajax({
    url: '/ajax-contact-form',
    data: {
      'email': email,
      'wallet': wallet,
    },
    dataType: 'json',
    success: function(response){
      $('#sbtn').prop('disabled', true).html('Submitting...');
      setTimeout(function() {
        $('#sbtn').prop('disabled', false).html('Submit');
      }, 5000); 
    }
  })
})

// Enabling drag scroll on predictions section
const container = document.querySelector('.predictions');
let isDragging = false;
let startX;
let scrollLeft;

container.addEventListener('mousedown', (e) => {
  isDragging = true;
  container.classList.add('active');
  startX = e.pageX - container.offsetLeft;
  scrollLeft = container.scrollLeft;
});

container.addEventListener('mouseleave', () => {
  isDragging = false;
});

container.addEventListener('mouseup', () => {
  isDragging = false;
});

container.addEventListener('mousemove', (e) => {
  if (!isDragging) return;
  e.preventDefault();
  const x = e.pageX - container.offsetLeft;
  const walk = (x - startX);
  container.scrollLeft = scrollLeft - walk;
});

  document.addEventListener('DOMContentLoaded', () => {
    const circleDates = document.querySelectorAll('#roadmap .circle .circle-img');
    const lastCircleDate = circleDates[circleDates.length - 1];
    lastCircleDate.style.animation = "fluctuate-shadow 1s infinite alternate ease-in-out";
});

// Loading display toggle function
window.addEventListener('load', function () {
  const loader = document.getElementById('loading');
  loader.style.opacity = '0';
  loader.style.transition = 'opacity 0.5s ease';
  setTimeout(() => {
    loader.style.display = 'none';
  }, 500);
});
