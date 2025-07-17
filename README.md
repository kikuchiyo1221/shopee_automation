# Shopee Automation Toolkit

このリポジトリは Shopee OpenAPI を用いて

* 注文・商品・広告データの取得
* SQLite への保存
* 分析ダッシュボードへの供給

を行う Python プロジェクトです。

---

## 目次
1. 必要環境
2. セットアップ手順
3. .env サンプル
4. よく使うコマンド
5. TODO / 今後のロードマップ

---

## 1. 必要環境
* **Python 3.11 以上**
* Git / GitHub アカウント
* Shopee Partner Platform の認証情報（Partner ID / Partner Key / Shop ID / Access Token）

---

## 2. セットアップ手順
```bash
# 1. リポジトリをクローン
$ git clone https://github.com/<YOUR_NAME>/shopee_automation.git
$ cd shopee_automation

# 2. 仮想環境を作成
$ python -m venv .venv
$ source .venv/Scripts/activate    # ← Windows PowerShell は .\.venv\Scripts\Activate.ps1

# 3. ライブラリをインストール
(.venv)$ pip install -r requirements.txt

# 4. .env を作成し認証情報を入力
(.venv)$ cp .env.example .env
#   → テキストエディタで値を埋める

# 5. データベースを初期化
(.venv)$ python src/db.py

# 6. API 動作テスト（ショップ情報取得）
(.venv)$ python src/api.py
```

---

## 3. .env サンプル
```env
SHOPEE_PARTNER_ID=123456
SHOPEE_PARTNER_KEY=abcdefghijklmnopqrstuvwxyz
SHOPEE_SHOP_ID=987654321
SHOPEE_ACCESS_TOKEN=xxxxx
DB_URL=sqlite:///shopee.db
```

---

## 4. よく使うコマンド
| タスク | コマンド |
|--------|----------|
| 仮想環境を有効化 | `source .venv/Scripts/activate` (Windows は `Activate.ps1`) |
| ライブラリ追加 & freeze | `pip install <pkg> && pip freeze > requirements.txt` |
| DB テーブル作成 | `python src/db.py` |
| ショップ情報取得 | `python src/api.py` |

---

## 5. TODO / ロードマップ
- [ ] `api.py` に注文取得 (`get_orders`) を実装
- [ ] `db.py` に `insert_orders()` を実装し注文を保存
- [ ] GitHub Actions で毎朝データ取得
- [ ] Streamlit で KPI ダッシュボード公開

---

### ライセンス
MIT License 