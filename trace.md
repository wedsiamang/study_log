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

<details><summary>辺リスト(edgeList)から隣接行列(adjMatrix)への変換</summary>

| # | トレース | 判定 | edgeList | nodeNum | i | u | v | adjMatrix |
|---|---|---|---|---|---|---|---|---|
| 1 | ○int[][]edgesToMatrix(int[][]edgeList,int nodeNum) |   | {{1,3},{1,4},{3,4},{2,4},{4,5}} | 5 |   |   |   |   |
| 2 | int[][]adjMatrix←{nodeNum行nodeNum列の0} |   |   |   |   |   |   | {{0,0,0,0,0},{0,0,0,0,0},{0,0,0,0,0},{0,0,0,0,0},{0,0,0,0,0}} |
| 3 | int i,u,v |   |   |   |   |   |   |   |
| 4 | for(iを1からedgeListの要素数++) |   |   |   | 1 |   |   |   |
| 5 | u←edgeList[i][1] |   |   |   |   | 1 |   |   |
| 6 | v←edgeList[i][2] |   |   |   |   |   | 3 |   |
| 7 | adjMatrix[u,v]←1 |   |   |   |   |   |   | {{0,0,1,0,0},{0,0,0,0,0},{0,0,0,0,0},{0,0,0,0,0},{0,0,0,0,0}} |
| 8 | adjMatrix[v,u]←1 |   |   |   |   |   |   | {{0,0,1,0,0},{0,0,0,0,0},{1,0,0,0,0},{0,0,0,0,0},{0,0,0,0,0}} |
| 9 | for(iを1からedgeListの要素数++) |   |   |   | 2 |   |   |   |
| 10 | u←edgeList[i][1] |   |   |   |   | 1 |   |   |
| 11 | v←edgeList[i][2] |   |   |   |   |   | 4 |   |
| 12 | adjMatrix[u,v]←1 |   |   |   |   |   |   | {{0,0,1,1,0},{0,0,0,0,0},{1,0,0,0,0},{0,0,0,0,0},{0,0,0,0,0}} |
| 13 | adjMatrix[v,u]←1 |   |   |   |   |   |   | {{0,0,1,1,0},{0,0,0,0,0},{1,0,0,0,0},{1,0,0,0,0},{0,0,0,0,0}} |
| 14 | for(iを1からedgeListの要素数++) |   |   |   | 3 |   |   |   |
| 15 | u←edgeList[i][1] |   |   |   |   | 3 |   |   |
| 16 | v←edgeList[i][2] |   |   |   |   |   | 4 |   |
| 17 | adjMatrix[u,v]←1 |   |   |   |   |   |   | {{0,0,1,1,0},{0,0,0,0,0},{1,0,0,1,0},{1,0,0,0,0},{0,0,0,0,0}} |
| 18 | adjMatrix[v,u]←1 |   |   |   |   |   |   | {{0,0,1,1,0},{0,0,0,0,0},{1,0,0,1,0},{1,0,1,0,0},{0,0,0,0,0}} |
| 19 | for(iを1からedgeListの要素数++) |   |   |   | 4 |   |   |   |
| 20 | u←edgeList[i][1] |   |   |   |   | 2 |   |   |
| 21 | v←edgeList[i][2] |   |   |   |   |   | 4 |   |
| 22 | adjMatrix[u,v]←1 |   |   |   |   |   |   | {{0,0,1,1,0},{0,0,0,1,0},{1,0,0,1,0},{1,0,1,0,0},{0,0,0,0,0}} |
| 23 | adjMatrix[v,u]←1 |   |   |   |   |   |   | {{0,0,1,1,0},{0,0,0,1,0},{1,0,0,1,0},{1,1,1,0,0},{0,0,0,0,0}} |
| 24 | for(iを1からedgeListの要素数++) |   |   |   | 5 |   |   |   |
| 25 | u←edgeList[i][1] |   |   |   |   | 4 |   |   |
| 26 | v←edgeList[i][2] |   |   |   |   |   | 5 |   |
| 27 | adjMatrix[u,v]←1 |   |   |   |   |   |   | {{0,0,1,1,0},{0,0,0,1,0},{1,0,0,1,0},{1,1,1,0,1},{0,0,0,0,0}} |
| 28 | adjMatrix[v,u]←1 |   |   |   |   |   |   | {{0,0,1,1,0},{0,0,0,1,0},{1,0,0,1,0},{1,1,1,0,1},{0,0,0,1,0}} |
| 29 | endfor |   |   |   |   |   |   |   |
| 30 | return adjMatrix |   |   |   |   |   |   | {{0,0,1,1,0},{0,0,0,1,0},{1,0,0,1,0},{1,1,1,0,1},{0,0,0,1,0}} |
  
