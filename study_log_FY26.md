#### study_log (FY26)
----

##### 2026/08/15

<details><summary>📗FE_A 判定C+</summary>

`█████░░░░░` 56.3%　45/80問 

| 教材 | 過去問道場 |
|---|---|
|テクノロジ|48.1%|
|マネジメント|66.7%|
|ストラテジ|76.5% |

</details>

##### 2026/08/11

<details><summary>📗FE_A 判定C-</summary>

`█████░░░░░` 52.0%　26/50問 

| 教材 | 過去問道場 |
|---|---|
|テクノロジ|41.9%|
|マネジメント|75.0%|
|ストラテジ|66.7% |

</details>

<details><summary>📕 FE 科目B ・ 16問</summary>

`█████████░` 94%　15/16問 · 1時間19分

| 教材 | 大原練習問題 / 第1部 アルゴリズムの表現方法 |
|---|---|
| 分野 | 疑似言語 |
| 最長 | 疑似言語 No.8（16分） |
| 誤答 | 疑似言語 No.18 |

</details>

##### 2026/08/09

<details><summary>📗FE_A 判定C+</summary>

`█████░░░░░` 55.3%　47/85問 

| 教材 | 過去問道場 |
|---|---|
|テクノロジ|44.6%|
|マネジメント|88.9%|
|ストラテジ|70.0% |

</details>

> [!TIP]
> **About AppSheet × webhook × GitHub Actions**  
> AppSheet Automation と GitHub Actions を webhook でつなぐと、リポジトリを自動更新できるようになりました。  
> Connecting AppSheet Automation to GitHub Actions via a webhook lets me update the repo automatically.


<details><summary>AppSheetのボタン押すとリポジトリ学習ログを自動更新する / Auto-updating my study log with one button via webhook</summary>


## やりたかったこと

基本情報技術者の勉強記録を参考書毎に AppSheet で時間計測と正答率について管理していました。
Appsheetで、1日の終わりにボタンを押すと、その日の「解いた問題数・正答率・解答時間・間違えた問題」を集計して、
GitHub の Markdown に草を生やさず追記できるようにしたい。

- AppSheet
- GitHub のリポジトリ
- GitHub Actions
- PAT（Personal Access Token）

---

### オートメーションの変更

AppSheetで今日はここまでというアクションボタンを押すと、今日の日付で解いた問題が
ex:アプリオーナーである自分にメール送信され、それをリポジトリmdファイルに手動で追記していた。
now:webhookでGithubに送り、Actionsでmdファイルを自動更新

Github Actions が起動できるイベントは push / pull_request / schedule などで、
外部の出来事で起動したいときは **`repository_dispatch`** という仕組みを使う。
GitHub の API を叩いて Actions を外から起こすためのもの。

> 「AppSheet ボタン押下で GitHub の API を叩く → Actions が起きる」という流れになる。

AppSheet でCall a webhook設定

```
- HTTP Verb：`POST`
- URL：`https://api.github.com/repos/<ユーザー名>/<リポジトリ>/dispatches`
- Headers：
  - `Authorization`：`Bearer <PAT>`
  - `Accept`：`application/vnd.github+json`
