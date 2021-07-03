# Copyright (c) 2021 uranum

v = 0
for i in range(10):  # 外側のループは10回繰り返されます
    for j in range(21):  # 内側のループは21回繰り返されます
        if v == 0:  # vが0のときに実行されます
            print("*", end="")  # アスタリスクを表示します
            v = 1  # 1を代入します
        elif v == 1:  # vが1のときに実行されます
            print("-", end="")  # マイナスを表示します
            v = 0  # 0を代入します
    print()  # 改行します
