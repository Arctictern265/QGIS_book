##WMS/WFS
WMS(Web Map Service)とWFS(Web Feature Service)はOpen Geospatial Consortiumにより定められたインターネッ越に地図データをやり取りするための規約です。WMSでは地図画像データを、WFSは図形データを配信することが出来ます。  
WMSを例にとると、まずクライアント側からどのような地図サービスを提供しているかサーバに対して問い合わせを行います。

    http://サーバのURL?service=wms&version=1.1.1&request=GetCapabilities

サーバからはxmlにて提供しているサービスの情報が返答されます。次に取得した情報から判断して、適当な地図画像の取得を行います。

    http://サーバのURL?service=wms&version=1.1.1&request=GetMap&取得範囲やレイヤの指定が並ぶ・・・

QGISではWMSをサポートしていますので、公開されているWMSサーバのURLさえわかれば、サーバへ接続して画像を取得することができます。サーバ側になる多くのWebGISでもこの仕組みをサポートしています。  
データの公開に際して、
  * クライアント側での加工を前提としない
  * ファイル公開では容量が大きい
といった場合には、こういった仕組みも検討してみてください。