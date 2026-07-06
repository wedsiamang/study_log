# 📚 学習進度自動化セットアップガイド

## 概要

このリポジトリは、アルゴリズムトレース学習の進度を**自動でカウント・可視化**するシステムを備えています。

- 🎯 **全50問のアルゴリズムトレース**を学習
- 📊 **進度を自動で追跡**（GitHub Actions）
- 📈 **progress.md に自動更新**

---

## 🔧 セットアップ

### 前提条件

- GitHub リポジトリが作成済み
- `.github/workflows/` ディレクトリ作成済み
- Node.js 18以上（ローカル実行時）

### インストール手順

#### 1. ファイル配置

以下のファイルが配置されていることを確認してください：

```
study_log/
├── .github/
│   └── workflows/
│       └── update-progress.yml       # GitHub Actions ワークフロー
├── scripts/
│   └── update-progress.js             # 進度カウント・更新スクリプト
├── trace.md                           # アルゴリズムトレース集
├── progress.md                        # 進度ダッシュボード（自動生成）
├── README.md                          # リポジトリ説明
└── SETUP.md                           # このファイル
```

#### 2. ローカルでテスト実行

```bash
# Node.js スクリプトを実行
node scripts/update-progress.js
```

実行後、`progress.md` が更新されていることを確認します。

#### 3. GitHub Actions の有効化

1. リポジトリの **Settings** を開く
2. **Actions** → **General** を選択
3. **Allow all actions and reusable workflows** を選択
4. **Save** をクリック

#### 4. 権限設定

ワークフローが push できるよう、以下を設定：

1. **Settings** → **Actions** → **General**
2. **Workflow permissions** → **Read and write permissions** を選択
3. **Allow GitHub Actions to create and approve pull requests** にチェック
4. **Save** をクリック

---

## 🚀 使用方法

### トレース追加時の流れ

1. **trace.md** に新しいトレースを追加

```markdown
<details><summary>新しいアルゴリズム名</summary>

| # | トレース | ... |
|---|---------|-----|
| 1 | ... | ... |

</details>
```

2. **コミット＆プッシュ**

```bash
git add trace.md
git commit -m "Add algorithm trace"
git push
```

3. **自動実行**

- GitHub Actions が自動で起動
- `scripts/update-progress.js` が実行される
- `progress.md` が自動更新される
- 進度が自動にコミット・プッシュされる

---

## 📊 進度ダッシュボード（progress.md）の見方

### 表示内容

```
進度: ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 10.0%
```

- **完成トレース数**: 現在の完成数と目標数（例: 5/50）
- **進度バー**: ビジュアル表示（50文字）
- **進度率**: パーセンテージ

### テーブル内容

| 列 | 説明 |
|---|-----|
| # | トレース番号 |
| トレース名 | `<details><summary>` の内容 |
| ステータス | ✅ 完成 / ⏳ 進行中 |
| 最終更新日 | 最後に更新された日付 |

---

## 🔍 スクリプト詳細（update-progress.js）

### 処理フロー

1. **trace.md を読み込む**
2. **`<details><summary>` をカウント** → 完成トレース数
3. **進度率を計算** → (完成数 / 50) × 100
4. **プログレスバーを生成** → 50文字表示
5. **progress.md を生成**
6. **ファイルに書き込み**

### カスタマイズ

総トレース数を変更する場合：

```javascript
const totalCount = 50;  // この値を変更
```

---

## 🐛 トラブルシューティング

### GitHub Actions が実行されない

**確認事項：**

- ✅ `.github/workflows/update-progress.yml` が存在するか
- ✅ ワークフローの権限が正しく設定されているか
- ✅ `trace.md` への変更がコミットされているか

**解決方法：**

1. リポジトリの **Actions** タブを開く
2. 実行履歴を確認
3. ログを見てエラーを確認

### progress.md が更新されない

**確認事項：**

- ✅ Node.js スクリプトが正しく実行されているか
- ✅ `trace.md` の形式が正しいか（`<details><summary>` で囲まれているか）

**デバッグ：**

```bash
# ローカルでテスト実行
node scripts/update-progress.js

# 結果を確認
cat progress.md
```

---

## 📈 進度目標

| マイルストーン | 問題数 | 進度率 |
|-------------|-------|-------|
| 初期段階 | 5/50 | 10% ✅ |
| 入門完了 | 10/50 | 20% |
| 中級開始 | 25/50 | 50% |
| 中級完了 | 40/50 | 80% |
| **完全習得** | **50/50** | **100%** |

---

## 📝 ファイル説明

### `.github/workflows/update-progress.yml`

GitHub Actions の設定ファイル。

- **トリガー**: `trace.md` が変更されたときに自動実行
- **実行環境**: Ubuntu Latest
- **処理**: Node.js スクリプトを実行 → progress.md を更新 → コミット・プッシュ

### `scripts/update-progress.js`

進度カウント・ダッシュボード生成スクリプト。

- `trace.md` を解析
- トレース数をカウント
- progress.md を自動生成

### `progress.md`

学習進度ダッシュボード（自動生成・自動更新）。

- 全体進度表示
- トレース一覧
- カテゴリ別分類
- マイルストーン管理

---

## 🎓 学習カテゴリ

現在のトレースは以下のカテゴリに分類されています：

- **データ構造**: 優先度付きキュー
- **ソート・マージ**: マージ
- **アルゴリズム最適化**: 範囲内の4の倍数を数える
- **数学的アルゴリズム**: 最大公約数
- **グラフ理論**: 辺リストから隣接行列への変換

---

## 💡 Tips

### 効率的な学習法

1. 1日1つのトレースを完成させる
2. `trace.md` に追加してコミット
3. 進度が自動更新される（GitHub Actions）
4. `progress.md` で成長を可視化

### カスタマイズ例

**スクリプトで別の情報も追跡したい場合：**

```javascript
// update-progress.js を編集
// トレース数以外の指標を追加
```

**進度バーのスタイルを変更したい場合：**

```javascript
const progressBar = '🟩'.repeat(filledLength) + '⬜'.repeat(barLength - filledLength);
```

---

## ❓ よくある質問

**Q: 50問はどこから来た？**

A: 基本情報技術者試験の想定学習量です。必要に応じてカスタマイズ可能。

**Q: トレース名を変更したら？**

A: `trace.md` の `<summary>` 内容を変更するだけで、次回実行時に自動更新されます。

**Q: ローカルでもスクリプトを実行できる？**

A: はい。`node scripts/update-progress.js` で実行可能です。

---

## 🔗 関連リンク

- [trace.md](/trace.md) - アルゴリズムトレース集
- [progress.md](/progress.md) - 学習進度ダッシュボード
- [GitHub Actions ドキュメント](https://docs.github.com/en/actions)
- [基本情報技術者試験](https://www.ipa.go.jp/shiken/kubun/fe.html)

---

**最終更新**: 2026-07-06