- Body（JSON）：`event_type` と `client_payload` を入れる
```

Json-body例(テキストごとにbotを作ってテンプレートも書き換えるということを今はやっているが)
```
{
  "event_type": "study-log-entry",
  "client_payload": {
    "log": {
"correct": "<<COUNT(SELECT(パーフェクトラーニング技術評論社06[id],AND([1st_date]=today(),[1st_lap]=true)))>>",
      "text": "パーフェクトラーニング技術評論社06",
      "solved": "<<COUNT(SELECT(パーフェクトラーニング技術評論社06[id],AND([1st_date]=today(),ISNOTBLANK([1st_lap]))))>>",
      "chapter": "<<SELECT(パーフェクトラーニング技術評論社06[chapter],[1st_date]=today(),true)>>",
      "category": "<<SELECT(パーフェクトラーニング技術評論社06[category],[1st_date]=today(),true)>>",
      "time_total": "<<SUM(SELECT(パーフェクトラーニング技術評論社06[1st_chapter_time],[1st_date]=today()))>>",
      "rate": "<<IF(COUNT(SELECT(パーフェクトラーニング技術評論社06[id],AND([1st_date]=today(),ISNOTBLANK([1st_lap]))))=0,\"—\",TEXT(COUNT(SELECT(パーフェクトラーニング技術評論社06[id],AND([1st_date]=today(),[1st_lap]=true))) / DECIMAL(COUNT(SELECT(パーフェクトラーニング技術評論社06[id],AND([1st_date]=today(),ISNOTBLANK([1st_lap]))))) * 100))>>",
      "longest_cat": "<<SELECT(パーフェクトラーニング技術評論社06[category],AND([1st_chapter_time]=MAX(SELECT(パーフェクトラーニング技術評論社06[1st_chapter_time],[1st_date]=today())),[1st_date]=today()))>>",
      "longest_no": "<<SELECT(パーフェクトラーニング技術評論社06[no.],AND([1st_chapter_time]=MAX(SELECT(パーフェクトラーニング技術評論社06[1st_chapter_time],[1st_date]=today())),[1st_date]=today()))>>",
      "longest_time": "<<MAX(SELECT(パーフェクトラーニング技術評論社06[1st_chapter_time],[1st_date]=today()))>>",
      "wrong_cat": "<<SELECT(パーフェクトラーニング技術評論社06[category],AND([1st_lap]=false,[1st_date]=today()),true)>>",
      "wrong_no": "<<SELECT(パーフェクトラーニング技術評論社06[no.],AND([1st_lap]=false,[1st_date]=today()))>>"
    }
  }
}
```
> **AppSheetあるある**
> Header の値をそのまま書くと、AppSheet が `application/vnd.github+json` の `/` を「割り算」と解釈してエラーになる。
> AppSheet の設定欄は式として評価されるので、**固定文字列はダブルクォートで囲む**必要があった。
> `"application/vnd.github+json"` のように。

---

## 送るデータの組み立て

AppSheet は数値や文字を項目ごとにデータを送るだけ、
見た目（表やレイアウト）の組み立ては GitHub Actions 側の Python 
デザインのテンプレがリポジトリに残る
0除算は AppSheet 側で `IF(分母=0, "—", 割り算)` とガードした。

---

## 本体：GitHub Actions のワークフロー

`repository_dispatch` を受けて、Python でファイルを更新する。

```yaml
name: study-log-append

on:
  repository_dispatch:
    types: [study-log-entry]

permissions:
  contents: write

jobs:
  append:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: build and append
        run: |
          python3 scripts/add_entry.py --kind fe_b
      - name: commit and push
        run: |
          git add -A
          git commit -m "study log" || { echo "no changes"; exit 0; }
          git push origin HEAD:main
```

> `repository_dispatch` で起動するワークフローは、**YAML がデフォルトブランチ（main）に無いと発火しない**。
> あと dispatch が成功すると返ってくるのは **204 No Content**（本文が空）。
> 「反応が無い＝失敗？」と一瞬焦ったが、空が正解だった。
> なお草については別記事で書いたが、コミットの author を bot にしておけば増えない。

---

## `runs-on` と `uses` って何

ワークフロー**呪文の2行の意味**
`runs-on: ubuntu-latest` と `uses: actions/checkout@v4`。

### `runs-on`：ジョブを「どのマシンで動かすか」

`runs-on` は、そのジョブをどの実行環境（ランナー）で走らせるか

`ubuntu-latest` は、**GitHub が用意してくれる使い捨ての Linux 仮想マシン**を使う、という意味。
GitHub 側が管理してくれる（マネージドな）環境で、ジョブが終わると消える。
毎回まっさらな Ubuntu が立ち上がって、そこで自分の処理が動くイメージ。

大事だったのは、**Ubuntu になるのは自動じゃなくて、自分でそう書いたから**という点。

- `windows-latest` と書けば Windows で動く
- `macos-latest` なら Mac
- 自分のサーバーで動かす **self-hosted runner** も指定できる

> つまり「なぜ ubuntu なのか」の答えは「YAML にそう書いたから」だった。
> マネージドの Linux を使うか、Windows/Mac を使うか、自前マシンを使うか、を選ぶ場所。
> 「latest」は最新の用意された Ubuntu バージョンを使う、の意味。

### `uses`：他人が作った部品（アクション）を呼ぶ

`uses: actions/checkout@v4` の方は、**既製の部品を呼び出す命令**だった。

Actions では、よく使う処理が「アクション」という再利用可能な部品として公開されている。
`uses` はそれを「使う」宣言。

`actions/checkout@v4` を分解する

- `actions/checkout` … リポジトリのコードをランナーに持ってくる公式アクション
- `@v4` … そのバージョン（タグ）

このアクションが無いと、まっさらな Ubuntu にはリポジトリのファイルが無いので、
`python3 scripts/add_entry.py` を実行しようとしてもスクリプトが見つからない。
**「マシンを用意（runs-on）→ コードを持ってくる（uses: checkout）→ 自分の処理を走らせる（run）」**
という順番と分かり腑に落ちた。

> `@v4` のバージョン指定も大事で、
> `@main` みたいに動くブランチを指すと、その先が更新されると挙動が変わるらしい。
> 多くの人が固定タグ（`@v4`）で参照しているらしい。

---

## 全体の流れ

```
AppSheet のアクションボタンで発火
   │  Call a webhook（POST）
   ▼
