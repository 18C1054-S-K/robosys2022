# robosys2022

## plus.py
![plus_test](https://github.com/18C1054-S-K/robosys2022/actions/workflows/plus_test.yml/badge.svg)  
引数として与えた数の和を標準出力で表示します
#### コマンド
```
python3 plus.py <引数1> <引数2> ... <引数n>
```
または
```
./plus.py <引数1> <引数2> ... <引数n>
```

#### 使用例
```
./plus.py 1 2 3
```
結果
```
6
```

## aas.py
アスキーアートを表示、読み込みするための関数、クラスが定義されています  
単独では機能しません

## dice.py
![dice_test](https://github.com/18C1054-S-K/robosys2022/actions/workflows/dice_test.yml/badge.svg)  
サイコロを振り、出た目と和を標準出力で表示します  
1つ目の引数は振るサイコロの個数です  
10以下の自然数を与えてください  
2つ目の引数は乱数発生器を初期化する際に用いるシード値です  
シード値を与えなかった場合、現在時刻が用いられます
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

## 参考


## 著作権
MITライセンス  
(同ディレクトリ内にある)LICENSEをお読みください  
このパッケージのコードは、下記のスライド(CC-BY-SA 4.0 by Ryuichi Ueda)のものを、本人の許可を得て自身の著作としたものです
[ryuichiueda/my_slides_robosys_2022](https://github.com/ryuichiueda/my_slides_robosys_2022)

