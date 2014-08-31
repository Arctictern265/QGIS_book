##WMS/WFS
WMS(Web Map Service)とWFS(Web Feature Service)はOpen Geospatial Consortiumにより定められたインターネッ越に地図データをやり取りするための規約です。WMSでは地図画像データを、WFSは図形データを配信することが出来ます。  
WMSを例にとると、まずクライアント側からどのような地図サービスを提供しているかサーバに対して問い合わせを行います。

*GetCapabilitiesリクエスト例*
    http://サーバのURL?request=GetCapabilities&service=WMS&version=1.0.0

サーバからはxmlにて提供しているサービスの情報が返答されます。次に取得した情報から判断して、適当な地図画像の取得を行います。

*GetMapリクエスト例*
    http://サーバのURL?service=WMS&version=1.0.0&request=GetMap&取得範囲やレイヤの指定が並ぶ・・・

QGISではWMSをサポートしていますので、公開されているWMSサーバのURLさえわかれば、サーバへ接続して画像を取得することができます。サーバ側になる多くのWebGISでもこの仕組みをサポートしています。  

例として、基盤地図情報２万５千分の１WMS配信サービス（http://www.finds.jp/ws/kiban25000wms.cgi?）に以下のようなURIパラメータを付与してリクエストを送信してみます。

*基盤地図情報２万５千分の１WMS配信サービスへのリクエスト例*

	http://www.finds.jp/ws/kiban25000wms.cgi?request=GetCapabilities&service=WMS&version=1.0.0

これに対するレスポンスは以下のようなXMLです。この中には利用可能なレイヤー、フォーマット等の全体の情報と、各レイヤーの範囲や空間参照系などの必要な情報が格納されています。クライアント側はこのXMLレスポンスを解析して、レイヤーリスト等の情報をユーザに提示することができます。

*GetCapabilities返答例*

	<!--  end of DOCTYPE declaration  -->
	<WMT_MS_Capabilities version="1.0.0">
	<!--
	 MapServer version 6.4.1 OUTPUT=GIF OUTPUT=PNG OUTPUT=JPEG SUPPORTS=PROJ SUPPORTS=GD SUPPORTS=AGG SUPPORTS=FREETYPE SUPPORTS=CAIRO SUPPORTS=ICONV SUPPORTS=WMS_SERVER SUPPORTS=WMS_CLIENT SUPPORTS=WFS_SERVER SUPPORTS=WFS_CLIENT SUPPORTS=WCS_SERVER SUPPORTS=SOS_SERVER SUPPORTS=GEOS INPUT=JPEG INPUT=POSTGIS INPUT=OGR INPUT=GDAL INPUT=SHAPEFILE 
	-->
	<Service>
		<Name>GetMap</Name>
		<Title>KIBAN 25000 WMS</Title>
		<OnlineResource>http://www.finds.jp/ws/kiban25000wms.cgi?</OnlineResource>
	</Service>
	<Capability>
		<Request>
			<Map>
				<Format>
					<GIF/>
					<PNG/>
					<JPEG/>
					<SVG/>
				</Format>
				<DCPType>
					<HTTP>
						<Get onlineResource="http://www.finds.jp/ws/kiban25000wms.cgi?"/>
						<Post onlineResource="http://www.finds.jp/ws/kiban25000wms.cgi?"/>
					</HTTP>
				</DCPType>
			</Map>

	・・・中略・・・

		<Layer>
			<Name>KIBAN25000</Name>
			<Title>KIBAN 25000 WMS</Title>
			<Abstract>KIBAN25000</Abstract>
			<SRS>
				EPSG:4612 EPSG:2443 EPSG:2444 EPSG:2445 EPSG:2446 EPSG:2447 EPSG:2448 EPSG:2449 EPSG:2450 EPSG:2451 EPSG:2452 EPSG:2453 EPSG:2454 EPSG:2455 EPSG:2456 EPSG:2457 EPSG:2458 EPSG:2459 EPSG:2460 EPSG:2461 EPSG:3097 EPSG:3098 EPSG:3099 EPSG:3100 EPSG:3101 EPSG:4019 EPSG:4326 EPSG:32651 EPSG:32652 EPSG:32653 EPSG:32654 EPSG:32655 EPSG:32656 EPSG:4301 EPSG:30161 EPSG:30162 EPSG:30163 EPSG:30164 EPSG:30165 EPSG:30166 EPSG:30167 EPSG:30168 EPSG:30169 EPSG:30170 EPSG:30171 EPSG:30172 EPSG:30173 EPSG:30174 EPSG:30175 EPSG:30176 EPSG:30177 EPSG:30178 EPSG:30179 EPSG:3091 EPSG:3092 EPSG:3093 EPSG:3094 EPSG:3095 EPSG:3096 EPSG:900913 EPSG:3857
			</SRS>
			<LatLonBoundingBox minx="122" miny="22" maxx="149" maxy="46"/>
			<BoundingBox SRS="EPSG:4612" minx="122" miny="22" maxx="149" maxy="46"/>
			<Layer queryable="0">
				<Name>AdmArea</Name>
				<Title>AdmArea</Title>
				<SRS>EPSG:4612</SRS>
				<LatLonBoundingBox minx="122" miny="22" maxx="149" maxy="46"/>
				<BoundingBox SRS="EPSG:4612" minx="122" miny="22" maxx="149" maxy="46"/>
				<ScaleHint min="0" max="748.354272644456"/>
			</Layer>

	・・・以下略・・・

データの公開に際して、

  * クライアント側での加工を前提としない
  * ファイル公開では容量が大きい

といった場合には、こういった仕組みも検討してみてください。