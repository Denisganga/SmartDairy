document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Counter animation
    function animateCounters() {
        const counters = document.querySelectorAll('.counter');
        counters.forEach(counter => {
            const target = parseInt(counter.getAttribute('data-target'));
            const increment = target / 100;
            let current = 0;
            
            const updateCounter = () => {
                if (current < target) {
                    current += increment;
                    counter.textContent = Math.ceil(current);
                    setTimeout(updateCounter, 20);
                } else {
                    counter.textContent = target;
                }
            };
            
            updateCounter();
        });
    }

    // Intersection Observer for animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const element = entry.target;
                
                // Add animation classes
                if (element.classList.contains('fade-in-up')) {
                    element.style.opacity = '1';
                    element.style.transform = 'translateY(0)';
                }
                
                if (element.classList.contains('fade-in-left')) {
                    element.style.opacity = '1';
                    element.style.transform = 'translateX(0)';
                }
                
                if (element.classList.contains('fade-in-right')) {
                    element.style.opacity = '1';
                    element.style.transform = 'translateX(0)';
                }

                // Animate counters when hero stats come into view
                if (element.classList.contains('hero-stats')) {
                    animateCounters();
                }

                // Add stagger effect for feature cards
                if (element.classList.contains('feature-card')) {
                    const delay = element.getAttribute('data-delay') || 0;
                    setTimeout(() => {
                        element.style.opacity = '1';
                        element.style.transform = 'translateY(0)';
                    }, delay);
                }
            }
        });
    }, observerOptions);

    // Observe elements for animation
    document.querySelectorAll('.fade-in-up, .fade-in-left, .fade-in-right, .hero-stats, .feature-card').forEach(el => {
        // Set initial state
        el.style.opacity = '0';
        if (el.classList.contains('fade-in-up') || el.classList.contains('feature-card')) {
            el.style.transform = 'translateY(30px)';
        } else if (el.classList.contains('fade-in-left')) {
            el.style.transform = 'translateX(-30px)';
        } else if (el.classList.contains('fade-in-right')) {
            el.style.transform = 'translateX(30px)';
        }
        
        el.style.transition = 'all 0.8s ease-out';
        observer.observe(el);
    });

    // Navbar background change on scroll
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 50) {
            navbar.style.background = 'rgba(0, 0, 0, 0.95)';
        } else {
            navbar.style.background = 'rgba(0, 0, 0, 0.9)';
        }
    });

    // Parallax effect for hero section
    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;
        const heroSection = document.querySelector('.hero-section');
        if (heroSection) {
            heroSection.style.transform = `translateY(${scrolled * 0.5}px)`;
        }
    });

    // Form validation and enhancement
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processing...';
                submitBtn.disabled = true;
            }
        });
    });

    // Add floating animation to images
    const images = document.querySelectorAll('.hero-image img');
    images.forEach(img => {
        img.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.05) translateY(-10px)';
        });
        
        img.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1) translateY(0)';
        });
    });

    // Video play on scroll
    const videos = document.querySelectorAll('video');
    const videoObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.play();
            } else {
                entry.target.pause();
            }
        });
    }, { threshold: 0.5 });

    videos.forEach(video => {
        videoObserver.observe(video);
    });
});
