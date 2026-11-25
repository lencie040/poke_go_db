# poke_go_db

ポケモンGO 個体データベース（278件 / 39列）。

| ファイル | 内容 |
|---|---|
| `data.csv` | 元データ（編集するのはこれ） |
| `data.json` / `pokemon.sqlite` | `data.csv` から生成 |
| `index.html` | ブラウザで見られるビューア（検索・絞り込み・並べ替え・詳細表示）。データ埋め込み済みで、ダブルクリックで開けます |
| `template.html` | `index.html` の元テンプレート |
| `build.py` | 生成スクリプト |

## 更新方法

1. `data.csv` を編集
2. `python3 build.py` を実行
3. commit & push

## GitHub Pages で公開する場合

Settings → Pages → Branch を `main` / `(root)` にすると `index.html` がWebページとして見られます。