</details>

<details><summary>2進数文字列から10進整数への変換</summary>

| # | トレース | 判定 | binary | i | length | result |
|---|---|---|---|---|---|---|
| 1 | ○int convDecimal(String binary) |   | "10010" |   |   |   |
| 2 | int i,length,result←0 |   |   |   |   | 0 |
| 3 | length←binaryの文字数 |   |   |   | 5 |   |
| 4 | for(iを1からlengthまで++) | true |   | 1 |   |   |
| 5 | result←result*2+int(binaryのi文字目の文字) |   |   |   |   | 1 |
| 6 | for(iを1からlengthまで++) | true |   | 2 |   |   |
| 7 | result←result*2+int(binaryのi文字目の文字) |   |   |   |   | 2 |
| 8 | for(iを1からlengthまで++) | true |   | 3 |   |   |
| 9 | result←result*2+int(binaryのi文字目の文字) |   |   |   |   | 4 |
| 10 | for(iを1からlengthまで++) | true |   | 4 |   |   |
| 11 | result←result*2+int(binaryのi文字目の文字) |   |   |   |   | 9 |
| 12 | for(iを1からlengthまで++) | true |   | 5 |   |   |
| 13 | result←result*2+int(binaryのi文字目の文字) |   |   |   |   | 18 |
| 14 | for(iを1からlengthまで++) | false |   | 6 |   |   |
| 15 | endfor |   |   |   |   |   |
| 16 | return result |   |   |   |   | 18 |

</details>

<details><summary>素数列挙</summary>

| # | トレース | 判定 | maxNum | pnList | i | j | divideFlag | iの正の平方根の整数部分 |
|---|---|---|---|---|---|---|---|---|
| 1 | ○int[]findPrimeNumbers(int maxNum) |   | 5 |   |   |   |   |   |
| 2 | int[]pnList←{} |   |   |   |   |   |   |   |
| 3 | int i,j |   |   |   |   |   |   |   |
| 4 | boolean divideFlag |   |   |   |   |   |   |   |
| 5 | for(iを2~maxNum++) | true |   |   | 2 |   |   |   |
| 6 | divideFlag←true |   |   |   |   |   | true |   |
| 7 | α:for(jを2~iの正の平方根の整数部分++) | false |   |   |   |   |   | 1 |
| 8 | endfor |   |   |   |   |   |   |   |
| 9 | if(divideFlag==true) | true |   |   |   |   |   |   |
| 10 | pnListの末尾にiの値を追加する |   |   | 2 |   |   |   |   |
| 11 | endif |   |   |   |   |   |   |   |
| 12 | for(iを2~maxNum++) | true |   |   | 3 |   |   |   |
| 13 | divideFlag←true |   |   |   |   |   | true |   |
| 14 | α:for(jを2~iの正の平方根の整数部分++) | false |   |   |   |   |   | 1 |
| 15 | endfor |   |   |   |   |   |   |   |
| 16 | if(divideFlag==true) | true |   |   |   |   |   |   |
| 17 | pnListの末尾にiの値を追加する |   |   | 2,3 |   |   |   |   |
| 18 | endif |   |   |   |   |   |   |   |
| 19 | for(iを2~maxNum++) |   |   |   | 4 |   |   |   |
| 20 | divideFlag←true |   |   |   |   |   | true |   |
| 21 | α:for(jを2~iの正の平方根の整数部分++) | true |   |   |   | 2 |   | 2 |
| 22 | if(i mod j==0) | true |   |   |   |   |   |   |
| 23 | divideFlag←false |   |   |   |   |   | false |   |
| 24 | α:break |   |   |   |   |   |   |   |
| 25 | endfor |   |   |   |   |   |   |   |
| 26 | if(divideFlag==true) | false |   |   |   |   |   |   |
| 27 | endif |   |   |   |   |   |   |   |
| 28 | for(iを2~maxNum++) |   |   |   | 5 |   |   |   |
| 29 | divideFlag←true |   |   |   |   |   | true |   |
| 30 | α:for(jを2~iの正の平方根の整数部分++) | true |   |   |   | 2 |   | 2 |
| 31 | if(i mod j==0) | false |   |   |   |   |   |   |
| 32 | endif |   |   |   |   |   |   |   |
| 33 | if(divideFlag==true) | true |   |   |   |   |   |   |
| 34 | pnListの末尾にiの値を追加する |   |   | 2,3,5 |   |   |   |   |
| 35 | endif |   |   |   |   |   |   |   |
| 36 | for(iを2~maxNum++) | false |   |   | 6 |   |   |   |
| 37 | endfor |   |   |   |   |   |   |   |
| 38 | return pnList |   |   | 2,3,5 |   |   |   |   |

