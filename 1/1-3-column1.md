# GPSの仕組み

まず初めに、GPSとは現在位置を示す情報及び現在地情報を取得するための機器であると思われるくらいに、GPSという用語が一般化したような印象を受ける事が度々あります。ですが、本来的にGPSというのはアメリカが運用する人工衛星のことです。GPSはGlobal Positioning Systemの頭文字を取ったもので、全地球測位網と訳されます。実は、アメリカ以外にも各国で測位目的の衛星を所有しています。また、世界各国で位置情報の取得に用いるための電波の周波数帯が異なります。日本は準天頂衛星みちびき(QZSS)を既に打ち上げており、今後7機を追加する予定と言われています。ただし、現在は日本が独自に所有する人工衛星の数が少ないのでアメリカのGPSを借りるような形になっております。また使用する電波に関しては、アメリカと歩調を合わせるように周波数が1575.42MHzで信号名はL1C/Aを使用することにしています。

|衛星名|所有国|
|:-----|:-----|
|GPS|アメリカ|
|QZSS|日本|
|GLONASS|ロシア|
|Beidou|中国|
|Gallileo|EU|
|IRNSS|インド|

位置情報を取得するための基本原則に関しては、3次元測位を行います。

--要追記--