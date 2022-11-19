# robosys2022

## 概要
2つのpythonコード(足し算をするpush.pyとサイコロを振るdice.py)を含みます。  
ロボットシステム学の課題で作成したリポジトリです。

## 動作環境
Ubuntu20.04  
python3.7~3.10

## plus.py
![plus_test](https://github.com/18C1054-S-K/robosys2022/actions/workflows/plus_test.yml/badge.svg)  
標準入力で与えた数の和を標準出力で表示します。
#### コマンド
```
python3 plus.py
```
または
```
./plus.py
```

#### 使用例
```
seq 3 | ./plus.py
```
結果
```
6
```

ただし、```seq 3```は1から3までの数を標準出力で表示するコマンドです。

## dice.py
![dice_test](https://github.com/18C1054-S-K/robosys2022/actions/workflows/dice_test.yml/badge.svg)  
サイコロを振り、出た目と和を標準出力で表示します。  
1つ目の引数は振るサイコロの個数です。  
10以下の自然数を与えてください。  
2つ目の引数は乱数発生器を初期化する際に用いるシード値です。  
シード値を与えなかった場合、現在時刻が用いられます。
#### コマンド
```
python3 dice.py <サイコロの数> <シード値(なくても可)>
```
または
```
./dice.py <サイコロの数> <シード値(なくても可)>
```
#### 使用例
```
./dice.py 3 5
```
結果
```
+-------+   +-------+   +-------+
| O   O |   |     O |   | O   O |
|   O   |   |   O   |   | O   O |
| O   O |   | O     |   | O   O |
+-------+   +-------+   +-------+

sum: 14
```

### 補足
dice.pyはサイコロを表示するためにaas.pyから関数等をimportしています。

## その他ファイル、ディレクトリについて

| 名前 | 概要 |
|:-:|:-|
| aas | AA(アスキーアート)が列記されたtxtファイルと対応するymlファイルが入っています。 |
| txts4test | テストで用いる文字列が書かれたtxtファイルが入っています。 |
| *_test.bash | テスト用のシェルスクリプトです。 |
| aas.py | AAを扱うための関数、クラスが定義されています。単独では機能しません。 |
| aas_test.py | ![aas_test](https://github.com/18C1054-S-K/robosys2022/actions/workflows/aas_test.yml/badge.svg)実行するとaas内から第1引数で指定された名前のtxt、ymlファイルを読み込み、そこに書かれたAAとその情報(幅など)を標準出力で表示します。aas.pyが正常に機能しているかテストするのが目的のコードです。 |
| show_robosys.py | ![show_robosys_test](https://github.com/18C1054-S-K/robosys2022/actions/workflows/aas_test.yml/badge.svg)実行すると"robosys2022"と書かれたAAを標準出力で表示します。上に同じくaas.pyが正常に機能しているかテストするのが目的のコードです。 |


## 参考
* pythonファイルを書く際に参考にしました。
  * [note.nkmk.me](https://note.nkmk.me/python/)
  * [python 公式ドキュメント](https://docs.python.org/ja/3/library/index.html)
* README.mdを書く際に参考にしました。
  * [Qiita Markdown記法一覧](https://qiita.com/oreo/items/82183bfbaac69971917f)
* シェルスクリプトを書く際に参考にしました。
  * [Qiita diffでコマンドの出力の結果を直接比較する。](https://qiita.com/wingedtw/items/2f05c5d0c37d71f209f4)


## ライセンスについて
MITライセンス  
(同ディレクトリ内にある)LICENSEをお読みください。

## 著作権について
このパッケージのコードは、下記のスライド(CC-BY-SA 4.0 by Ryuichi Ueda)のものを、本人の許可を得て自身の著作としたものです。  
[ryuichiueda/my_slides_robosys_2022](https://github.com/ryuichiueda/my_slides_robosys_2022)

