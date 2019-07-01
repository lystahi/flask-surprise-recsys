from collections import defaultdict

from surprise import SVD
from surprise import Dataset


def get_top_n(predictions, n=10):
    '''
    予測セットに基いて各ユーザにトップN件のレコメンデーションを返す。
    '''

    # まず各ユーザに予測値をマップする。
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # そして各ユーザに対して予測値をソートして最も高いk個を返す。
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n


# まずmovielensデータセットでSVDアルゴリズムを学習させる。
data = Dataset.load_builtin('ml-100k')
trainset = data.build_full_trainset()
algo = SVD()
algo.fit(trainset)

# そして学習用データに含まれていない全ての（ユーザ、アイテムの）組み合わせに対して評価を予測する。
testset = trainset.build_anti_testset()
predictions = algo.test(testset)

top_n = get_top_n(predictions, n=10)

# 各ユーザにレコメンドされるアイテムを表示する。
for uid, user_ratings in top_n.items():
    print(uid, [iid for (iid, _) in user_ratings])

# json形式で結果を保存する。
with open('./results.json', 'w') as f:
    json.dump(top_n, f, indent=2, ensure_ascii=False)
