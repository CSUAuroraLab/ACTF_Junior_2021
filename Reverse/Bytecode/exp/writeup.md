  1           0 LOAD_CONST               0 (0)
              2 LOAD_CONST               1 (None)
              4 IMPORT_NAME              0 (hashlib)
              6 STORE_NAME               0 (hashlib)

  2           8 LOAD_CONST               0 (0)
             10 LOAD_CONST               1 (None)
             12 IMPORT_NAME              1 (itertools)
             14 STORE_NAME               1 (itertools)

  3          16 LOAD_CONST               2
             18 STORE_NAME               2 (part1)

  4          20 LOAD_CONST               3
             22 STORE_NAME               3 (part2)

  5          24 LOAD_CONST               4 (32) 								#key = [0x20, 0x21, 0x0a, 0x0c, 0x07, 0x0f]
             26 LOAD_CONST               5 (33)
             28 LOAD_CONST               6 (10)
             30 LOAD_CONST               7 (12)
             32 LOAD_CONST               8 (7)
             34 LOAD_CONST               9 (15)
             36 BUILD_LIST               6
             38 STORE_NAME               4 (key)

  6          40 LOAD_NAME                5 (input)						    #tmp = input("Part2 of flag:")
             42 LOAD_CONST              10 ('Part2 of flag:')
             44 CALL_FUNCTION            1
             46 STORE_NAME               6 (tmp)

  7          48 LOAD_NAME                7 (len)
             50 LOAD_NAME                6 (tmp)
             52 CALL_FUNCTION            1
             54 LOAD_CONST               8 (7)
             56 COMPARE_OP               4 (>)
             58 POP_JUMP_IF_FALSE       76

  8          60 LOAD_NAME                8 (print)							#print("Part2 no more than 7 characters!")
             62 LOAD_CONST              11 ('Part2 no more than 7 characters!')
             64 CALL_FUNCTION            1
             66 POP_TOP

  9          68 LOAD_NAME                9 (exit)
             70 LOAD_CONST               0 (0)
             72 CALL_FUNCTION            1
             74 POP_TOP

 10     >>   76 BUILD_LIST               0
             78 STORE_NAME              10 (input1)

 11          80 SETUP_LOOP              44 (to 126)
             82 LOAD_NAME                6 (tmp)
             84 LOAD_CONST               0 (0)
             86 LOAD_CONST              12 (6)
             88 BUILD_SLICE              2
             90 BINARY_SUBSCR
             92 GET_ITER
        >>   94 FOR_ITER                28 (to 124)
             96 STORE_NAME              11 (i)

 12          98 LOAD_NAME               12 (str)
            100 LOAD_NAME               13 (int)
            102 LOAD_NAME               11 (i)
            104 LOAD_CONST               6 (10)
            106 CALL_FUNCTION            2
            108 CALL_FUNCTION            1
            110 STORE_NAME              14 (t)

 13         112 LOAD_NAME               10 (input1)
            114 LOAD_ATTR               15 (append)
            116 LOAD_NAME               14 (t)
            118 CALL_FUNCTION            1
            120 POP_TOP
            122 JUMP_ABSOLUTE           94
        >>  124 POP_BLOCK

 14     >>  126 LOAD_NAME                5 (input)
            128 LOAD_CONST              13 ('Part1 of flag:')
            130 CALL_FUNCTION            1
            132 STORE_NAME              16 (input2)

 15         134 LOAD_NAME               16 (input2)								#temp = input2 + ''.join(input1) + '}'
            136 LOAD_CONST              14 ('')
            138 LOAD_ATTR               17 (join)
            140 LOAD_NAME               10 (input1)
            142 CALL_FUNCTION            1
            144 BINARY_ADD
            146 LOAD_CONST              15 ('}')
            148 BINARY_ADD
            150 STORE_NAME              18 (temp)

 16         152 LOAD_NAME                2 (part1)								#flag = part1 + part2
            154 LOAD_NAME                3 (part2)
            156 BINARY_ADD
            158 STORE_NAME              19 (flag)

 17         160 LOAD_NAME                0 (hashlib)							#hash1 = hashlib.sha1(flag.encode('utf-8'))
            162 LOAD_ATTR               20 (sha1)
            164 LOAD_NAME               19 (flag)
            166 LOAD_ATTR               21 (encode)
            168 LOAD_CONST              16 ('utf-8')
            170 CALL_FUNCTION            1
            172 CALL_FUNCTION            1
            174 STORE_NAME              22 (hash1)

 18         176 LOAD_NAME                0 (hashlib)							#hash2 = hashlib.sha1(temp.encode('utf-8'))
            178 LOAD_ATTR               20 (sha1)
            180 LOAD_NAME               18 (temp)
            182 LOAD_ATTR               21 (encode)
            184 LOAD_CONST              16 ('utf-8')
            186 CALL_FUNCTION            1
            188 CALL_FUNCTION            1
            190 STORE_NAME              23 (hash2)

 19         192 LOAD_NAME               22 (hash1)
            194 LOAD_ATTR               24 (hexdigest)
            196 CALL_FUNCTION            0
            198 LOAD_NAME               23 (hash2)
            200 LOAD_ATTR               24 (hexdigest)
            202 CALL_FUNCTION            0
            204 COMPARE_OP               2 (==)
            206 POP_JUMP_IF_FALSE      218

 20         208 LOAD_NAME                8 (print)							#if hash1.hexdigest() == hash2.hexdigest():  print("You are right!")
            210 LOAD_CONST              17 ('You are right!')
            212 CALL_FUNCTION            1
            214 POP_TOP
            216 JUMP_FORWARD            16 (to 234)

 22     >>  218 LOAD_NAME                8 (print)
            220 LOAD_CONST              18 ('Try again!')
            222 CALL_FUNCTION            1
            224 POP_TOP

 23         226 LOAD_NAME                9 (exit)
            228 LOAD_CONST               0 (0)
            230 CALL_FUNCTION            1
            232 POP_TOP

 24     >>  234 LOAD_NAME               22 (hash1)				#hash1 = hash1.hexdigest().encode()
            236 LOAD_ATTR               24 (hexdigest)
            238 CALL_FUNCTION            0
            240 LOAD_ATTR               21 (encode)
            242 CALL_FUNCTION            0
            244 STORE_NAME              22 (hash1)

 25         246 LOAD_CONST               5 (33)							#enc2 = [0x21]
            248 BUILD_LIST               1
            250 STORE_NAME              25 (enc2)

 26         252 SETUP_LOOP              46 (to 300)
            254 LOAD_NAME               26 (range)
            256 LOAD_CONST               0 (0)
            258 LOAD_NAME                7 (len)
            260 LOAD_NAME               22 (hash1)
            262 CALL_FUNCTION            1
            264 CALL_FUNCTION            2
            266 GET_ITER
        >>  268 FOR_ITER                28 (to 298)
            270 STORE_NAME              11 (i)

 27         272 LOAD_NAME               25 (enc2)							#for i in range(0, len(hash1)):  enc2.append(hash1[i] ^ enc2[i])
            274 LOAD_ATTR               15 (append)
            276 LOAD_NAME               22 (hash1)
            278 LOAD_NAME               11 (i)
            280 BINARY_SUBSCR
            282 LOAD_NAME               25 (enc2)
            284 LOAD_NAME               11 (i)
            286 BINARY_SUBSCR
            288 BINARY_XOR
            290 CALL_FUNCTION            1
            292 POP_TOP
            294 EXTENDED_ARG             1
            296 JUMP_ABSOLUTE          268
        >>  298 POP_BLOCK

 28     >>  300 LOAD_NAME                8 (print)
            302 LOAD_CONST              19 ('enc2:')
            304 LOAD_NAME               25 (enc2)
            306 CALL_FUNCTION            2
            308 POP_TOP

 29         310 LOAD_CONST              20 (<code object <listcomp> at 0x000001CB39F58ED0, file "test.py", line 29>)				
            312 LOAD_CONST              21 ('<listcomp>')				#enc1 = [ord(m) ^ k for m, k in zip(part1, itertools.cycle(key))]
            314 MAKE_FUNCTION            0
            316 LOAD_NAME               27 (zip)
            318 LOAD_NAME                2 (part1)
            320 LOAD_NAME                1 (itertools)
            322 LOAD_ATTR               28 (cycle)
            324 LOAD_NAME                4 (key)
            326 CALL_FUNCTION            1
            328 CALL_FUNCTION            2
            330 GET_ITER
            332 CALL_FUNCTION            1
            334 STORE_NAME              29 (enc1)

 30         336 LOAD_NAME                8 (print)
            338 LOAD_CONST              22 ('enc1:')
            340 LOAD_NAME               29 (enc1)
            342 CALL_FUNCTION            2
            344 POP_TOP
            346 LOAD_CONST               1 (None)
            348 RETURN_VALUE

#flag = actf{Pyth0n_byt3c0de_114514}