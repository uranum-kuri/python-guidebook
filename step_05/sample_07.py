# Copyright (c) 2021 uranum

for i in range(10):  # 10回繰り返します
    if i == 5:  # iが5と等しいときにcontinueを実行します
        print("処理をスキップします")
        continue  # このループをスキップします
    print("変数iは", i, "です")