</details>

<details><summary>ビット列の反転</summary>

| # | トレース | 判定 | byte | rbyte | r | i | (r<<1) | (rbyte∧00000001) | rbyte>>1 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ○8bit型 rev(8bit型 byte) |   | 01001011 |   |   |   |   |   |   |
| 2 | 8bit型 rbyte←byte |   |   | 01001011 |   |   |   |   |   |
| 3 | 8bit型 r←00000000 |   |   |   | 00000000 |   |   |   |   |
| 4 | int i |   |   |   |   |   |   |   |   |
| 5 | for(iを1~8++) | true |   |   |   | 1 |   |   |   |
| 6 | r←(r<<1)∨(rbyte∧00000001) |   |   |   | 00000001 |   | 00000000 | 00000001 |   |
| 7 | rbyte←rbyte>>1 |   |   | 00100101 |   |   |   |   | 00100101 |
| 8 | for(iを1~8++) | true |   |   |   | 2 |   |   |   |
| 9 | r←(r<<1)∨(rbyte∧00000001) |   |   |   | 00000011 |   | 00000010 | 00000001 |   |
| 10 | rbyte←rbyte>>1 |   |   | 00010010 |   |   |   |   | 00010010 |
| 11 | for(iを1~8++) | true |   |   |   | 3 |   |   |   |
| 12 | r←(r<<1)∨(rbyte∧00000001) |   |   |   | 00000110 |   | 00000110 | 00000000 |   |
| 13 | rbyte←rbyte>>1 |   |   | 00001001 |   |   |   |   | 00001001 |
| 14 | for(iを1~8++) | true |   |   |   | 4 |   |   |   |
| 15 | r←(r<<1)∨(rbyte∧00000001) |   |   |   | 00001101 |   | 00001100 | 00000001 |   |
| 16 | rbyte←rbyte>>1 |   |   | 00000100 |   |   |   |   | 00000100 |
| 17 | for(iを1~8++) | true |   |   |   | 5 |   |   |   |
| 18 | r←(r<<1)∨(rbyte∧00000001) |   |   |   | 00011010 |   | 00011010 | 00000000 |   |
| 19 | rbyte←rbyte>>1 |   |   | 00000010 |   |   |   |   | 00000010 |
| 20 | for(iを1~8++) | true |   |   |   | 6 |   |   |   |
| 21 | r←(r<<1)∨(rbyte∧00000001) |   |   |   | 00110100 |   | 00110100 | 00000000 |   |
| 22 | rbyte←rbyte>>1 |   |   | 00000001 |   |   |   |   | 00000001 |
| 23 | for(iを1~8++) | true |   |   |   | 7 |   |   |   |
| 24 | r←(r<<1)∨(rbyte∧00000001) |   |   |   | 01101001 |   | 01101000 | 00000001 |   |
| 25 | rbyte←rbyte>>1 |   |   | 00000000 |   |   |   |   | 00000000 |
| 26 | for(iを1~8++) | true |   |   |   | 8 |   |   |   |
| 27 | r←(r<<1)∨(rbyte∧00000001) |   |   |   | 11010010 |   | 11010010 | 00000000 |   |
| 28 | rbyte←rbyte>>1 |   |   | 00000000 |   |   |   |   | 00000000 |
| 29 | for(iを1~8++) | false |   |   |   | 9 |   |   |   |
| 30 | endfor |   |   |   |   |   |   |   |   |
| 31 | return r |   |   |   | 11010010 |   |   |   |   |
  
</details>

<details><summary>文字の隣接確率(バイグラム)</summary>

| # | トレース | 判定 | c1 | c2 | s1 | s2 | words.freq(s1+s2) | (words.freq(s1) | words.freqE(s1) | (words.freq(s1)-words.freqE(s1)) | words.freq(s1+s2)/(words.freq(s1)-words.freqE(s1)) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | INT WORDS words←{"importance","inflation","information","innovation"} |   |   |   |   |   |   |   |   |   |   |
| 2 | int freq(String str)//英単語群中の文字列strの出現回数を返す |   |   |   |   |   |   |   |   |   |   |
| 3 | int freqE(String str)//英単語群の中で文字列strで終わる英単語の数を返す |   |   |   |   |   |   |   |   |   |   |
| 4 | ○double prob(String c1,String c2) |   | "n" | "f" |   |   |   |   |   |   |   |
| 5 | String s1←c1の1文字だけから成る文字列 |   |   |   | "n" |   |   |   |   |   |   |
| 6 | String s2←c2の1文字だけから成る文字列 |   |   |   |   | "f" |   |   |   |   |   |
| 7 | if(words.freq(s1+s2)>0) | true |   |   |   |   | 2 |   |   |   |   |
| 8 | return words.freq(s1+s2)/(words.freq(s1)-words.freqE(s1)) |   |   |   |   |   | 2 | 8 | 3 | 5 | 0.4 |
  
