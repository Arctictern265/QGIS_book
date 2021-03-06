﻿## 特殊なレイヤを追加する
### OpenLayersプラグインからの追加
メニュー【プラグイン】→【プラグインの管理とインストール】からOpenLayers Pluginが入っていることを確認してください。無い場合は追加を行います。

![OpenLayersPluginの確認](./img/appendix1-6-1.png).

追加後に、【Web】→【Openlayers plugin】を選択すると図のようなドロップダウンリストが開きます。

![OpenLayersPluginメニュー](./img/appendix1-6-2.png).

Google, OpenStreetMap, Yahoo, Bing(MicroSoft), Appleが提供するマップを使用することが出来ます。
下図は、【Google Maps】→【GooglePhisical】を読み込んでみた例です。

![GooglePhisicalの表示例](./img/appendix1-6-3.png).

### WMSサーバからの追加

農研機構の公開するWMSサーバーを例に、地図データを取得して初期レイヤーとしてセットしてみましょう。

http://www.finds.jp/wsdocs/kibanwms/index.html.ja

![農研機構 基盤地図WMS](./img/appendix1-6-4.png).

画面中段にある、ご使用ガイドをクリックしてください。

![ご使用ガイドの確認](./img/appendix1-6-5.png).

画面上段にある、

- http://www.finds.jp/ws/kiban25000wms.cgi?
- http://www.finds.jp/ws/kiban2500wms.cgi?

という2つのアドレスが確認できます。今回は上の方のアドレスを使ってみましょう。
QGISのメニューから【レイヤ】→【WMS/WMTSレイヤの追加】を選択します。
![WMS/WMTSレイヤの追加メニュー](./img/appendix1-6-6.png).

![WMS/WMTSレイヤの追加](./img/appendix1-6-7.png).

WM(T)Sサーバーからレイヤを追加というウィンドウが開くので、『新規』ボタンをクリックしてください。新しいWMSコネクションの作成ウィンドウが開いたら、以下のように記入してください。

![新しいWMSコネクションの作成](./img/appendix1-6-8.png).

新しいWMSコネクションの作成ウィンドウの右下の『OK』をクリックすると、以下のようなWM(T)Sサーバーからレイヤを追加というウィンドウが開くので、追加したいレイヤを選択してクリックしてください。その後、ウィンドウ内右下の『追加(A)』ボタンをクリックしてください。今回はIDの欄が0をクリックして追加します。

![WM(T)Sサーバーからレイヤを追加](./img/appendix1-6-9.png).

下図のように表示されることを確認してください。

![WMSレイヤのQGISへの表示例](./img/appendix1-6-10.png).
