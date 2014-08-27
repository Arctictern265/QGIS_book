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
 * viii. [タイル地図](https://github.com/Arctictern265/QGIS_book/blob/master/2/2-2-8.md)
 * (Column) [オープンストリートマップ](https://github.com/Arctictern265/QGIS_book/blob/master/2/2-2-column1.md)

### c. ライセンス

 * i. [見ておくべきところ](https://github.com/Arctictern265/QGIS_book/blob/master/2/2-3-1.md)
 * ii. [クリエイティブ・コモンズ](https://github.com/Arctictern265/QGIS_book/blob/master/2/2-3-2.md)
 * iii. [パブリックドメイン](https://github.com/Arctictern265/QGIS_book/blob/b905b9f17a9056898cd487348017472f9987908e/2/2-3-3.md)
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
  * ii. 投影法を変換する
  * iii. ラスタデータに変換する
  * (Column)GDAL -- Geospatial Data Abstraction Library --
  * iv. 距離を計算する
 * ii. 植生データから畑地面積率図を作成する
  * i. データをダウンロードする
  * ii. 畑地を抽出する
  * iii. ラスタデータに変換する
  * iii. 畑地面積率を計算する
  * (Column)プロセッシングツール
 * iii. 標高データから日射量図を作成する
  * i. 投影法を変換する
  * ii. 傾斜、傾斜方位を計算する
  * iii. 日射量を計算する
 * iv. データを組み合わせて新たな図を作成する
  * i. ラスタデータを組み合わせる
  * (Column)統計モデル
  * ii. ラスタデータとベクタデータを組み合わせる 
  * (Column)オープンソースとしてのQGIS

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
 * (Column) [githubにGeoJSONデータを保存する](https://github.com/Arctictern265/QGIS_book/blob/master/5/5-3-column3.md)
 * iii. [ベクトルデータで公開する(->github pagesようにリポジトリをeditするへ変更)](https://github.com/Arctictern265/QGIS_book/blob/master/5/5-2.md)
 * (Column) [WMS/WFS](https://github.com/Arctictern265/QGIS_book/blob/master/5/5-2-column1.md)
 * (Column) [Mapbox](https://github.com/Arctictern265/QGIS_book/blob/master/5/5-2-column2.md)

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
 * g'. [特殊なレイヤを追加する](https://github.com/Arctictern265/QGIS_book/blob/master/appendix1/appendix1-6-2.md)
 * h. [レイヤにスタイルを設定する](https://github.com/Arctictern265/QGIS_book/blob/master/appendix1/appendix1-8.md)
 * i. [レイヤを編集する](https://github.com/Arctictern265/QGIS_book/blob/master/appendix1/appendix1-9.md)
 * j.  [レイヤを保存する](https://github.com/Arctictern265/QGIS_book/blob/master/appendix1/appendix1-10.md)
 * k. [ベクタ演算例](https://github.com/Arctictern265/QGIS_book/blob/master/appendix1/appendix1-11.md)
 * l. [ラスタ演算例](https://github.com/Arctictern265/QGIS_book/blob/master/appendix1/appendix1-12.md)
 * m. [印刷する](https://github.com/Arctictern265/QGIS_book/blob/master/appendix1/appendix1-13.md)

## Appendix Ⅱ:[データカタログ](https://github.com/Arctictern265/QGIS_book/blob/master/appendix2/appendix2.md)

### a. [国の機関から入手できる情報](https://github.com/Arctictern265/QGIS_book/blob/master/appendix2/appendix2-1.md)
 * i. 基盤地図情報
 * ii. 国土数値情報
 * iii. 自然環境情報GIS提供システム
 * iv. e-stat

### b. [地方自治体から入手できる情報](https://github.com/Arctictern265/QGIS_book/blob/master/appendix2/appendix2-2.md)

 * i. 都道府県
  * 福井県
  * 岐阜県
  * 静岡県
  * 愛知県
  * 兵庫県
  * 鳥取県
 * ii. 市町村
  * 北海道室蘭市
  * 岩手県陸前高田市
  * 宮城県大崎市
  * 秋田県横手市
  * 福島県会津若松市
  * 群馬県前橋市
  * 埼玉県さいたま市
  * 埼玉県和光市
  * 埼玉県南埼玉郡宮代町
  * 千葉県千葉市
  * 千葉県流山市
  * 東京都板橋区
  * 東京都八王子市
  * 神奈川県横浜市
  * 神奈川県横浜市金沢区
  * 神奈川県川崎市
  * 神奈川県相模原市
  * 神奈川県横須賀市
  * 神奈川県藤沢市
  * 神奈川県大和市
  * 新潟県三条市
  * 新潟県糸魚川市
  * 石川県金沢市
  * 石川県野々市市
  * 石川県河北郡内灘町
  * 福井県福井市
  * 福井県敦賀市
  * 福井県鯖江市
  * 福井県越前市
  * 福井県坂井市
  * 福井県吉田郡永平寺町
  * 長野県須坂市
  * 岐阜県大垣市
  * 静岡県三島市
  * 静岡県裾野市
  * 静岡県御前崎市
  * 愛知県名古屋市
  * 滋賀県大津市
  * 大阪府大阪市
  * 奈良県葛城市
  * 島根県松江市
  * 岡山県玉野市
  * 福岡県福岡市
  * 佐賀県武雄市

### c. [国外のデータ](https://github.com/Arctictern265/QGIS_book/blob/master/appendix2/appendix2-3.md)

 * i. Natural Earth
 * ii. 地球地図
 * iii. Landsat衛星画像
 * iv. VIIRS（Visible Infrared Imaging Radiometer Suite）衛星画像
 * v. SRTM（Shuttle Radar Topography Mission） 