GitHub API  /repos/…/dispatches   ← 認証は PAT（ここで 401/403/404 の世界）
   │  repository_dispatch イベント
   ▼
GitHub Actions（main の YAML が受ける）
   │  runs-on: ubuntu-latest でマシンを用意
   │  uses: checkout でコードを取得
   │  Python で Markdown を組み立てて追記
   ▼
bot 名義でコミット & push
```

---

## つまずきメモ（自分用）

- **401 Bad credentials**：PAT が空だった / 二重に貼っていた。`echo "${#PAT}"` で文字数を見ると気づける。fine-grained PAT は `github_pat_` で始まって90文字前後。
- **Header の `/` がエラー**：AppSheet の Header は式評価される。値をダブルクォートで囲む。
- **204 が返る**：成功。空レスポンスが正常。
- **YAML がデフォルトブランチに無いと起動しない**：`repository_dispatch` の仕様。
- **`runs-on` は環境の選択**：ubuntu は自動じゃなく指定。Windows/Mac/self-hosted も選べる。
- **`uses` は既製アクションの呼び出し**：`checkout` が無いとコードが手元に来ない。`@v4` はバージョン固定。
- **push が rejected（non-fast-forward）**：bot が自動 push した後、手元が古くなると起きる。`git pull` してから push すれば解ける。
- **フォルダを2箇所に clone していた**：同名フォルダが2つあり「直したのに反映されない」を繰り返した。clone は1箇所に。作業前に `pwd` を見る癖。

---

# English version

## What I wanted

I'd been tracking my exam study (time spent and accuracy, per textbook) in AppSheet.
At the end of the day I press an action button, and I wanted that day's stats
— questions solved, accuracy, time, and mistakes — appended to a Markdown file on GitHub,
**without growing grass** (the green squares on my contribution graph).

- AppSheet
- a GitHub repo
- GitHub Actions
- a PAT (Personal Access Token)

---

### Changing the automation

Before, pressing the "done for today" action button in AppSheet emailed that day's solved
problems to me (the app owner), and I appended them to the repo's md file by hand.
Now, it sends them to GitHub via a webhook, and Actions updates the md file automatically.

The events that can start GitHub Actions are push / pull_request / schedule, etc.
To start it from something external, you use **`repository_dispatch`** —
it hits the GitHub API to wake Actions up from outside.

> So the flow is: "AppSheet button press hits the GitHub API → Actions fires."

AppSheet "Call a webhook" settings:

```
- HTTP Verb: POST
- URL: https://api.github.com/repos/<user>/<repo>/dispatches
- Headers:
  - Authorization: Bearer <PAT>
  - Accept: application/vnd.github+json
