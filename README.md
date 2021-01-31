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
データの近似直線を求める。
今はデータをコードに直書きしているが、コマンドラインから与えて配列に詰めるように拡張することも可能。
データ点と最小二乗法で求めた直線をプロットできる状態。
エラーバーの付け方:
![error](https://user-images.githubusercontent.com/11633979/106389729-3aa08580-6428-11eb-979e-a42a7155638a.png)

実行方法:
```
python3 LSM.py
```