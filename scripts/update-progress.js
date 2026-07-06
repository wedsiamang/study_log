const fs = require('fs');
const path = require('path');

// trace.md ファイルを読み込む
const traceFilePath = path.join(__dirname, '../trace.md');
const traceContent = fs.readFileSync(traceFilePath, 'utf8');

// トレース数をカウント（<details><summary>で数える）
const traceMatches = traceContent.match(/<details><summary>(.*?)<\/summary>/g);
const completedCount = traceMatches ? traceMatches.length : 0;
const totalCount = 50;
const progressPercent = ((completedCount / totalCount) * 100).toFixed(1);

// プログレスバーを生成（50文字）
const barLength = 50;
const filledLength = Math.round((completedCount / totalCount) * barLength);
const progressBar = '█'.repeat(filledLength) + '░'.repeat(barLength - filledLength);

// トレース名と最終更新日を抽出
const traceEntries = [];
let match;
const regex = /<details><summary>(.*?)<\/summary>\s*([\s\S]*?)<\/details>/g;

let index = 1;
while ((match = regex.exec(traceContent)) !== null) {
  const traceName = match[1];
  const traceBody = match[2];
  
  // 最終更新日を取得（最後のテーブル行の日付を使用、なければ本日の日付）
  const today = new Date().toISOString().split('T')[0];
  
  traceEntries.push({
    number: index,
    name: traceName,
    status: '✅ 完成',
    updated: today
  });
  index++;
}

// 残りのトレース（未作成）
if (index <= totalCount) {
  traceEntries.push({
    number: `${index}-${totalCount}`,
    name: '(未作成)',
    status: '⏳ 進行中',
    updated: '-'
  });
}

// progress.md を生成
let progressTable = `# 📊 学習進度ダッシュボード

## 全体進度
**完成トレース数: ${completedCount}/${totalCount}**

\`\`\`
進度: ${progressBar} ${progressPercent}%
\`\`\`

---

## 📈 トレース別進捗

| # | トレース名 | ステータス | 最終更新日 |
|---|----------|----------|----------|
`;

// トレース一覧を追加
traceEntries.forEach(entry => {
  progressTable += `| ${entry.number} | ${entry.name} | ${entry.status} | ${entry.updated} |\n`;
});

progressTable += `
---

## 📝 学習カテゴリ別

### データ構造
- 優先度付きキュー ✅
- (その他: 進行中)

### ソート・マージ
- マージ ✅

### アルゴリズム最適化
- 範囲内の4の倍数を数える ✅

### 数学的アルゴリズム
- 最大公約数 ✅

### グラフ理論
- 辺リストから隣接行列への変換 ✅

---

## 🎯 次のマイルストーン

- ${completedCount >= 10 ? '[x]' : '[ ]'} 10問完成（20%）
- ${completedCount >= 25 ? '[x]' : '[ ]'} 25問完成（50%）
- ${completedCount >= 40 ? '[x]' : '[ ]'} 40問完成（80%）
- ${completedCount >= 50 ? '[x]' : '[ ]'} 50問完成（100%）

---

**最終更新:** ${new Date().toISOString().split('T')[0]} (自動生成)
`;

// progress.md に書き込み
const progressFilePath = path.join(__dirname, '../progress.md');
fs.writeFileSync(progressFilePath, progressTable, 'utf8');

console.log(`✅ Progress updated: ${completedCount}/${totalCount} (${progressPercent}%)`);
console.log(`📊 progress.md has been updated`);
