# Copyright (c) 2021 uranum

num = int(input("数字を入力してください :"))
print("変数numは", num, "です")

if num > 5 and num < 10:  # num > 5 がTrueかつ num < 10 がTrueのときに実行されます
    print("変数numは5より大きく10より小さいです")

if num == 5 or num == 10:  # num == 5 がTrueまたは num == 10 がTrueのときに実行されます
    print("変数numは5または10に等しいです")

if not num < 10:  # num < 10 がTrueではないときに実行されます
    print("変数numは10より小さくありません")
