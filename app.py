from flask import Flask, render_template, jsonify
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# 1. 連接 Firebase (大廚拿鑰匙開冰箱)
# 確保你的 JSON 檔案名稱是 service-account.json 並且放在同一個資料夾
cred = credentials.Certificate("./service-account.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# 2. 首頁路由：當有人連到網站首頁，就給他看 HTML
# app.py

@app.route('/')
def index():
    posts_ref = db.collection('skzoo_posts').order_by('timestamp', direction=firestore.Query.DESCENDING)
    docs = posts_ref.stream()

    # 1. 先抓出所有原始資料
    all_posts = []
    for doc in docs:
        post = doc.to_dict()
        all_posts.append(post)

    # 2. 開始進行「歸類」 (Group by nickname)
    # 結構會變成： { "達康寶": [照片1, 照片2], "某某某": [照片1] }
    grouped_posts = {}
    
    for post in all_posts:
        nickname = post.get('nickname', 'Unknown')
        
        # 如果這個人還沒在名單上，先幫他開一個空位
        if nickname not in grouped_posts:
            grouped_posts[nickname] = []
            
        # 把照片放進這個人的口袋裡
        grouped_posts[nickname].append(post)

    # 3. 把整理好的 grouped_posts 送給網頁
    return render_template('index.html', grouped_posts=grouped_posts)

@app.route('/timeline')
def timeline():
    # 定義時間軸資料：依照時間「由舊到新」排列 (升冪)
    
    timeline_data = [
        # 2017 年 (起點)
        ("2017", [
            ("《Mixtape》", "Hellevator /《Mixtape》")
        ]),

        # 2018 年
        ("2018", [
            ("District 9", "District 9 /《I am NOT》"),
            ("I am WHO", "My Pace /《I am WHO》"),
            ("I am YOU", "I am YOU /《I am YOU》"),
            # 如果之後要補 I am WHO, I am YOU 可以加在這邊
        ]),

        # 2019 年
        ("2019", [
            # 順序：Miroh (若有) -> Yellow Wood -> Levanter
            ("《Clé 1 : MIROH》", "MIROH / 《Clé 1 : MIROH》"),
            ("《Clé 2: Yellow Wood》", "Double Knot / 《Clé 2: Yellow Wood》"),
            ("《Clé : LEVANTER》", "LEVANTER /《Clé : LEVANTER》"),
            ("〈Mixtape : Gone Days〉", "Gone Days /〈Mixtape : Gone Days〉")

        ]),

        # 2020 年
        ("2020", [
            # 順序：神菜單(6月) -> 後門(9月)
            ("《GO生》", "God's Menu / 《GO生》"),
            ("《IN生》", " Back Door /《IN生》")
        ]),
        # 2022 年
        ("2021", [
            # 順序：Maniac(3月) -> Case 143(10月)
            ("Mixtape  애", "OH /〈Mixtape  애〉"),
            ("noeasy", "Thunderous /《NOEASY》"),
            ("《Christmas EveL》", "Christmas EveL /《Christmas EveL》")
        ]),


        # 2022 年
        ("2022", [
            # 順序：Maniac(3月) -> Case 143(10月)
            ("maniac", "Maniac /《ODDINARY》"),
            ("case143", "Case 143 /《MAXIDENT》 ")
        ]),
        
        # 2023 年
        ("2023", [
            # 順序：特(6月) -> 樂(11月)
            ("5星", "S-Class /《★★★★★ (5-STAR)》"),
            ("樂", "樂 (LALALALA) /《樂-STAR》")
        ]),

        # 2024 年 (最新)
        ("2024", [
            # 順序：Lose My Breath(5月) -> ATE(7月)
            ("Lose My Breath", "Lose My Breath / 《Lose My Breath》"),
            ("ATE", "Chk Chk Boom /《ATE》"),
            ("walkin on water", "Walkin On Water /《合（HOP) 》")
        ]),
        ("2025", [
            # 順序：Lose My Breath(5月) -> ATE(7月)
            ("KARMA", "CEREMONY /《KARMA》"),
            ("do it", "Do It / 《DO IT》")
        ])
    ]

    # 把這些資料傳給網頁
    return render_template('timeline.html', timeline_data=timeline_data)


# 3. API 路由：專門吐資料給前端 (這是 Option B 的精髓)
# 前端不用自己連資料庫，而是來問這個路徑拿資料
@app.route('/api/posts')
def get_posts():
    posts_ref = db.collection('skzoo_posts')
    # 依照時間排序，最新的在前面
    docs = posts_ref.order_by('timestamp', direction=firestore.Query.DESCENDING).stream()
    
    data_list = []
    for doc in docs:
        post = doc.to_dict()
        # 把資料整理乾淨放進清單
        data_list.append({
            'nickname': post.get('nickname', 'STAY'),
            'message': post.get('message', ''),
            'photo_url': post.get('photo_url', ''),
            'timestamp': post.get('timestamp')
        })
    
    return jsonify(data_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