- Body (JSON): with event_type and client_payload
```

(The JSON body is the one shown in the Japanese section above. Right now I make a separate
bot and rewrite the template per textbook.)

> **A classic AppSheet gotcha.**
> If you type the header value plainly, AppSheet reads the `/` in `application/vnd.github+json`
> as division and errors out. The fields are evaluated as expressions, so you must
> **wrap literal strings in double quotes**: `"application/vnd.github+json"`.

---

## Building the payload

AppSheet just sends the numbers and text field by field;
the layout (the table) is assembled by Python inside GitHub Actions,
so the design template lives in the repo.
For divide-by-zero I guarded it on the AppSheet side with `IF(denominator=0, "—", division)`.

---

## The core: the Actions workflow

It receives `repository_dispatch` and updates the file with Python.
(The YAML is the one shown in the Japanese section above.)

> A workflow triggered by `repository_dispatch` **won't fire unless the YAML is on the default branch (main)**.
> Also, a successful dispatch returns **204 No Content** (empty body).
> "No response = failure?" I panicked for a second, but empty is correct.
> (I wrote about the grass part elsewhere; making the commit author a bot keeps it from growing.)

---

## What are `runs-on` and `uses`?

The meaning of the **two "spell" lines** in the workflow:
`runs-on: ubuntu-latest` and `uses: actions/checkout@v4`.

### `runs-on`: which machine the job runs on

`runs-on` picks **which runner (execution environment)** the job runs on.

`ubuntu-latest` means **use a disposable Linux VM that GitHub provides** —
a managed environment GitHub spins up and throws away when the job ends.
A fresh Ubuntu boots each time, and my steps run there.

The key point: **it's Ubuntu because I wrote it, not automatically.**

- `windows-latest` runs on Windows
- `macos-latest` on Mac
- a **self-hosted runner** lets you use your own server

> So "why Ubuntu?" answers to "because the YAML says so."
> It's where you choose managed Linux vs Windows/Mac vs your own machine.
> "latest" means the newest provided Ubuntu version.

### `uses`: calling a ready-made part (an action)

`uses: actions/checkout@v4` **calls a ready-made part**.

In Actions, common tasks are published as reusable "actions." `uses` declares you use one.

- `actions/checkout` … the official action that brings your repo's code onto the runner
- `@v4` … its version (tag)

Without it, the fresh Ubuntu has none of my files, so `python3 scripts/add_entry.py`
can't find the script. The order finally clicked:
**provision a machine (`runs-on`) → fetch the code (`uses: checkout`) → run my steps (`run`)**.

> The `@v4` pin matters too. Pointing at a moving branch like `@main` can change behavior
> when it updates, so most people reference a fixed tag (`@v4`).

---

## The whole flow

```
AppSheet action button fires
   │  Call a webhook (POST)
   ▼
GitHub API  /repos/…/dispatches   ← auth is the PAT (the 401/403/404 world)
   │  repository_dispatch event
   ▼
GitHub Actions (the YAML on main receives it)
   │  runs-on: ubuntu-latest provisions a machine
   │  uses: checkout fetches the code
   │  Python builds the Markdown and appends
   ▼
