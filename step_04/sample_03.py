# Copyright (c) 2021 uranum

num = int(input("数字を入力してください :"))
print("変数numは", num, "です")

if num < 5:  # num < 5がTrueのときに実行されます
    print("変数numは5より小さいです")
elif num < 10:  # num < 5 がFalseかつ num < 10 がTrueのときに実行されます
    print("変数numは5より小さくありません")
    print("変数numは10より小さいです")
elif num < 15:  # num < 5, num < 10 がFalseかつ num < 15 がTrueのときに実行されます
    print("変数numは10より小さくありません")
    print("変数numは15より小さいです")
else:  # 全ての条件がFalseのときに実行されます
    print("変数numは15より小さくありません")
