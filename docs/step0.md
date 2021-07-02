# step 0

## Pythonの環境構築 (Windows10)

### Pythonのインストール

まず、Pythonのインストールについて解説します  
以下のリンクから公式サイトにアクセスして下さい  
  
[Python公式サイト](https://www.python.org)  
  
画面上部の「Downloads」にカーソルを合わせると下の画像の様なメニューが表示されます  
表示されたメニューの左側にある「Python 3.9.6」と書かれたボタンをクリックして下さい  
最新バージョンのPythonのインストーラーがダウンロードされます  
(数字は異なる場合があります)  
  
![Python公式サイト ダウンロード](images/python/01.png)  
  
次にダウンロードしたファイルを起動してください  
以下の画像の様なウィンドウが表示されるので「Add Python 3.9 to PATH」にチェックを入れて「Install Now」クリックして下さい  
  
![Pythonインストールウィザード](images/python/02.png)  
  
インストールが始まります
  
![Pythonインストールウィザード](images/python/03.png)  
  
終了したら「Close」をクリックしてください  

![Pythonインストールウィザード](images/python/04.png)  

最後にPythonがインストールされているか確認します  
タスクバー左下の検索アイコンをクリックして、「cmd」と入力して下さい  
  
![pythonインストール確認 cmd](images/python/05.png)  
  
「開く」をクリックしてコマンドプロンプトを起動して下さい  
以下のコマンドを入力して下さい  

```
python -V
```

インストールが成功していれば以下の画像の様にバージョンが表示されます  
  
![pythonインストール確認 cmd](images/python/06.png)  


### VSCodeのインストール

次にVSCodeのインストールについて解説します  
VSCode (Visual Studio Code)とは、マイクロソフトが無料で提供している軽量なコードエディタのことです  
今回はこれを使ってコードを書いていきます  
以下のリンクからVSCodeの公式サイトにアクセスしてください  

[VSCode公式サイト](https://code.visualstudio.com)  

画面の「Download for Windows」をクリックしてください  
VSCodeのインストーラがダウンロードされます  

![VSCode 公式サイト Download](images/vscode/01.png)  

次にダウンロードしたファイルを起動してください  
以下の画像の様なウィンドウが表示されるので使用許諾契約書を読み、「同意する」にチェックを入れて「次へ」をクリックして下さい  
  
![VSCode インストールウィザード 使用許諾契約書](images/vscode/02.png)  
  
次にインストール先を変えることができるウィンドウになりますが、特に変える必要がないので「次へ」をクリックして下さい  

![VSCode インストールウィザード インストール先](images/vscode/03.png)

次にスタートメニューフォルダを変えることができるウィンドウになりますが、これも特に変える必要がないので「次へ」をクリックして下さい  

![VSCode インストールウィザード スタートメニューフォルダ](images/vscode/04.png)

次に追加タスクを選択できるウィンドウになります  
全てのチェックボックスにチェックを入れ、「次へ」をクリックして下さい  

![VSCode インストールウィザード 追加タスク](images/vscode/05.png)

次に今までの設定の確認を行う画面になるので「次へ」をクリックして下さい  

![VSCode インストールウィザード 確認](images/vscode/06.png)

インストールが始まります  

![VSCode インストールウィザード インストール中](images/vscode/07.png)

終了したら「完了」をクリックしてください  

![VSCode インストールウィザード 完了](images/vscode/08.png)

以下のようなウィンドウが開いたらインストール成功です  

![VSCode ウインドウ](images/vscode/09.png)

### VSCode日本語化
VSCodeを日本語化する方法について解説します  
まず左のメニュー欄から「Extensions(拡張機能)」を選択して、検索欄に「japanese」と入力して下さい  
一番上に出てくる「Japanese Language Pack for Visual Studio Code」を選択して「Install」をクリックして下さい  

![VSCode 拡張機能 検索](images/vscode/10.png)

インストールが終わると右下にホップアップが現れ、「Restart」というボタンがあるのでクリックして下さい  

![VSCode 拡張機能 Restart](images/vscode/11.png)

もう一回VSCodeが起動するので、以下のように日本語になっていたらインストールは成功です  

![VSCode 日本語化後](images/vscode/12.png)

### Python拡張機能
インストールの方法は「Japanese Language Pack for Visual Studio Code」と同じです  
左のメニューから拡張機能を選択し、検索欄に「python」と入力して下さい  
一番上に出てくる「Python」を選択し「Install」をクリックして下さい  

![VSCode 拡張機能 Python](images/vscode/13.png)

インストールに成功すると以下の様な画面になります  

![VSCode Python インストール後](images/vscode/14.png)

## プログラムの書き方

### ソースファイルの作成
デスクトップにフォルダーを作成します  
例として、フォルダー名は「programs」とします  
  
![フォルダ作成](images/newproject/01.png)  
  
![フォルダ](images/newproject/02.png)  
  
VSCodeからフォルダーを開きます  
左上の「ファイル」を選択して、「フォルダーを開く」をクリックして下さい  
  
![ファイル](images/newproject/03.png)
  
![フォルダ](images/newproject/04.png)
  
デスクトップから作成したフォルダーを選択して開いてください  
以下のような表示が出た時は、「はい、作成者を信頼します」をクリックして下さい  
  
![信頼](images/newproject/05.png)
  
フォルダー名の右にカーソルを合わせて「新しいファイル」を選択し、ファイルを作成して下さい  

![新規ファイル作成](images/newproject/06.png)

例として、ファイル名は「sample.py」とし、中身は以下のようにします  
   
```python
# sample.py
print("Hello World")

```

### プログラムの実行

右上の実行ボタンをクリックしてプログラムを実行します  

![実行](images/newproject/07.png)

またはターミナルに、以下のように入力して実行します  
ターミナルは Ctrl + Shift + @で出すことができます  

```
pyhton ./sample.py
```
  
![実行](images/newproject/08.png)