commit & push as bot
```

---

## Trap notes (for future me)

- **401 Bad credentials**: the PAT was empty / pasted twice. `echo "${#PAT}"` reveals it. A fine-grained PAT starts with `github_pat_` and is ~90 chars.
- **`/` in header errors**: AppSheet headers are evaluated as expressions. Wrap values in double quotes.
- **204 returned**: success. Empty response is normal.
- **Won't fire unless YAML is on the default branch**: `repository_dispatch` spec.
- **`runs-on` is an environment choice**: Ubuntu isn't automatic; you can pick Windows/Mac/self-hosted.
- **`uses` calls a ready-made action**: without `checkout`, your code isn't on the runner. `@v4` pins the version.
- **push rejected (non-fast-forward)**: after the bot auto-pushes, your local falls behind. `git pull` then push.
- **Cloned into two folders**: same-named folder in two places → "I fixed it but nothing changed," repeatedly. Keep one clone. Check `pwd` before working.

</details>

##### 2026/08/06 · FE 科目B

<details><summary>📕 FE 科目B ・ 6問</summary>

`███████░░░` 67%　4/6問 · 47分

| 教材 | パーフェクトラーニング技術評論社06 / 3_対策問題①_B |
|---|---|
| 分野 | アルゴリズム |
| 最長 | アルゴリズム No.5（16分） |
| 誤答 | アルゴリズム No.5 , 7 |

</details>

##### 2026/08/04 · FE 科目B

<details><summary>📕 FE 科目B ・ 18問</summary>

`█████████░` 89%　16/18問 · 1時間23分

| 教材 | 確認テスト / 2_サンプル問題_B |
|---|---|
| 分野 | アルゴリズム, セキュリティ |
| 最長 | アルゴリズム No.9（7分） |
| 誤答 | アルゴリズム No.16, 17 |

</details>

##### 📅 2026/08/04

<details><summary>FE_B</summary>

📗 基本情報テキスト：パーフェクトラーニング技術評論社06  
✏️ 解いた問題数：18問  
🔢 2_サンプル問題_B  
🎨 カテゴリー：アルゴリズム , セキュリティ  
🕰️ 解答時間合計：-613656:56:09  
⭕️ 正答率：88.89%  
⚠️ 最長解答問題：【アルゴリズム】No.9 ／ 00:07:00  
❌ 間違えた問題：【アルゴリズム , セキュリティ】No.16 , 17

</details>

##### 📅 2026/08/03

<details><summary>FE_B</summary>

📗 基本情報テキスト：パーフェクトラーニング技術評論社06  
✏️ 解いた問題数：2問  
🔢 2_サンプル問題_B  
🎨 カテゴリー：アルゴリズム  
🕰️ 解答時間合計：00:00:52  
⭕️ 正答率：100.00%  
⚠️ 最長解答問題：【アルゴリズム】No.1 ／ 00:00:50  
❌ 間違えた問題：【】No.

</details>

##### 📅 2026/08/02 

<details><summary>FE_A</summary>

- 大原科目A: 57%
  - テクノロジ
    - ユーザーインタフェース 9/12
    - マルチメディア 14/20
    - ネットワーク 38/77

</details>

> [!TIP]
> **About Contribution graph**.  
> ローカルからGithub未登録メールアドレスの user でコミットするとそのリポジトリには草が生えないことを知りました。  
> Committing locally with an unregistered email address will keep your work off the
> contribution graph (no green squares / grass).

<details><summary>リポジトリの雑草除去作業メモ / Removing grass from a Markdown-only repo</summary>

 学習ログを日々 md で更新するだけで GitHub の草（contribution graph）が増えるのが嫌なので、
 ブランチを変えるなど試したがうまくいかなかった。
 過去に生えた草も消して、リポジトリを main 一本に統一した作業記録。

### 0. 前提

すでにローカルに clone 済みであること。無ければ clone する。

```bash
git clone https://github.com/wedsiamang/study_log.git
cd study_log
```

### 1. このリポジトリだけ未登録メールに設定

```bash
git config user.email "studylog@local.invalid"
git config user.name  "studylog"
git config user.email   # => studylog@local.invalid を確認
```

`--global` は付けない。付けると草を残したい他リポジトリまで無効化される。
リポジトリローカル設定は `.git/config` に保存され、このリポジトリ内でのみ有効。
`.invalid` は実在しないよう予約された TLD なので、登録済みメールと衝突する事故が起きない。

### 2.（一度きり）散らばったブランチを main に統一

ブランチにしか無いデータが無いか確認する。

```bash
git fetch --all --prune
git branch -a
git log --oneline main..origin/studyLogs   # main に無い＝救出候補
```

ブランチにしか無いファイルを main へ取り込む（今回は trace.md が1件多かった）。

```bash
git checkout origin/studyLogs -- trace.md   # "--" の後にスペース。file だけ差し替え
git add trace.md
git commit -m "recover: merge trace into main"
git show main:trace.md | grep -c '<summary>'   # 件数が揃ったか確認
```

### 3. 履歴を書き換える前にバックアップ

```bash
cd ~
cp -r study_log study_log_backup_20260802
cd ~/study_log
```

`cp -r` = copy recursively（フォルダごと複製）。`cd` と打ち間違えないこと。

### 4. 過去の草を消す：全履歴のメールを書き換え

```bash
brew install git-filter-repo   # 未インストールなら

