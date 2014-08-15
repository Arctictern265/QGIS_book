#地図情報のオープンデータ可視化［実践］入門

## 全ページ

## 1. [地理空間情報とオープンデータの概要](https://github.com/Arctictern265/QGIS_book/blob/master/1/1.md)

###  a. 地理空間情報とは
 * i. [身近な地理空間情報](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-1-1.md "身近な地理空間情報")
 * ii. [情報は位置に結びつく](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-1-2.md)
 * iii. [位置の表現の仕方](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-1-3.md)
 * (Column) [同じ経度緯度でも位置が違う？-測地系の違い](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-1-column1.md)
 * iv. [さまざまな投影法](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-1-4.md)
 * (Column) [空間参照系](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-1-column2.md)
 * v. [住所から位置を求める](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-1-5.md)
 * vi. [可視化することで理解が進む](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-1-6.md)

### b. オープンデータとは

 * i. [オープンデータの定義](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-2-1.md)
 * (Column) [5スターオープンデータ](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-2-column2.md)
 * (Column) [ライセンスを理解しよう](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-2-column1.md)
 * ii. [オープンデータを巡る動き](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-2-2.md)
 * iii. [公共のデータだけがオープンデータ？](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-2-3.md)

### c. いまなぜ注目されているのか

 * i. [測位技術の充実](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-3-1.md)
 * (Column) [GPSの仕組み](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-3-column1.md)
 * ii. [オープンソースソフトウェアの充実](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-3-2.md)
 * (Column) [OSGeo財団](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-3-column2.md)
 * iii. [位置情報利用への期待と課題](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-3-3.md)

## 2. [データを準備する](https://github.com/Arctictern265/QGIS_book/blob/master/2/2.md)

