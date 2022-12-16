# callme [hard]
わからんことがあったらなんでも聞いてね！

もしもし．．．

ヒント？．．`pwntools`とか`objdump`とか`return address`とか．．もっと聞きたい？

## Write up
main関数の`return address`をオーバーフローを利用して書き換え，任意の関数を呼ぶ問題．
関数が`return`した時に何が起きているのかわかれば何をすべきかわかる．
`pwntools`の使い方をしっていないとちょっと苦戦したかもしれない．
他と比べると難しいのでhard


工事中