git filter-repo --email-callback 'return b"studylog@local.invalid"'
```

全コミットの author/committer メールが未登録アドレスに置き換わり、集計から外れる。
**必ず1行で、開き `'` と閉じ `'` をペアで**打つ（閉じ忘れると `quote>` で待ち状態になる）。
コールバックに**登録メールを入れない**こと。入れると逆に全部が自分の草に塗り替わる。

### 5. remote を付け直して force-push

filter-repo は安全のため origin を外す。付け直してから main を上書きする。

```bash
git remote -v
git remote add origin https://github.com/wedsiamang/study_log.git   # origin が消えていたら
git push origin main --force
```

force-push は取り消せない上書き。他端末に clone があれば、それは clone し直しになる。
反映（草が消える）は最大24時間。

### 6. 不要ブランチを削除

```bash
git push origin --delete studyLogs
git push origin --delete test
```

### 7. 今後の更新フロー

Web エディタは使わず、ローカルで編集 → commit → push。

```bash
code .                              # VS Code で開く
# study_log.md / trace.md を編集して保存 (Cmd+S)
git add study_log.md trace.md
git commit -m "log: 2026/08/02"
git push
git log -1 --format='%an <%ae>'     # studylog <studylog@local.invalid> を確認
```

author が `studylog@local.invalid` になっていれば、そのコミットは草に載らない。

### メモ

- progress.md を自動更新する Actions は bot（actions-user）名義なので、元々あなたの草には無関係。そのまま動かしてよい。
- 「今後だけ草を止めたい／過去の緑は残したい」場合は、手順4〜5（filter-repo と force-push）を省略し、手順1と7だけ行う。

### 参考

- GitHub Docs — *Profile contributions reference* / *Troubleshooting missing contributions*（草の判定条件：default ブランチ＋メール紐づけ）
- GitHub Docs — *Viewing a project's contributors*（非デフォルトブランチ・未紐づけメールは集計外）
- RFC 2606（`.invalid` は予約 TLD で実在しない）
- `git filter-repo` 公式ドキュメント（履歴書き換え）

---

 I didn't want my contribution graph filling up just from updating a Markdown study log
 every day. I tried things like switching branches, but they didn't work out.
 This is a record of erasing the grass that had already grown and consolidating the
 repo onto a single `main` branch.

### 0. Prerequisite

The repo is already cloned locally. If not, clone it first.

```bash
git clone https://github.com/wedsiamang/study_log.git
cd study_log
```

### 1. Set an unregistered email (repo-local only)

```bash
git config user.email "studylog@local.invalid"
git config user.name  "studylog"
git config user.email   # => verify it shows studylog@local.invalid
```

Do **not** use `--global`, or you'll also kill the grass on repos you *want* green.
Repo-local config is saved in `.git/config` and applies only inside this repo.
`.invalid` is a reserved, never-real TLD, so it can never collide with a registered address.

### 2. One-time: consolidate stray branches into main

Check whether any data exists *only* on a side branch.

```bash
git fetch --all --prune
git branch -a
git log --oneline main..origin/studyLogs   # commits not on main = candidates to recover
```

Pull the branch-only file into main (here `trace.md` had one extra entry).

```bash
git checkout origin/studyLogs -- trace.md   # space after "--"; swaps only that file
git add trace.md
git commit -m "recover: merge trace into main"
git show main:trace.md | grep -c '<summary>'   # confirm the count matches
```

### 3. Back up before rewriting history

```bash
cd ~
cp -r study_log study_log_backup_20260802
cd ~/study_log
```

`cp -r` copies the folder recursively. Don't type `cd` by mistake.

### 4. Erase past grass: rewrite all commit emails

```bash
brew install git-filter-repo   # if not installed

git filter-repo --email-callback 'return b"studylog@local.invalid"'
```

Every commit's author/committer email is replaced with the unregistered one, dropping it
from the graph. Type it **on one line with matching quotes** (a missing closing `'` leaves
you stuck at `quote>`). **Never** put a *registered* email in the callback, or you'd repaint
the entire history as your own grass.

### 5. Re-add remote and force-push

filter-repo removes `origin` for safety. Re-add it, then overwrite `main`.

```bash
git remote -v
git remote add origin https://github.com/wedsiamang/study_log.git   # if origin is gone
git push origin main --force
```

