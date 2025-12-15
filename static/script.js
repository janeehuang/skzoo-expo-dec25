document.addEventListener('DOMContentLoaded', function() {
    
    // --- 功能 1：每 5 秒自動重新整理網頁 (抓取最新投稿) ---
    setTimeout(function() {
        window.location.reload(); // 這行指令就是「重新整理」
    }, 60000); // 5000 毫秒 = 5 秒 (你可以改這個數字)


    // --- 功能 2：每 3 秒自動換下一張照片 (輪播特效) ---
    setInterval(function() {
        
        // 1. 找到網頁上所有的「輪播容器」
        const containers = document.querySelectorAll('.slideshow-container');
        
        containers.forEach(container => {
            // 2. 找到這個容器裡的所有圖片
            const images = container.querySelectorAll('.slide-img');
            
            // 如果這人只有 1 張照片，就不需要輪播
            if (images.length > 1) {
                let activeIndex = 0;
                
                // 3. 找出現在顯示的是第幾張 (有 active class 的那張)
                images.forEach((img, index) => {
                    if (img.classList.contains('active')) {
                        activeIndex = index;
                        img.classList.remove('active'); // 把現在這張藏起來
                    }
                });
                
                // 4. 計算下一張是誰 (用餘數運算 % 來讓它循環回到 0)
                let nextIndex = (activeIndex + 1) % images.length;
                
                // 5. 讓下一張顯示出來
                images[nextIndex].classList.add('active');
            }
        });

    }, 3000); // 3000 毫秒 = 3 秒換一張照片
});