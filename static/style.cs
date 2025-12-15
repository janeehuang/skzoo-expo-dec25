/* --- 1. 核心背景：漸層拿鐵色 + 大雪紛飛 --- */
body {
    background: linear-gradient(to bottom, #D9C5B2, #9E7E56); /* 漸層背景 */
    background-attachment: fixed; 
    color: #FDFBF7;            /* 奶油白文字 */
    font-family: 'Helvetica Neue', Arial, sans-serif;
    text-align: center;
    margin: 0;
    padding: 20px;
    overflow-x: hidden;
    position: relative;
    min-height: 100vh;
}

/* --- 雪花動畫設定 --- */
body::before, body::after {
    content: "";
    position: absolute;
    top: -100%;
    left: 0;
    width: 100%;
    height: 200%;
    pointer-events: none;
    background-image: 
        radial-gradient(6px 6px at 10% 10%, #FDFBF7 50%, transparent 50%),
        radial-gradient(4px 4px at 20% 30%, #FDFBF7 50%, transparent 50%),
        radial-gradient(8px 8px at 30% 50%, #FDFBF7 50%, transparent 50%),
        radial-gradient(5px 5px at 40% 70%, #FDFBF7 50%, transparent 50%),
        radial-gradient(7px 7px at 50% 90%, #FDFBF7 50%, transparent 50%),
        radial-gradient(4px 4px at 60% 10%, #FDFBF7 50%, transparent 50%),
        radial-gradient(8px 8px at 70% 30%, #FDFBF7 50%, transparent 50%),
        radial-gradient(5px 5px at 80% 50%, #FDFBF7 50%, transparent 50%),
        radial-gradient(6px 6px at 90% 70%, #FDFBF7 50%, transparent 50%),
        radial-gradient(4px 4px at 15% 85%, #FDFBF7 50%, transparent 50%),
        radial-gradient(7px 7px at 35% 25%, #FDFBF7 50%, transparent 50%),
        radial-gradient(5px 5px at 55% 45%, #FDFBF7 50%, transparent 50%),
        radial-gradient(8px 8px at 75% 65%, #FDFBF7 50%, transparent 50%),
        radial-gradient(4px 4px at 95% 5%, #FDFBF7 50%, transparent 50%);
    background-size: 500px 500px;
    animation-name: snow;
    animation-timing-function: linear;
    animation-iteration-count: infinite;
    z-index: 0;
}

body::before { animation-duration: 20s; opacity: 0.7; }
body::after { background-size: 600px 600px; animation-duration: 12s; opacity: 0.9; }

@keyframes snow {
    0% { transform: translateY(0); }
    100% { transform: translateY(500px); }
}

h1 { 
    margin-bottom: 30px; 
    letter-spacing: 1px; 
    text-shadow: 2px 2px 4px rgba(0,0,0,0.2); 
    position: relative; z-index: 1; 
}

/* --- 2. 問卷按鈕樣式 (這就是剛剛加的新東西) --- */
.survey-btn {
    display: inline-block;
    background-color: #A0522D;
    color: #ffffff;
    padding: 12px 25px;
    margin-bottom: 30px;
    border-radius: 50px;
    text-decoration: none;
    font-weight: bold;
    font-size: 1.1em;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    transition: all 0.3s ease;
    position: relative; z-index: 2; /* 浮在雪花上 */
}

.survey-btn:hover {
    background-color: #8B4513;
    transform: translateY(-3px);
    box-shadow: 0 6px 15px rgba(0,0,0,0.4);
}

/* --- 3. 畫廊與卡片設定 --- */
.gallery {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
    padding: 10px;
    position: relative; z-index: 1;
}

.card {
    background-color: #FDFBF7;
    border-radius: 12px;
    overflow: hidden;
    width: 300px;
    display: flex;
    flex-direction: column;
    text-align: left;
    box-shadow: 0 4px 15px rgba(60, 40, 20, 0.3);
    transition: transform 0.2s;
}

.card:hover { transform: translateY(-5px); }

/* --- 輪播與圖片 (保持完整比例) --- */
.slideshow-container {
    position: relative;
    width: 100%;
    background-color: transparent;
    min-height: 50px;
}

.slide-img {
    width: 100%;
    height: auto;     /* 高度自動 */
    display: none;    /* 預設隱藏 */
}

.slide-img.active {
    display: block;   /* 顯示 */
}

/* --- 卡片文字內容 --- */
.card-content { padding: 15px; flex-grow: 1; }
.nickname { color: #A0522D; font-weight: bold; font-size: 1.1em; margin-bottom: 5px; display: flex; align-items: center; }
.message { color: #5D4037; font-size: 0.95em; margin-bottom: 10px; line-height: 1.4; word-wrap: break-word; }
.timestamp { color: #8D6E63; font-size: 0.8em; }
.badge { background-color: #D7CCC8; color: #5D4037; font-size: 0.7em; padding: 2px 8px; border-radius: 10px; margin-left: 8px; border: 1px solid #A1887F; }