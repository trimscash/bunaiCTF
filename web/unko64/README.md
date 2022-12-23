# unko64 [easy]
trimscash君がくそウェブサイトを作ったって自慢してきたよ．でもなんか余計な機能がついてるなぁ．．
http://192.168.1.80:30010
## writeup
```
/finder/?filename=./flag
```

にアクセスするとunko64エンコードされたものが出てくるのでそれをデコードするとフラグが出てくる．

```
bunaiCTF{FL4SK_1S_USEFUL}
```