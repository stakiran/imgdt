# imgdt
デジカメの画像ファイル名を `DSCNXXXX.JPG` → `YYMMDD_HHMMSS.JPG` に変換する Python スクリ。

<!-- toc -->
- [imgdt](#imgdt)
  - [Overview](#overview)
  - [Requirement](#requirement)
  - [How to use](#how-to-use)
  - [FAQ](#faq)
    - [Q: 撮影日付はどうやって取得している？](#q-撮影日付はどうやって取得している)
  - [License](#license)
  - [Author](#author)

## Overview
デジカメで撮影した「画像ファイル名」を「撮影時刻の日付時刻文字列名」に変換する Python スクリ。

画像ファイルたちがファイル名で時系列に並ぶようになるので管理・整理しやすくなる。

## Requirement
- Windows 7+
- Python 3(動作確認は3.6で実施)

## How to use
変換したい画像ファイルを適当なフォルダに置き、imgdt.py もそこに置いてから `python imgdt.py` を実行する。

```
$ dir
2018/01/10  20:20           774,204 DSCN5346.JPG
2018/01/13  16:53           865,041 DSCN5349.JPG
2018/01/13  17:26           870,276 DSCN5354.JPG
2018/01/13  17:26           828,614 DSCN5355.JPG
2018/01/13  17:26           841,007 DSCN5356.JPG

$ python imgdt.dt
DSCN5346.JPG -> 180110_202024.JPG
DSCN5349.JPG -> 180113_165358.JPG
DSCN5354.JPG -> 180113_172610.JPG
DSCN5355.JPG -> 180113_172618.JPG
DSCN5356.JPG -> 180113_172630.JPG
5 items, do rename?
>y
fin.

$ dir
2018/01/10  20:20           774,204 180110_202024.JPG
2018/01/13  16:53           865,041 180113_165358.JPG
2018/01/13  17:26           870,276 180113_172610.JPG
2018/01/13  17:26           828,614 180113_172618.JPG
2018/01/13  17:26           841,007 180113_172630.JPG
```

## FAQ

### Q: 撮影日付はどうやって取得している？
Ans: ファイルの最終修正時間＝撮影した日付、とみなし、 `os.stat(ファイルパス).st_mtime`  で取得しています。

## License
[MIT License](LICENSE)

## Author
[stakiran](https://github.com/stakiran)
