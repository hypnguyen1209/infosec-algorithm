# Thuật toán trong an toàn thông tin

## 1. Tính toán trên số nguyên lớn trong trường $F_{p}$

### Phép cộng và phép trừ
* Các thuật toán cộng, trừ, nhân, chia, ..giới thiệu trong chương này phù hợp với triển khai phần mềm

* Ta giả thiết nền tảng triển khai có kiến trúc W - bit trong đó W là bội số của 8 (phổ biến là 64 - 32 bit), các hệ thống máy có công suất thấp có thể có W nhỏ hơn, VD: hệ thống nhúng W = 16 bit, thẻ thông minh W = 8 bit.

* Các bit của một W-bit là từ U được đánh số từ phải qua trái bắt đầu từ 0 đến W -1.
---
* Ta có $F_{p}$ = {0 … p - 1}.

* Tính m = [ $\log_{2}(p)$ ] là độ dài bit của $p$ và $t$ = [ $m/W$ ] là độ dài từ của 

* Biểu diễn của phần tử a được lưu trữ trong một mảng $A$ = (A[t - 1], …, A[2], A[1], A[0]) của t các từ W bit, trong đó bit ngoài cùng bên phải của A[0] là bit có trọng số thấp nhất.

| A[t - 1] | ... | A[2] | A[1] | A[0] |
|----------|-----|------|------|------|

* Biểu diễn $F_{p}$ như một mảng $A$ của các từ W-bit:

![](https://i.imgur.com/lGonQDk.png)

#### Ví dụ

Ví dụ: cho $W$ = 8, xét $F_{2147483647}$, hãy biểu diễn số $a$ = 23456789 dưới dạng mảng

* Ta có $m$ = [ $\log_{2}(p)$ ] = [ $\log_{2}(2147483647)$ ] $= 31, t = [ 31/8 ] = 4$

* Biểu diễn a dưới dạng mảng ($A[3], A[2], A[1], A[0]$)

* $a$ $= 2^{(t-1)W}A[t-1]$ $+ .... +$ $2^{2W}A[2] + 2^{W}A[2] + A[0]$

    $= 2^{(4-1)8}A[t-1]$ $+$ $2^{2.8}A[2] + 2^{8}A[2] + A[0]$

    $= 2^{24}A[t-1]$ $+$ $2^{16}A[2] + 2^{8}A[2] + A[0]$

    $= 2^{24}.1$ $+$ $2^{16}.101 + 2^{8}.236 + 21$

* Vậy $a$ được biểu diễn qua mảng $A$: $(1, 101, 236, 21)$

---
* Thuật toán cộng và trừ trên trường hữu hạn được đưa ra dưới dạng các thuật toán tương ứng cho các số nguyên $w$. Phép gán dạng "$(ε, z) ← w$" được định nghĩa như sau:
    * $z$ ← $w$ $mod$ $2^{W}$ và $ε ← 0$ nếu $w \in [0, 2W)$, ngược lại $ε ← 1$
    * Nếu $w = x + y + ε'$ với $x$, $y$ $\in [0, 2W)$ và $ε'$ $\in \{0, 1\}$ , thì $w = ε.2^{W} + z$ và $ε$ được gọi là "bit nhớ" (carry bit) cho phép cộng mỗi một từ đơn ($ε = 1$ nếu và chỉ nếu $z < x + ε'$)

---
### Thuật toán cộng chính xác bội:
#### Algorithm 1. Multiprecision addition

**Input**: số nguyên $a, b \in [0, 2^{Wt})$
<br>
**Output**: $(ε, c)$ với $c = a + b$ $mod$ $2^{Wt}$ và ε là bit nhớ

1. $(ε, C[0]) ← A[0] + B[0]$
2. For $i$ from $1$ to $t - 1$ do
    2.1. $(ε, C[i]) ← A[i] + B[i] + ε$
3. Return $(ε, c)$

[multiprecision_addition.py](./multiprecision_addition.py)

#### Algorithm 2. Multiprecision subtraction

**Input**: số nguyên $a, b \in [0, 2^{Wt})$
<br>
**Output**: $(ε, c)$ với $c = a - b$ $mod$ $2^{Wt}$ và ε là bit mượn
1. $(ε, C[0]) ← A[0] - B[0]$
2 For $i$ from $1$ to $t - 1$ do
    2.1. $(ε, C[i]) ← A[i] - B[i] - ε$
3. Return $(ε, c)$

[multiprecision_subtraction.py](./multiprecision_subtraction.py)

#### Algorithm 3. Addition in $F_{p}$

**Input**: số modulo $p$, số nguyên $a, b \in [0, p − 1]$
<br>
**Output**: $c = a + b$ $mod$ $p$

1. Dùng thuật toán Algorithm 1 để thu được $(ε, c)$ với $c = a + b$ $mod$ $2^{Wt}$ và $ε$ là bit nhớ.

2. Nếu $ε = 1$ thì trừ $p$ từ $c = (C[t – 1], …, C[2], C[1], C[0])$;
<br>
Ngược lại nếu $c \ge p$ thì $c ←  c - p$

3. Return $(c)$

[addition_in_Fp.py](./addition_in_Fp.py)

#### Algorithm 4. Subtraction in $F_{q}$

**Input**: số modulo $p$, số nguyên $a, b \in [0, p − 1]$
<br>
**Output**: $c = a - b$ $mod$ $p$

1. Dùng thuật toán Algorithm 2 để thu được $(ε, c)$ với $c = a - b$ $mod$ $2^{Wt}$ và $ε$ là bit nhớ.

2. Nếu $ε = 1$ thì thêm $p$ từ $c = (C[t – 1], …, C[2], C[1], C[0])$;

3. Return $(c)$

[subtraction_in_Fq.py](./subtraction_in_Fq.py)