</details>

<details><summary>理論度数</summary>

| # | トレース | 判定 | data | t | row | col | result | r | c | (dataの行番号rの要素の和) | (dataの列番号cの要素の和) | (dataの行番号rの要素の和)*(dataの列番号cの要素の和)/t |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ○double[][] f(double[][] data) |   | {{82,6},{58,8}} |   |   |   |   |   |   |   |   |   |
| 2 | double t←dataの要素の和 |   |   | 154 |   |   |   |   |   |   |   |   |
| 3 | int row←dataの行数 |   |   |   | 2 |   |   |   |   |   |   |   |
| 4 | int col←dataの列数 |   |   |   |   | 2 |   |   |   |   |   |   |
| 5 | double[][] result←{row行col列の未定義の値} |   |   |   |   |   | {{0,0},{0,0}} |   |   |   |   |   |
| 6 | int r,c |   |   |   |   |   |   |   |   |   |   |   |
| 7 | for(rを1~row++) | true |   |   |   |   |   | 1 |   |   |   |   |
| 8 | for(cを1~col++) | true |   |   |   |   |   |   | 1 |   |   |   |
| 9 | result[r,c]←(dataの行番号rの要素の和)*(dataの列番号cの要素の和)/t |   |   |   |   |   | {{80,0},{0,0}} |   |   | 88 | 140 | 80 |
| 10 | for(cを1~col++) | true |   |   |   |   |   |   | 2 |   |   |   |
| 11 | result[r,c]←(dataの行番号rの要素の和)*(dataの列番号cの要素の和)/t |   |   |   |   |   | {{80,8},{0,0}} |   |   | 88 | 14 | 8 |
| 12 | for(cを1~col++) | false |   |   |   |   |   |   | 3 |   |   |   |
| 13 | endfor |   |   |   |   |   |   |   |   |   |   |   |
| 14 | for(rを1~row++) | true |   |   |   |   |   | 2 |   |   |   |   |
| 15 | for(cを1~col++) | true |   |   |   |   |   |   | 1 |   |   |   |
| 16 | result[r,c]←(dataの行番号rの要素の和)*(dataの列番号cの要素の和)/t |   |   |   |   |   | {{80,8},{60,0}} |   |   | 66 | 140 | 60 |
| 17 | for(cを1~col++) | true |   |   |   |   |   |   | 2 |   |   |   |
| 18 | result[r,c]←(dataの行番号rの要素の和)*(dataの列番号cの要素の和)/t |   |   |   |   |   | {{80,8},{60,6}} |   |   | 66 | 14 | 6 |
| 19 | for(cを1~col++) | false |   |   |   |   |   |   | 3 |   |   |   |
| 20 | endfor |   |   |   |   |   |   |   |   |   |   |   |
| 21 | for(rを1~row++) | false |   |   |   |   |   | 3 |   |   |   |   |
| 22 | endfor |   |   |   |   |   |   |   |   |   |   |   |
| 23 | return result |   |   |   |   |   | {{80,8},{60,6}} |   |   |   |   |   |

  
</details>

<details><summary>二分木の通りがけ順走査（再帰）</summary>

出力はあっているが、再帰の戻り方、階層を間違えている

