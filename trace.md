### Trace
<details><summary>優先度付きキュー</summary>

優先度付きキュー（値が小さいほど高優先度）のスケジューラを、enqueue/dequeue で1ステップずつ追跡

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

<details><summary>マージ</summary>

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

</details>

<details><summary>範囲内の4の倍数を数える ― 全走査と倍数ジャンプの比較</summary>

| # | トレース | 判定 | n | m | count | i | tempN | j |
|---|---|---|---|---|---|---|---|---|
| 1 | ○function1(int n,int m) |   | 3 | 14 |   |   |   |   |
| 2 | int count←0 |   |   |   | 0 |   |   |   |
| 3 | int i |   |   |   |   |   |   |   |
| 4 | for(iをn~m++) |   |   |   |   | 3 |   |   |
| 5 | if((imod4)=0) | false |   |   |   |   |   |   |
| 6 | endif |   |   |   |   |   |   |   |
| 7 | for(iをn~m++) |   |   |   |   | 4 |   |   |
| 8 | if((imod4)=0) | true |   |   |   |   |   |   |
| 9 | count←count+1 |   |   |   | 1 |   |   |   |
| 10 | endif |   |   |   |   |   |   |   |
| 11 | for(iをn~m++) |   |   |   |   | 5 |   |   |
| 12 | if((imod4)=0) | false |   |   |   |   |   |   |
| 13 | endif |   |   |   |   |   |   |   |
| 14 | for(iをn~m++) |   |   |   |   | 6 |   |   |
| 15 | if((imod4)=0) | false |   |   |   |   |   |   |
| 16 | endif |   |   |   |   |   |   |   |
| 17 | for(iをn~m++) |   |   |   |   | 7 |   |   |
| 18 | if((imod4)=0) | false |   |   |   |   |   |   |
| 19 | endif |   |   |   |   |   |   |   |
| 20 | for(iをn~m++) |   |   |   |   | 8 |   |   |
| 21 | if((imod4)=0) | true |   |   |   |   |   |   |
| 22 | count←count+1 |   |   |   | 2 |   |   |   |
| 23 | for(iをn~m++) |   |   |   |   | 9 |   |   |
| 24 | if((imod4)=0) | false |   |   |   |   |   |   |
| 25 | endif |   |   |   |   |   |   |   |
| 26 | for(iをn~m++) |   |   |   |   | 10 |   |   |
| 27 | if((imod4)=0) | false |   |   |   |   |   |   |
| 28 | endif |   |   |   |   |   |   |   |
| 29 | for(iをn~m++) |   |   |   |   | 11 |   |   |
| 30 | if((imod4)=0) | false |   |   |   |   |   |   |
| 31 | endif |   |   |   |   |   |   |   |
| 32 | for(iをn~m++) |   |   |   |   | 12 |   |   |
| 33 | if((imod4)=0) | true |   |   |   |   |   |   |
| 34 | count←count+1 |   |   |   | 3 |   |   |   |
| 35 | endif |   |   |   |   |   |   |   |
| 36 | for(iをn~m++) |   |   |   |   | 13 |   |   |
| 37 | if((imod4)=0) | false |   |   |   |   |   |   |
| 38 | endif |   |   |   |   |   |   |   |
| 39 | for(iをn~m++) |   |   |   |   | 14 |   |   |
| 40 | if((imod4)=0) | false |   |   |   |   |   |   |
| 41 | endif |   |   |   |   |   |   |   |
| 42 | for(iをn~m++) |   |   |   |   |   |   |   |
| 43 | endfor |   |   |   |   |   |   |   |
| 44 | return count |   |   |   | 3 |   |   |   |
| 45 |   |   |   |   |   |   |   |   |
| 46 | ○function2(int n,int m) |   | 3 | 14 |   |   |   |   |
| 47 | int count←0 |   |   |   | 0 |   |   |   |
| 48 | int tempN←n |   |   |   |   |   | 3 |   |
| 49 | int i , j |   |   |   |   |   |   |   |
| 50 | for(iを1~3++) |   |   |   |   | 1 |   |   |
| 51 | if((tempN mod 4)=0) | false |   |   |   |   |   |   |
| 52 | endif |   |   |   |   |   |   |   |
| 53 | tempN←tempN+1 |   |   |   |   |   | 4 |   |
| 54 | for(iを1~3++) |   |   |   |   | 2 |   |   |
| 55 | if((tempN mod 4)=0) | true |   |   |   |   |   |   |
| 56 | break |   |   |   |   |   |   |   |
| 57 | endfor |   |   |   |   |   |   |   |
| 58 | for(jをtempN~m4++) |   |   |   |   |   |   | 4 |
| 59 | count←count+1 |   |   |   | 1 |   |   |   |
| 60 | for(jをtempN~m4++) |   |   |   |   |   |   | 8 |
| 61 | count←count+1 |   |   |   | 2 |   |   |   |
| 62 | for(jをtempN~m4++) |   |   |   |   |   |   | 12 |
| 63 | count←count+1 |   |   |   | 3 |   |   |   |
| 64 | for(jをtempN~m4++) |   |   |   |   |   |   | 16 |
| 65 | endfor |   |   |   |   |   |   |   |
| 66 | return count |   |   |   | 3 |   |   |   |
  
</details>

<details><summary>最大公約数</summary>

  | # | トレース | 判定 | num1 | num2 | x | y |
|---|---|---|---|---|---|---|
| 1 | ○int gcd(int num1,int num2) |   | 8 | 26 |   |   |
| 2 | int x←num1 |   |   |   | 8 |   |
| 3 | int y←num2 |   |   |   |   | 26 |
| 4 | while(x!=y) | true |   |   |   |   |
| 5 | if(x>y) | false |   |   |   |   |
| 6 | else |   |   |   |   |   |
| 7 | y←y-x |   |   |   |   | 18 |
| 8 | endif |   |   |   |   |   |
| 9 | while(x!=y) | true |   |   |   |   |
| 10 | if(x>y) | false |   |   |   |   |
| 11 | else |   |   |   |   |   |
| 12 | y←y-x |   |   |   |   | 10 |
| 13 | endif |   |   |   |   |   |
| 14 | while(x!=y) | true |   |   |   |   |
| 15 | if(x>y) | false |   |   |   |   |
| 16 | y←y-x |   |   |   |   | 2 |
| 17 | endif |   |   |   |   |   |
| 18 | while(x!=y) | true |   |   |   |   |
| 19 | if(x>y) | true |   |   |   |   |
| 20 | x←x-y |   |   |   | 6 |   |
| 21 | endif |   |   |   |   |   |
| 22 | while(x!=y) | true |   |   |   |   |
| 23 | if(x>y) | true |   |   |   |   |
| 24 | x←x-y |   |   |   | 4 |   |
| 25 | endif |   |   |   |   |   |
| 26 | while(x!=y) | true |   |   |   |   |
| 27 | if(x>y) | true |   |   |   |   |
| 28 | x←x-y |   |   |   | 2 |   |
| 29 | endif |   |   |   |   |   |
| 30 | while(x!=y) | false |   |   |   |   |
| 31 | endwhile |   |   |   |   |   |
| 32 | return x |   |   |   | 2 |   |

</details>
