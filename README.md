# なんこれ
iBusのON/OFFにしたがってカーソルの色を変えます<br/>
デフォルトでは、OFFで水色、ONでピンクになります<br/>
1秒毎にIMEの状態を確認しているので、<br/>
ON/OFを切り替えてから実際にカーソルの色が変わるまで若干の遅延があります

# 必要な物
python<br/>
iBus<br/>
bash（これ以外でも大丈夫かも）<br/>
GNOME Terminal（これ以外でも大丈夫かも）

# 使い方
（ホームディレクトリにcloneした場合で書きます）
以下の行を.bashrcに追加してから

~/CursorColorToggler/change_cursor_color.sh &

次のコマンドを実行

$ cd ~/CursorColorToggler<br/>
$ chmod u+x toggle_cursor_color.py toggle_cursor_color.sh <br/>
$ source ~/.bashrc

