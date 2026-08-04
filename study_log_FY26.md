#### study_log (FY26)
----

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

