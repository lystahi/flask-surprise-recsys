# flask-surprise-recsys

ターミナルもしくはコマンドプロンプトで

python recommender.py

を実行して、レコメンドするアイテム一覧を作成。

python api.py

を実行してFlaskアプリケーションを起動。

ブラウザで

http://127.0.0.1:5000/
がホーム画面

http://127.0.0.1:5000/api/v1/resources/movies/all
が全てのアイテム

http://127.0.0.1:5000/api/v1/resources/movies?id=1
がIDが1のユーザに対して推薦するアイテムのID
となります。

何かおかしな点やアドバイス等がございましたらコメントいただけますと幸いです。

参考：
https://surprise.readthedocs.io/en/stable/FAQ.html
https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
