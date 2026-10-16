# ---------------------------------------------------------------------------------------------- 
# 
# プログラム概要 ： mjscli：Mjaiクライアント
# バージョン     ： 0.0.0.0.5(オリ判断：期待値実装)
# プログラム名   ： bot.py
# 処理概要       ： mjai.app通信用スクリプト
# Ver0.0.0作成日 ： 2026/09/21 17:09:46
# 最終更新日     ： 2026/10/17 00:32:18
# 
# Copyright (c) 2010-2026 TechMileStoraJP, All rights reserved.
# 
# ---------------------------------------------------------------------------------------------- 

import sys
import mjsmodule as mjs

# プレーヤIDの定義
ply_id = int(sys.argv[1])
ret = mjs.init(ply_id)

# メイン処理
while True:
  # resは行末に改行が必要
  res = sys.stdin.readline().strip() + "\n"
  # メッセージが改行のみならば
  if res == "\n":
    break
  # メッセージが存在するならば
  else:
    # reactの返り値sndには改行が含まれている
    snd = mjs.react(res)
    sys.stdout.write(snd)
    sys.stdout.flush()
# 処理ここまで
