import json

import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['JSON_AS_ASCII'] = False

# データの読み込み
with open('./results.json') as f:
    movies = json.loads(f.read())

# ホーム
# http://127.0.0.1:5000/

@app.route('/', methods=['GET'])
def home():
    return '''<h1>シンプルな推薦システム</h1>
<p>映画レコメンデーションのためのAPIプロトタイプ</p>'''

# 全てのアイテム
# http://127.0.0.1:5000/api/v1/resources/movies/all

@app.route('/api/v1/resources/movies/all', methods=['GET'])
def api_all():
    return jsonify(movies)

# 特定のユーザIDのアイテム
# http://127.0.0.1:5000/api/v1/resources/movies?id=1

@app.route('/api/v1/resources/movies', methods=['GET'])
def api_id():
    # URLにIDが含まれているか確認する。
    # IDが含まれていれば、変数に代入する。
    # IDが含まれていなければブラウザにエラーを表示する。
    if 'id' in request.args:
        id = str(request.args['id'])
    else:
        return "エラー: IDが含まれていません。IDを指定してください。"

    items = movies.get(id)

    # 結果のために空のリストを作成する。
    results = []

    # リストに映画を追加していく。
    for i in range(len(items)):
        item = items[i][0]
        results.append(item)

    # Pythonの辞書のリストをJSON形式に変換するためFlaskのjsonify関数を使う。
    return jsonify(results)

app.run()
