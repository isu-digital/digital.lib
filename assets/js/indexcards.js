document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.about-us-card').forEach(function(card) {
      card.addEventListener('click', function() {
        const link = card.getAttribute('data-link');
        if (link) {
          window.open(link, '_blank');
        }
      });
    });
  
    document.querySelectorAll('.about-us-card .btn').forEach(function(button) {
      button.addEventListener('click', function(event) {
        event.stopPropagation(); // Prevent the card click event from firing
      });
    });
  });