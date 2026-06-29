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

</details>
