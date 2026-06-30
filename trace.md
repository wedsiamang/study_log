### Trace
<details><summary>優先度付きキューの手動トレース（21ステップ）</summary>

優先度付きキュー（値が小さいほど高優先度）のスケジューラを、enqueue/dequeue で1ステップずつ追跡。

| # | トレース | 条件式 | 判定 | PrioQueue | 出力 |
|---|---|---|---|---|---|
| 1 | prioSched() |   |   |   |   |
| 2 | prioQueue:prioQueue← PrioQueue() |   |   |   |   |
| 3 | prioQueue.enqueue("A",1) |   |   | A |   |
| 4 | prioQueue.enqueue("B",2) |   |   | A,B |   |
| 5 | prioQueue.enqueue("C",2) |   |   | A,B,C |   |
| 6 | prioQueue.enqueue("D",3) |   |   | A,B,C,D |   |
| 7 | prioQueue.dequeue() |   |   | B,C,D |   |
| 8 | prioQueue.dequeue() |   |   | C,D |   |
| 9 | prioQueue.enqueue("D",3) |   |   | C,D,D |   |
| 10 | prioQueue.enqueue("B",2) |   |   | C,D,D,B |   |
| 11 | prioQueue.dequeue() |   |   | D,D,B |   |
| 12 | prioQueue.dequeue() |   |   | D,D |   |
| 13 | prioQueue.enqueue("C",2) |   |   | D,D,C |   |
| 14 | prioQueue.enqueue("A",1) |   |   | D,D,C,A |   |
| 15 | while(prioQueue.size())!=0 |   | true |   |   |
| 16 | sysout(prioQueue.dequeue()) |   | true |   | A |
| 17 | sysout(prioQueue.dequeue()) |   | true |   | C |
| 18 | sysout(prioQueue.dequeue()) |   | true |   | D |
| 19 | sysout(prioQueue.dequeue()) |   | true |   | D |
| 20 | sysout(prioQueue.dequeue()) |   | false |   |   |
| 21 | endwhile |   |   |   |   |

>出典：基本情報技術者試験 科目B サンプル問題１　問8（IPA）

</details>

<details><summary>マージソート(37ステップ)</summary>

関数 merge を merge({2，3}，{1，4})として呼び出し昇順にして配列に格納する

| # | トレース | 判定 | n1 | n2 | work | i | j | k |
|---|---|---|---|---|---|---|---|---|
| 1 | ○int[]merge(int[]data1,int[]data2) |   |   |   |   |   |   |   |
| 2 | int n1←data1の要素数 |   | 2 |   |   |   |   |   |
| 3 | int n2←data2の要素数 |   |   | 2 |   |   |   |   |
| 4 | int[]work←{(n1+n2)の未定義の値} |   |   |   | null,null,null,null |   |   |   |
| 5 | int i←1 |   |   |   |   | 1 |   |   |
| 6 | int j←1 |   |   |   |   |   | 1 |   |
| 7 | int k←1 |   |   |   |   |   |   | 1 |
| 8 | while((i<=n1)&(j<=n2)) | true |   |   |   |   |   |   |
| 9 | if(data1[i]<=data2[j]) | false |   |   |   |   |   |   |
| 10 | else |   |   |   |   |   |   |   |
| 11 | work[k]←data2[j] |   |   |   | 1,null,null,null |   |   |   |
| 12 | j←j+1 |   |   |   |   |   | 2 |   |
| 13 | endif |   |   |   |   |   |   |   |
| 14 | k←k+1 |   |   |   |   |   |   | 2 |
| 15 | ②while((i<=n1)&(j<=n2)) | true |   |   |   |   |   |   |
| 16 | if(data1[i]<=data2[j]) | true |   |   |   |   |   |   |
| 17 | work[k]←data1[i] |   |   |   | 1,2,null,null |   |   |   |
| 18 | i←i+1 |   |   |   |   | 2 |   |   |
| 19 | endif |   |   |   |   |   |   |   |
| 20 | k←k+1 |   |   |   |   |   |   | 3 |
| 21 | ③while((i<=n1)&(j<=n2)) | true |   |   |   |   |   |   |
| 22 | if(data1[i]<=data2[j]) | true |   |   |   |   |   |   |
| 23 | work[k]←data1[i] |   |   |   | 1,2,3,null |   |   |   |
| 24 | i←i+1 |   |   |   |   | 3 |   |   |
| 25 | endif |   |   |   |   |   |   |   |
| 26 | k←k+1 |   |   |   |   |   |   | 4 |
| 27 | ④while((i<=n1)&(j<=n2)) | false |   |   |   |   |   |   |
| 28 | endwhile |   |   |   |   |   |   |   |
| 29 | while(i<=n1) | false |   |   |   |   |   |   |
| 30 | endwhile |   |   |   |   |   |   |   |
| 31 | while(j<=n2) | true |   |   |   |   |   |   |
| 32 | work[k]←data2[j] |   |   |   | 1,2,3,4 |   |   |   |
| 33 | j←j+1 |   |   |   |   |   | 3 |   |
| 34 | k←k+1 |   |   |   |   |   |   | 5 |
| 35 | ②while(j<=n2) | false |   |   |   |   |   |   |
| 36 | endwhile |   |   |   |   |   |   |   |
| 37 | return work |   |   |   | 1,2,3,4 |   |   |   |

> 出典：令和6年度 基本情報技術者試験 科目B 問4（IPA）

</details>
