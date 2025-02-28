// Main JavaScript for Portfolio Website

document.addEventListener('DOMContentLoaded', function() {
    // Toggle for showing all projects
    const viewAllBtn = document.getElementById('view-all-projects');
    if (viewAllBtn) {
        viewAllBtn.addEventListener('click', function() {
            const allProjectsContainer = document.getElementById('all-projects-container');
            if (allProjectsContainer) {
                if (allProjectsContainer.style.display === 'none') {
                    allProjectsContainer.style.display = 'flex';
                    viewAllBtn.textContent = 'Show Less';
                } else {
                    allProjectsContainer.style.display = 'none';
                    viewAllBtn.textContent = 'View All Projects';
                }
            }
        });
    }
    
    // Add active class to nav items based on scroll position
    const sections = document.querySelectorAll('section[id]');
    if (sections.length) {
        window.addEventListener('scroll', function() {
            let current = '';
            
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                const sectionHeight = section.clientHeight;
                if (scrollY >= (sectionTop - 200)) {
                    current = section.getAttribute('id');
                }
            });
            
            const navItems = document.querySelectorAll('.sidebar .nav-link');
            navItems.forEach(navItem => {
                navItem.classList.remove('active');
                if (navItem.getAttribute('href').includes(current)) {
                    navItem.classList.add('active');
                }
            });
        });
    }
    
    // Auto-hiding messages after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    if (alerts.length) {
        setTimeout(function() {
            alerts.forEach(alert => {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            });
        }, 5000);
    }
    
    // Animate elements when they come into view
    const animateOnScroll = function() {
        const elementsToAnimate = document.querySelectorAll('.animate-on-scroll');
        
        elementsToAnimate.forEach(element => {
            const elementPosition = element.getBoundingClientRect().top;
            const screenPosition = window.innerHeight / 1.3;
            
            if (elementPosition < screenPosition) {
                element.classList.add('animated');
            }
        });
    };
    
    if (document.querySelectorAll('.animate-on-scroll').length) {
        window.addEventListener('scroll', animateOnScroll);
        // Initial check
        animateOnScroll();
    }
});