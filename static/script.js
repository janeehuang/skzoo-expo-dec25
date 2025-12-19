document.addEventListener('DOMContentLoaded', function() {
    
    // 1. 自動重整 (僅限首頁)
    if (window.location.pathname === '/' || window.location.pathname === '/index') {
        setTimeout(function() {
            window.location.reload(); 
        }, 60000); 
    }

    // 2. 輪播特效 (僅限首頁)
    setInterval(function() {
        const containers = document.querySelectorAll('.slideshow-container');
        containers.forEach(container => {
            const images = container.querySelectorAll('.slide-img');
            if (images.length > 1) {
                let activeIndex = 0;
                images.forEach((img, index) => {
                    if (img.classList.contains('active')) {
                        activeIndex = index;
                        img.classList.remove('active');
                    }
                });
                let nextIndex = (activeIndex + 1) % images.length;
                images[nextIndex].classList.add('active');
            }
        });
    }, 3000); 

    // 3. Timeline 滑動偵測 (控制年份放大)
    const rows = document.querySelectorAll('.timeline-row');

    if (rows.length > 0) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    // 這一行進入畫面中間，加上 active-row
                    entry.target.classList.add('active-row');
                } else {
                    entry.target.classList.remove('active-row');
                }
            });
        }, {
            root: null,
            threshold: 0.6, // 至少看到 60% 才觸發
            rootMargin: "-25% 0px -25% 0px" // 縮小範圍，讓焦點集中在螢幕中間
        });

        rows.forEach(row => observer.observe(row));
    }
});