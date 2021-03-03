### miaomiaomiao

#### [flag]

`ACTF{cxlover_1s_@_li7tl3_c4t~}`

#### [题解思路]

存在一个AES-CTR模式下的Separator Oracle，对其作以下攻击：

由于加密前的token除了16 bytes的salt均已知，因此对salt攻击即可（且salt字符集为16进制）

* 对salt的每个字符xor上($十六进制字符\oplus ord('|')$)，当Separtor Oracle返回Invalid时，即说明分割符过多
* 通过上述方法在$O(16*16)$下爆破出完整salt

