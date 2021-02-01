## 電卓アプリ
スクリプト共有用プロジェクト。
python3 で動作確認済み。

# インストール
```
git clone https://github.com/atsushi0507/calculator.git
```

# 初めに
いくつかのライブラリは事前に準備する必要あり。
LSM.pyで必要なライブラリ:
```
numpy, matplotlib
```
インストール方法:
```
pip3 install numpy matplotlib
```

# 最小二乗法
データの回帰直線を求める:
```
y = ax + b
```
の形で直線を得られる。
データ点と最小二乗法で求めた直線をプロットできる。
今はデータをコードに直書きしているが、コマンドラインから与えて配列に詰めるように拡張することも可能。
エラーバーの付け方(基本):
![error](img/error.pdf)
-y (--yes)オプションで、ルートの中身のn-1をnへ切り替え可能。

実行方法:
```
python3 LSM.py
```