Force-push is an irreversible overwrite. Any other clone must be re-cloned.
The graph can take up to 24 hours to update.

### 6. Delete unused branches

```bash
git push origin --delete studyLogs
git push origin --delete test
```

### 7. Daily workflow from now on

Stop using the web editor. Edit locally, then commit and push.

```bash
code .                              # open in VS Code
# edit and save study_log.md / trace.md (Cmd+S)
git add study_log.md trace.md
git commit -m "log: 2026/08/02"
git push
git log -1 --format='%an <%ae>'     # verify studylog <studylog@local.invalid>
```

If the author shows `studylog@local.invalid`, that commit won't appear on your graph.

### Notes

- The Action that updates `progress.md` commits as a bot (`actions-user`), so it never counted toward your grass. Leave it running.
- To stop future grass but keep past green, skip steps 4–5 (filter-repo and force-push) and do only steps 1 and 7.

### References

- GitHub Docs — *Profile contributions reference* / *Troubleshooting missing contributions* (criteria: default branch + linked email)
- GitHub Docs — *Viewing a project's contributors* (non-default branches / unlinked emails are excluded)
- RFC 2606 (`.invalid` is a reserved, non-existent TLD)
- `git filter-repo` official docs (history rewriting)

</details>

##### 📅 2026/08/01.   

<details><summary>FE_B</summary>

📗　基本情報テキスト：パーフェクトラーニング技術評論社06.    
✏️　解いた問題数：20問.    
🔢　1_令和5年度_B.   
🎨　カテゴリー：アルゴリズム , セキュリティ.   
🕰️　解答時間合計：02:42:15.    
⭕️　正答率：100.00%.   
⚠️　最長解答問題：【アルゴリズム】No.16　／　00:38:02.   
❌　間違えた問題：【】No.     
Sent from AppSheet.   

</details>

##### 📅 ~2026/07/27

<details><summary>develop</summary>

- spring-boot slackbotをAIで学習開発
    - [RoomBooking_slack_bot](https://github.com/wedsiamang/RoomBooking_slack_bot/tree/main)
        -  Slack WF Builder からのフォーム送信データをspring-bootでh2dbのデータと照合し、ルールに添い判定結果をスレッドに返信する申請系bot

</details>

##### 📅 2026/07/14

<details><summary>FE_A_B</summary>

- FE_演習
    - | FE旧午後 H29秋問1(セキュリティ) |  40% | 30分 
    - | trace | R7年　問5 | 理論度数 | 30分 
    - | FE_A | 大原問題集 | ストラテジ |  15問 40%  

</details>

##### 📅 2026/07/13

<details><summary>FE_A_B</summary>

- FE_演習
    - | FE旧午後 H30春問1(セキュリティ) |  80% | 30分 
    - | trace | サンプル2　問5 | 文字の連接確率(バイグラム) | 40分 
    - | FE_A | 大原問題集 | マネジメント |  50問 74%  

</details>

##### 📅 2026/07/09  

<details><summary>FE_A_B</summary>

- FE_演習
    - | FE旧午後 R1秋問1(セキュリティ) |  75% | 20分 
    - | trace | サンプル　問6 | ビット列の反転 | 70分 
    - | FE_A | 過去問道場 |  10問  

</details>

##### 📅 2026/07/08  

<details><summary>FE_A_B</summary>

- FE_演習
    - | FE旧午後 H28春問1(セキュリティ) |  60% | 30分 
    - | trace | 令和5年　問1 | 素数列挙 | 90分 
    - | FE_A | 過去問道場 |  20問  

</details>

##### 📅 2026/07/07  

<details><summary>FE_A_B</summary>

- FE_演習
    - | FE旧午後 H21春問4(セキュリティ) |  50% | 30分 
    - | trace | 令和6年　問2 | 2進数文字列から10進数への変換 | 25分 
    - | FE_A | 過去問道場 |  50問  

</details>

##### 📅 2026/07/06  

<details><summary>FE_A_B</summary>

- FE_演習
    - | FE旧午後 H26秋問1(セキュリティ) | 5/5 (100%) | 50分 
    - | trace | 令和6年　問3 | 隣接行列 | 20分 
    - | FE_A | 過去問道場 |  50問  

</details>