| # | トレース | 判定 | n | tree[n] | tree[n][1] | tree[n][2] | system.out.println(n) |
|---|---|---|---|---|---|---|---|
| 1 | INT [] tree←{{2,3},{4,5},{6,7},{8,9},{10,11},{12,13},{14},{},{},{},{},{},{},{}} |   |   |   |   |   |   |
| 2 | ○order(int n) |   | 1 |   |   |   |   |
| 3 | if(tree[n]の要素数==2) | true |   | {2,3} |   |   |   |
| 4 | order(tree[n][1]) |   |   |   | 2 |   |   |
| 5 | order(2) |   | 2 |   |   |   |   |
| 6 | if(tree[n]の要素数==2) | true |   | {4,5} |   |   |   |
| 7 | order(tree[n][1]) |   |   |   | 4 |   |   |
| 8 | order(4) |   | 4 |   |   |   |   |
| 9 | if(tree[n]の要素数==2) | true |   | {8,9} |   |   |   |
| 10 | order(tree[n][1]) |   |   |   | 8 |   |   |
| 11 | order(8) |   | 8 |   |   |   |   |
| 12 | if(tree[n]の要素数==2) | false |   | {} |   |   |   |
| 13 | elseif(tree[n]の要素数==1) | false |   |   |   |   |   |
| 14 | else |   |   |   |   |   |   |
| 15 | system.out.println(n) |   |   |   |   |   | 8 |
| 16 | endif |   |   |   |   |   |   |
| 17 | order(4) |   | 4 |   |   |   |   |
| 18 | system.out.println(n) |   |   |   |   |   | 8,4 |
| 19 | order(tree[n][2]) |   |   |   |   | 9 |   |
| 20 | order(9) |   | 9 |   |   |   |   |
| 21 | if(tree[n]の要素数==2) | false |   | {} |   |   |   |
| 22 | elseif(tree[n]の要素数==1) | false |   | {} |   |   |   |
| 23 | else |   |   |   |   |   |   |
| 24 | system.out.println(n) |   |   |   |   |   | 8,4,9 |
| 25 | endif |   |   |   |   |   |   |
| 26 | order(2) |   | 2 |   |   |   |   |
| 27 | system.out.println(n) |   |   |   |   |   | 8,4,9,2 |
| 28 | order(tree[n][2]) |   |   |   |   | 5 |   |
| 29 | order(5) |   | 5 |   |   |   |   |
| 30 | if(tree[n]の要素数==2) | true |   | {10,11} |   |   |   |
| 31 | order([n][1]) |   |   |   | 10 |   |   |
| 32 | order(10) |   | 10 |   |   |   |   |
| 33 | if(tree[n]の要素数==2) | false |   | {} |   |   |   |
| 34 | elseif(tree[n]の要素数==1) | false |   | {} |   |   |   |
| 35 | else |   |   |   |   |   |   |
| 36 | system.out.println(n) |   |   |   |   |   | 8,4,9,2,10, |
| 37 | endif |   |   |   |   |   |   |
| 38 | order(5) |   |   |   |   |   |   |
| 39 | system.out.println(n) |   |   |   |   |   | 8,4,9,2,10,5, |
| 40 | order(tree[n][2]) |   |   |   |   | 11 |   |
| 41 | order(11) |   | 11 |   |   |   |   |
| 42 | if(tree[n]の要素数==2) | false |   | {} |   |   |   |
| 43 | elseif(tree[n]の要素数==1) | false |   | {} |   |   |   |
| 44 | else |   |   |   |   |   |   |
| 45 | system.out.println(n) |   |   |   |   |   | 8,4,9,2,10,5,11, |
| 46 | endif |   |   |   |   |   |   |
| 47 | order(1) |   |   |   |   |   |   |
| 48 | system.out.println(n) |   |   |   |   |   | 8,4,9,2,10,5,11,1, |
| 49 | order(tree[n][2]) |   |   |   |   | 3 |   |
| 50 | order(3) |   | 3 |   |   |   |   |
| 51 | if(tree[n]の要素数==2) | true |   | {6,7} |   |   |   |
| 52 | order(tree[n][1]) |   |   |   | 6 |   |   |
| 53 | order(6) |   |   |   |   |   |   |
| 54 | if(tree[n]の要素数==2) | true |   | {12,13} |   |   |   |
| 55 | order(tree[n][1]) |   |   |   | 12 |   |   |
| 56 | order(12) |   | 12 |   |   |   |   |
| 57 | if(tree[n]の要素数==2) | false |   | {} |   |   |   |
| 58 | elseif(tree[n]の要素数==1) | false |   | {} |   |   |   |
| 59 | else |   |   |   |   |   |   |
| 60 | system.out.println(n) |   |   |   |   |   | 8,4,9,2,10,5,11,1,12 |
| 61 | endif |   |   |   |   |   |   |
| 62 | order(6) |   | 6 |   |   |   |   |
| 63 | system.out.println(n) |   |   |   |   |   | 8,4,9,2,10,5,11,1,12,6 |
| 64 | order(tree[n][2]) |   |   |   |   | 13 |   |
| 65 | order(13) |   | 13 |   |   |   |   |
| 66 | if(tree[n]の要素数==2) | false |   | {} |   |   |   |
| 67 | elseif(tree[n]の要素数==1) | false |   | {} |   |   |   |
| 68 | else |   |   |   |   |   |   |
| 69 | system.out.println(n) |   |   |   |   |   | 8,4,9,2,10,5,11,1,12,6,13 |
| 70 | endif |   |   |   |   |   |   |
| 71 | order(3) |   | 3 |   |   |   |   |
| 72 | system.out.println(n) |   |   |   |   |   | 8,4,9,2,10,5,11,1,12,6,13,3 |
| 73 | order(tree[n][2]) |   |   |   |   | 7 |   |
| 74 | order(7) |   |   |   |   |   |   |
| 75 | if(tree[n]の要素数==2) | false |   | {14} |   |   |   |
| 76 | elseif(tree[n]の要素数==1) | true |   | {14} |   |   |   |
| 77 | order(tree[n][1]) |   |   |   | 14 |   |   |
| 78 | order(14) |   | 14 |   |   |   |   |
| 79 | if(tree[n]の要素数==2) | false |   | {} |   |   |   |
| 80 | elseif(tree[n]の要素数==1) | false |   | {} |   |   |   |
| 81 | else |   |   |   |   |   |   |
| 82 | system.out.println(n) |   |   |   |   |   | 8,4,9,2,10,5,11,1,12,6,13,3,14 |
| 83 | endif |   |   |   |   |   |   |
| 84 | order(7) |   |   |   |   |   |   |
| 85 | system.out.println(n) |   |   |   |   |   | 8,4,9,2,10,5,11,1,12,6,13,3,14,7 |
| 86 | endif |   |   |   |   |   |   |
| 87 | order(3) |   |   |   |   |   |   |
| 88 | endif |   |   |   |   |   |   |
| 89 | order(6) |   |   |   |   |   |   |
| 90 | endif |   |   |   |   |   |   |
| 91 | order(1) |   |   |   |   |   |   |
| 92 | endif |   |   |   |   |   |   |
| 93 | order(5) |   |   |   |   |   |   |
| 94 | endif |   |   |   |   |   |   |
| 95 | order(2) |   |   |   |   |   |   |
| 96 | endif |   |   |   |   |   |   |
| 97 | order(4) |   |   |   |   |   |   |
| 98 | endif |   |   |   |   |   |   |

  
</details>

