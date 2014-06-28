#地図情報のオープンデータ可視化［実践］入門

## 1. [地理空間情報とオープンデータの概要](https://github.com/Arctictern265/QGIS_book/blob/master/1/1.md)

###  a. 地理空間情報とは
 * i. [身近な地理空間情報](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-1-1.md "身近な地理空間情報")
 * ii. [情報は位置に結びつく](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-1-2.md)
 * iii. [位置の表現の仕方](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-1-3.md)
 * (Column) [同じ経度緯度でも位置が違う？-測地系の違い](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-1-column1.md)
 * iv. [さまざまな投影法](https://github.com/Arctictern265/QGIS_book/commit/4e017c3a18745f0066f48dd90a84d824636606d8)
 * (Column) [空間参照系](https://github.com/Arctictern265/QGIS_book/commit/12713251451820375fe8ae656035ecea8ff9d857)
 * v. [住所から位置を求める](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-1-5.md)
 * vi. [可視化することで理解が進む](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-1-6.md)

### b. オープンデータとは

 * i. [オープンデータの定義](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-2-1.md)
 * (Column) [ライセンスを理解しよう](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-2-column1.md)
 * ii. [オープンデータを巡る動き](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-2-2.md)
 * iii. [公共のデータだけがオープンデータ？](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-2-3.md)

### c. いまなぜ注目されているのか

 * i. [測位技術の充実](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-3-1.md)
 * (Column) [GPSの仕組み](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-3-column1.md)
 * ii. [オープンソースソフトウェアの充実](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-3-2.md)
 * (Column) [OSGeo財団](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-3-column2.md)
 * iii. [活用に不可欠な情報](https://github.com/Arctictern265/QGIS_book/blob/master/1/1-3-3.md)

## 2. [データを準備する](https://github.com/Arctictern265/QGIS_book/blob/master/2/2.md)

### a. オープンデータを使う

 * i. [データを探す](https://github.com/Arctictern265/QGIS_book/blob/master/2/2-1-1.md) #巻末のカタログへの誘導
 * ii. [カタログサイトの利用](https://github.com/Arctictern265/QGIS_book/blob/master/2/2-1-2.md) #data.go.jpの紹介？

### b. 代表的なフォーマット

 * i. [csv](https://github.com/Arctictern265/QGIS_book/blob/master/2/2-2-1.md)
 * ii. [xml](https://github.com/Arctictern265/QGIS_book/blob/master/2/2-2-2.md)
 * iii. [ESRI Shapefile](https://github.com/Arctictern265/QGIS_book/blob/master/2/2-2-3.md)
 * iv. GeoJSON
 * v. [KML](https://github.com/Arctictern265/QGIS_book/blob/master/2/2-2-5.md)
 * vi. 位置情報付きの画像
 * vii. [標高値データもしくはグリッドデータ](https://github.com/Arctictern265/QGIS_book/blob/master/2/2-2-7.md)
 * viii. 配信地図(オープンストリートマップ、地理院地図)
 * (Column) タイル地図

### c. ライセンス

 * i. 見ておくべきところ
 * ii. クリエイティブ・コモンズ
 * iii. パブリックドメイン
 * (Column) 測量成果の複製・使用

## 3. [基本となる地図を準備する](https://github.com/Arctictern265/QGIS_book/blob/master/3/3-1.md)

### a. 身近な地図を作成する #基盤地図情報を利用するイメージ

 * i. 使用にあたり確認すべき項目
 * ii. データをダウンロードする
 * iii. 一般的なフォーマットへ変換する
 * iv. ファイルを開く
 * v. レイヤ毎にスタイルを設定
 * vi. 保存しておく

### b. もう少し広い範囲を準備する #地理院地図、もしくはオープンストリートマップを利用するイメージ

 * i. プラグインを使用する
 * ii. オープンストリートマップを表示する
 * iii. 地理院地図を表示する
 * iv. 保存しておく

### c. 世界地図を作成する #Natural Earthを利用するイメージ

 * i. データをダウンロードする
 * ii. ファイルを開く
 * iii. レイヤ毎にスタイルを設定
 * iv. 保存しておく

## 4. テーマを決めてデータを可視化する

### a. 防災地図を作成する

 * i. データをダウンロードする #国土数値情報から防災系のデータ
 * ii. 面要素のスタイル
 * iii. 線要素のスタイル
 * iv. 点要素のスタイル
 * v. 保存する

### b. 年齢別人口分布図を作成する

 * i. データをダウンロードする #e-statから国勢調査データ
 * ii. ファイルを開く
 * iii. 小地域データに統計データを結びつける
 * iv. 人口により色分け
 * v. 選択したレイヤを出力する
 * vi. 保存する
 * (Column) 地域メッシュコードとは？ - 2050年の人口予想図を作成する

### c. 山岳表現を作成する

 * i. データをダウンロードする
  * i. 日本の範囲内の場合 #基盤地図情報から数値標高モデル
  * ii. 世界中のデータを扱いたい場合 #topography from global 30 arcsecond grid
 * (Column) 10mメッシュは10mではない？
 * ii. グリッドデータへ加工する
 * iii. 陰影を作成する
 * iv. 標高毎に色分け
 * v. 選択したレイヤを出力する
 * vi. 保存する
 * (Column) 標高タイル

### d. その他様々な可視化例

 * i. 保育所が必要な場所を可視化する
 * ii. 植生データを可視化する
 * iii. 海水水温を可視化する
 * iv. カッパの生息適地を可視化する

## 5. データを出力する

### a. 印刷する

 * i. プリントコンポーザ
 * ii. 地図を配置する
 * iii. タイトルを配置する
 * iv. スケールを配置する
 * v. 方位を配置する
 * vi. 凡例を配置する
 * vii. 出力する
 * viii. 地図帳機能を利用する

### b. Webで公開する

 * i. 利用されやすい公開方法
  * i. 利用者を想定する
  * ii. ライセンスを決定する
  * iii. フォーマットを決定する
 * ii. 画像データで公開する
 * (Column) 画像に位置を結ぶつける - ジオリファレンス
 * iii. ベクトルデータで公開する
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
 * f. 新規レイヤを作成する
 * g. [ファイルをレイヤに追加する](https://github.com/Arctictern265/QGIS_book/blob/master/appendix1/appendix1-7.md)
 * h. [レイヤにスタイルを設定する](https://github.com/Arctictern265/QGIS_book/blob/master/appendix1/appendix1-8.md)
 * i. [レイヤを編集する](https://github.com/Arctictern265/QGIS_book/blob/master/appendix1/appendix1-9.md)
 * j. レイヤを保存する
 * k. [ベクタ演算例](https://github.com/Arctictern265/QGIS_book/blob/master/appendix1/appendix1-11.md)
 * l. ラスタ演算例
 * m. 印刷する

## Appendix Ⅱ:データカタログ #表でざっと載せる

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