### a. オープンデータを使う

 * i. [データを探す](https://github.com/Arctictern265/QGIS_book/blob/master/2/2-1-1.md)
 * ii. [カタログサイトの利用](https://github.com/Arctictern265/QGIS_book/blob/master/2/2-1-2.md)

### b. 代表的なフォーマット

 * i. [csv](https://github.com/Arctictern265/QGIS_book/blob/master/2/2-2-1.md)
 * ii. [xml](https://github.com/Arctictern265/QGIS_book/blob/master/2/2-2-2.md)
 * iii. [ESRI Shapefile](https://github.com/Arctictern265/QGIS_book/blob/master/2/2-2-3.md)
 * iv. [GeoJSON](https://github.com/Arctictern265/QGIS_book/blob/master/2/2-2-4.md)
 * v. [KML](https://github.com/Arctictern265/QGIS_book/blob/master/2/2-2-5.md)
 * vi. [位置情報付きの画像](https://github.com/Arctictern265/QGIS_book/blob/master/2/2-2-6.md)
 * vii. [標高値データもしくはグリッドデータ](https://github.com/Arctictern265/QGIS_book/blob/master/2/2-2-7.md)
 * viii. [配信地図(オープンストリートマップ、地理院地図)](https://github.com/Arctictern265/QGIS_book/blob/master/2/2-2-8.md)
 * (Column) [タイル地図](https://github.com/Arctictern265/QGIS_book/blob/master/2/2-2-column1.md)

### c. ライセンス

 * i. [見ておくべきところ](https://github.com/Arctictern265/QGIS_book/blob/master/2/2-3-1.md)
 * ii. [クリエイティブ・コモンズ](https://github.com/Arctictern265/QGIS_book/blob/master/2/2-3-2.md)
 * iii. パブリックドメイン
 * (Column) [測量成果の複製・使用](https://github.com/Arctictern265/QGIS_book/blob/master/2/2-3-column1.md)

## 3. [基本となる地図を準備する](https://github.com/Arctictern265/QGIS_book/blob/master/3/3.md)

### a. [身近な地図を作成する](https://github.com/Arctictern265/QGIS_book/blob/master/3/3-1.md)


 * i. 使用にあたり確認すべき項目
 * ii. データをダウンロードする
 * iii. 一般的なフォーマットへ変換する
 * iv. ファイルを開く
 * v. レイヤ毎にスタイルを設定
 * vi. 保存しておく

### b. [もう少し広い範囲を準備する](https://github.com/Arctictern265/QGIS_book/master/3/3-2.md)

 * i. [プラグインを使用する](https://github.com/Arctictern265/QGIS_book/blob/master/3/3-2.md)
 * ii. [オープンストリートマップを表示する](https://github.com/Arctictern265/QGIS_book/blob/master/3/3-2.md)
 * iii. [地理院地図を表示する](https://github.com/Arctictern265/QGIS_book/blob/master/3/3-2.md)
 * iv. [保存しておく](https://github.com/Arctictern265/QGIS_book/blob/master/3/3-2.md)

### c. [世界地図を作成する](https://github.com/Arctictern265/QGIS_book/master/3/3-3.md)

 * i. データをダウンロードする
 * ii. ファイルを開く
 * iii. レイヤ毎にスタイルを設定
 * iv. 保存しておく

## 4. [テーマを決めてデータを可視化する](https://github.com/Arctictern265/QGIS_book/blob/master/4/4.md)

### a. [防災地図を作成する](https://github.com/Arctictern265/QGIS_book/blob/master/4/4-1.md)

 * [i. データをダウンロードする #国土数値情報から防災系のデータ](https://github.com/Arctictern265/QGIS_book/blob/master/4/4-1.md)
 * [ii. 点要素のスタイル](https://github.com/Arctictern265/QGIS_book/blob/master/4/4-1.md)
 * [iii. 線要素のスタイル](https://github.com/Arctictern265/QGIS_book/blob/master/4/4-1.md)
 * [iv. 面要素のスタイル](https://github.com/Arctictern265/QGIS_book/blob/master/4/4-1.md)
 * [v. 保存する](https://github.com/Arctictern265/QGIS_book/blob/master/4/4-1.md)

### b. [年齢別人口分布図を作成する](https://github.com/Arctictern265/QGIS_book/blob/master/4/4-2.md)

 * i. データをダウンロードする
 * ii. ファイルを開く
 * iii. 小地域データに統計データを結びつける
 * iv. 人口により色分け
 * v. 選択したレイヤを出力する
 * vi. 保存する
 * (Column) [標準地域メッシュコードとは？ - 2050年の人口予想図を作成する](https://github.com/Arctictern265/QGIS_book/blob/master/4/4-2-column1.md)

### c. [山岳表現を作成する](https://github.com/Arctictern265/QGIS_book/blob/master/4/4-3.md)

 * i. 日本の範囲内の場合 #基盤地図情報から数値標高モデル
  * i. データをダウンロードする
  * (Column) 10mメッシュは10mではない？
  * ii. グリッドデータへ加工する
  * (Column) 数値標高モデルの変換ツール
  * iii. 標高ごとに色分けする
  * iv. 陰影図を作成する
  * v. 色分けした標高と陰影図を重ねる
 * ii. 世界中のデータを扱いたい場合 #ETOPO1
  * i. データをダウンロードする
  * ii. 投影法を変換する
  * iii. 標高ごとに色分けする
  * iv. 色分けした標高と陰影図を重ねる

### d. [データから新たな図を作成する](https://github.com/Arctictern265/QGIS_book/blob/master/4/4-4.md)

 * i. 河川データから河川からの距離図を作成する
  * i. データをダウンロードする
  * ii. ラスタデータに変換する
  * iii. 距離を計算する
 * ii. 標高データから日射量図を作成する
  * i. データをダウンロードする
  * ii. 傾斜、斜面方位を計算する
  * iii. 日射量を計算する
 * i. 植生データから畑地の面積割合図を作成する
  * i. データをダウンロードする
  * ii. ラスタデータに変換する
  * iii. 面積割合を計算する
 * iv. データを組み合わせて新たな図を作成する
  * i. ラスタデータを組み合わせる
  * ii. ラスタデータとベクタデータを組み合わせる 
  * (Column) 統計モデル

## 5. [データを出力する](https://github.com/Arctictern265/QGIS_book/blob/master/5/5.md)


### a. [印刷する](https://github.com/Arctictern265/QGIS_book/blob/master/5/5-1.md)

 * i. プリントコンポーザ
 * ii. コンポーザマネージャ
 * iii. 地図を配置する
 * iv. 全体図を配置する
 * v. タイトルを配置する
 * vi. スケールを配置する
 * vii. 方位を配置する
 * viii. 凡例を配置する
 * ix. その他整飾
 * x. 出力する
 * xi. 地図帳機能を利用する

### b. Webで公開する

 * i. [利用されやすい公開方法(github pagesを用いることにした)](https://github.com/Arctictern265/QGIS_book/blob/master/5/5-2.md)
  * i. [利用者を想定する(->githubアカウントの作成方法へ変更)](https://github.com/Arctictern265/QGIS_book/blob/master/5/5-2.md)
  * ii. [ライセンスを決定する(->githubリポジトリのクローンを行うへ変更)](https://github.com/Arctictern265/QGIS_book/blob/master/5/5-2.md)
  * iii. [フォーマットを決定する(->githubを利用した作業へ変更)](https://github.com/Arctictern265/QGIS_book/blob/master/5/5-2.md)
 * ii. [画像データで公開する(->githubにpushするに変更)](https://github.com/Arctictern265/QGIS_book/blob/master/5/5-2.md)
 * (Column) 画像に位置を結ぶつける - ジオリファレンス
 * iii. [ベクトルデータで公開する(->github pagesようにリポジトリをeditするへ変更)](https://github.com/Arctictern265/QGIS_book/blob/master/5/5-2.md)
 * (Column) WMS/WFS
 * (Column) Mapbox

## Appendix Ⅰ: QGIS操作ガイド

 * a. [QGISとは？](https://github.com/Arctictern265/QGIS_book/blob/master/appendix1/appendix1-1.md)
 * b. [インストール](https://github.com/Arctictern265/QGIS_book/blob/master/appendix1/appendix1-2.md)
  * i. Windows
  * ii. Mac
 * c. [プロジェクトを開く/保存する](https://github.com/Arctictern265/QGIS_book/blob/master/appendix1/appendix1-3.md)
 * d. [測地系・投影法を設定する](https://github.com/Arctictern265/QGIS_book/blob/master/appendix1/appendix1-4.md)
 * e. [プラグインを設定する](https://github.com/Arctictern265/QGIS_book/blob/master/appendix1/appendix1-5.md)
 * f. [新規レイヤを作成する](https://github.com/Arctictern265/QGIS_book/blob/master/appendix1/appendix1-6.md)
 * g. [ファイルをレイヤに追加する](https://github.com/Arctictern265/QGIS_book/blob/master/appendix1/appendix1-7.md)
 * h. [レイヤにスタイルを設定する](https://github.com/Arctictern265/QGIS_book/blob/master/appendix1/appendix1-8.md)
 * i. [レイヤを編集する](https://github.com/Arctictern265/QGIS_book/blob/master/appendix1/appendix1-9.md)
 * j. レイヤを保存する
 * k. [ベクタ演算例](https://github.com/Arctictern265/QGIS_book/blob/master/appendix1/appendix1-11.md)
 * l. [ラスタ演算例](https://github.com/Arctictern265/QGIS_book/blob/master/appendix1/appendix1-12.md)
 * m. [印刷する](https://github.com/Arctictern265/QGIS_book/blob/master/appendix1/appendix1-13.md)

## Appendix Ⅱ:データカタログ

### a. 国の機関から入手できる情報
 * i. 基盤地図情報
  * i. 入手できるデータの種類
  * ii. ライセンス
  * iii. フォーマット
 * ii. 地理院地図
  * i. 入手できるデータの種類
  * ii. ライセンス
  * iii. フォーマット
 * iii. 国土数値情報
  * i. 入手できるデータの種類
  * ii. ライセンス
  * iii. フォーマット
 * iv. 統計データ
  * i. 入手できるデータの種類
  * ii. ライセンス
  * iii. フォーマット

### b. 自治体から入手できる情報

 * i. 自治体のオープンデータ
 * ii. 代表的な例
  * i. 静岡県
  * ii. 鯖江市
  * iii. 千葉市
  * iv. 室蘭市

### c. その他の情報

 * i. 世界地図の入手(NaturalEarth?)
  * i. 入手できるデータの種類
  * ii. ライセンス
  * iii. フォーマット
 * ii. (その他、後の事例で使用するデータなどを紹介)