<details><summary>疎行列</summary>

| # | トレース | 判定 | matrix | i | j | sparseMatrix | matrix[i,j] |
|---|---|---|---|---|---|---|---|
| 1 | ○int[] transformSparseMatrix(int[][]matrix) |   | {{3,0,0,0,0},{0,2,2,0,0},{0,0,0,1,3},{0,0,0,2,0},{0,0,0,0,1}} |   |   |   |   |
| 2 | int i,j |   |   |   |   |   |   |
| 3 | int[] sparseMatrix |   |   |   |   |   |   |
| 4 | sparseMatrix←{{},{},{}} |   |   |   |   |   |   |
| 5 | for(iを1からmatrixの行数まで++) | true |   | 1 |   |   |   |
| 6 | for(jを1からmatrixの列数まで++) | true |   |   | 1 |   |   |
| 7 | if(matrix[i,j]!=0) | true |   |   |   |   | 3 |
| 8 | sparseMatrix[1]の末尾にiの値を追加 |   |   |   |   | {{1},{},{}} |   |
| 9 | sparseMatrix[2]の末尾にjの値を追加 |   |   |   |   | {{1},{1},{}} |   |
| 10 | sparseMatrix[3]の末尾にmatrix[i,j]の値を追加 |   |   |   |   | {{1},{1},{3}} |   |
| 11 | endif |   |   |   |   |   |   |
| 12 | for(jを1からmatrixの列数まで++) | true |   |   | 2 |   |   |
| 13 | if(matrix[i,j]!=0) | false |   |   |   |   | 0 |
| 14 | endif |   |   |   |   |   |   |
| 15 | for(jを1からmatrixの列数まで++) | true |   |   | 3 |   |   |
| 16 | if(matrix[i,j]!=0) | false |   |   |   |   | 0 |
| 17 | endif |   |   |   |   |   |   |
| 18 | for(jを1からmatrixの列数まで++) | true |   |   | 4 |   |   |
| 19 | if(matrix[i,j]!=0) | false |   |   |   |   | 0 |
| 20 | endif |   |   |   |   |   |   |
| 21 | for(jを1からmatrixの列数まで++) | true |   |   | 5 |   |   |
| 22 | if(matrix[i,j]!=0) | false |   |   |   |   | 0 |
| 23 | endif |   |   |   |   |   |   |
| 24 | for(jを1からmatrixの列数まで++) | false |   |   | 6 |   |   |
| 25 | endfor |   |   |   |   |   |   |
| 26 | for(iを1からmatrixの行数まで++) | true |   | 2 |   |   |   |
| 27 | for(jを1からmatrixの列数まで++) | true |   |   | 1 |   |   |
| 28 | if(matrix[i,j]!=0) | false |   |   |   |   | 0 |
| 29 | endif |   |   |   |   |   |   |
| 30 | for(jを1からmatrixの列数まで++) | true |   |   | 2 |   |   |
| 31 | if(matrix[i,j]!=0) | true |   |   |   |   | 2 |
| 32 | sparseMatrix[1]の末尾にiの値を追加 |   |   |   |   | {{1,2,},{1},{3}} |   |
| 33 | sparseMatrix[2]の末尾にjの値を追加 |   |   |   |   | {{1,2,},{1,2,},{3}} |   |
| 34 | sparseMatrix[3]の末尾にmatrix[i,j]の値を追加 |   |   |   |   | {{1,2,},{1,2,},{3,2}} |   |
| 35 | endif |   |   |   |   |   |   |
| 36 | for(jを1からmatrixの列数まで++) | true |   |   | 3 |   |   |
| 37 | if(matrix[i,j]!=0) | true |   |   |   |   | 2 |
| 38 | sparseMatrix[1]の末尾にiの値を追加 |   |   |   |   | {{1,2,2},{1,2,},{3,2}} |   |
| 39 | sparseMatrix[2]の末尾にjの値を追加 |   |   |   |   | {{1,2,2},{1,2,3},{3,2}} |   |
| 40 | sparseMatrix[3]の末尾にmatrix[i,j]の値を追加 |   |   |   |   | {{1,2,2},{1,2,3},{3,2,2}} |   |
| 41 | endif |   |   |   |   |   |   |
| 42 | for(jを1からmatrixの列数まで++) | true |   |   | 4 |   |   |
| 43 | if(matrix[i,j]!=0) | false |   |   |   |   | 0 |
| 44 | endif |   |   |   |   |   |   |
| 45 | for(jを1からmatrixの列数まで++) | true |   |   | 5 |   |   |
| 46 | if(matrix[i,j]!=0) | false |   |   |   |   | 0 |
| 47 | endif |   |   |   |   |   |   |
| 48 | for(jを1からmatrixの列数まで++) | false |   |   | 6 |   |   |
| 49 | endfor |   |   |   |   |   |   |
| 50 | for(iを1からmatrixの行数まで++) | true |   | 3 |   |   |   |
| 51 | for(jを1からmatrixの列数まで++) | true |   |   | 1 |   |   |
| 52 | if(matrix[i,j]!=0) | false |   |   |   |   | 0 |
| 53 | endif |   |   |   |   |   |   |
| 54 | for(jを1からmatrixの列数まで++) | true |   |   | 2 |   |   |
| 55 | if(matrix[i,j]!=0) | false |   |   |   |   | 0 |
| 56 | endif |   |   |   |   |   |   |
| 57 | for(jを1からmatrixの列数まで++) | true |   |   | 3 |   |   |
| 58 | if(matrix[i,j]!=0) | false |   |   |   |   | 0 |
| 59 | endif |   |   |   |   |   |   |
| 60 | for(jを1からmatrixの列数まで++) | true |   |   | 4 |   |   |
| 61 | if(matrix[i,j]!=0) | true |   |   |   |   | 1 |
| 62 | sparseMatrix[1]の末尾にiの値を追加 |   |   |   |   | {{1,2,2,3},{1,2,3},{3,2,2}} |   |
| 63 | sparseMatrix[2]の末尾にjの値を追加 |   |   |   |   | {{1,2,2,3},{1,2,3,4},{3,2,2}} |   |
| 64 | sparseMatrix[3]の末尾にmatrix[i,j]の値を追加 |   |   |   |   | {{1,2,2,3},{1,2,3,4},{3,2,2,1}} |   |
| 65 | endif |   |   |   |   |   |   |
| 66 | for(jを1からmatrixの列数まで++) | true |   |   | 5 |   |   |
| 67 | if(matrix[i,j]!=0) | true |   |   |   |   | 3 |
| 68 | sparseMatrix[1]の末尾にiの値を追加 |   |   |   |   | {{1,2,2,3,3},{1,2,3,4},{3,2,2,1}} |   |
| 69 | sparseMatrix[2]の末尾にjの値を追加 |   |   |   |   | {{1,2,2,3,3},{1,2,3,4,5},{3,2,2,1}} |   |
| 70 | sparseMatrix[3]の末尾にmatrix[i,j]の値を追加 |   |   |   |   | {{1,2,2,3,3},{1,2,3,4,5},{3,2,2,1,3}} |   |
| 71 | endif |   |   |   |   |   |   |
| 72 | for(jを1からmatrixの列数まで++) | false |   |   | 6 |   |   |
| 73 | endfor |   |   |   |   |   |   |
| 74 | for(iを1からmatrixの行数まで++) | true |   | 4 |   |   |   |
| 75 | for(jを1からmatrixの列数まで++) | true |   |   | 1 |   |   |
| 76 | if(matrix[i,j]!=0) | false |   |   |   |   | 0 |
| 77 | endif |   |   |   |   |   |   |
| 78 | for(jを1からmatrixの列数まで++) | true |   |   | 2 |   |   |
| 79 | if(matrix[i,j]!=0) | false |   |   |   |   | 0 |
| 80 | endif |   |   |   |   |   |   |
| 81 | for(jを1からmatrixの列数まで++) | true |   |   | 3 |   |   |
| 82 | if(matrix[i,j]!=0) | false |   |   |   |   | 0 |
| 83 | endif |   |   |   |   |   |   |
| 84 | for(jを1からmatrixの列数まで++) | true |   |   | 4 |   |   |
| 85 | if(matrix[i,j]!=0) | true |   |   |   |   | 2 |
| 86 | sparseMatrix[1]の末尾にiの値を追加 |   |   |   |   | {{1,2,2,3,3,4},{1,2,3,4,5},{3,2,2,1,3}} |   |
| 87 | sparseMatrix[2]の末尾にjの値を追加 |   |   |   |   | {{1,2,2,3,3,4},{1,2,3,4,5,4},{3,2,2,1,3}} |   |
| 88 | sparseMatrix[3]の末尾にmatrix[i,j]の値を追加 |   |   |   |   | {{1,2,2,3,3,4},{1,2,3,4,5,4},{3,2,2,1,3,2}} |   |
| 89 | endif |   |   |   |   |   |   |
| 90 | for(jを1からmatrixの列数まで++) | true |   |   | 5 |   |   |
| 91 | if(matrix[i,j]!=0) | false |   |   |   |   | 0 |
| 92 | endif |   |   |   |   |   |   |
| 93 | for(jを1からmatrixの列数まで++) | false |   |   | 6 |   |   |
| 94 | endfor |   |   |   |   |   |   |
| 95 | for(iを1からmatrixの行数まで++) | true |   | 5 |   |   |   |
| 96 | for(jを1からmatrixの列数まで++) | true |   |   | 1 |   |   |
| 97 | if(matrix[i,j]!=0) | false |   |   |   |   | 0 |
| 98 | endif |   |   |   |   |   |   |
| 99 | for(jを1からmatrixの列数まで++) | true |   |   | 2 |   |   |
| 100 | if(matrix[i,j]!=0) | false |   |   |   |   | 0 |
| 101 | endif |   |   |   |   |   |   |
| 102 | for(jを1からmatrixの列数まで++) | true |   |   | 3 |   |   |
| 103 | if(matrix[i,j]!=0) | false |   |   |   |   | 0 |
| 104 | endif |   |   |   |   |   |   |
| 105 | for(jを1からmatrixの列数まで++) | true |   |   | 4 |   |   |
| 106 | if(matrix[i,j]!=0) | false |   |   |   |   | 0 |
| 107 | endif |   |   |   |   |   |   |
| 108 | for(jを1からmatrixの列数まで++) | true |   |   | 5 |   |   |
| 109 | if(matrix[i,j]!=0) | true |   |   |   |   | 1 |
| 110 | sparseMatrix[1]の末尾にiの値を追加 |   |   |   |   | {{1,2,2,3,3,4,5},{1,2,3,4,5,4},{3,2,2,1,3,2}} |   |
| 111 | sparseMatrix[2]の末尾にjの値を追加 |   |   |   |   | {{1,2,2,3,3,4,5},{1,2,3,4,5,4,5},{3,2,2,1,3,2}} |   |
| 112 | sparseMatrix[3]の末尾にmatrix[i,j]の値を追加 |   |   |   |   | {{1,2,2,3,3,4,5},{1,2,3,4,5,4,5},{3,2,2,1,3,2,1}} |   |
| 113 | endif |   |   |   |   |   |   |
| 114 | for(jを1からmatrixの列数まで++) | false |   |   | 6 |   |   |
| 115 | endfor |   |   |   |   |   |   |
| 116 | for(iを1からmatrixの行数まで++) | false |   |   | 6 |   |   |
| 117 | endfor |   |   |   |   |   |   |
| 118 | return sparseMatrix |   |   |   |   | {{1,2,2,3,3,4,5},{1,2,3,4,5,4,5},{3,2,2,1,3,2,1}} |   |
  
</details>
