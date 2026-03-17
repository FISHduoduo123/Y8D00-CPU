mov r1 #1 addr_3
mov r2 #1 addr_3
mov r3 #20 addr_3
mov r4 #10 addr_3

sub r5 r3 r1 addr_1
sub r6 r4 r2 addr_1

add r8 r5 r5 addr_1
add r9 r6 r6 addr_1

add r7 r6 r6 addr_1
sub r7 r7 r5 addr_1

mov r10 r1 addr_1
mov r11 r2 addr_1

mov [off:0,154] r10 addr_5
mov [off:0,155] r11 addr_5
or r11 r11 #64 addr_3
mov [off:0,155] r11 addr_5
or r11 r11 #32 addr_3
mov [off:0,155] r11 addr_5
and r11 r11 #31 addr_3
mov [off:0,155] r11 addr_5

sub r12 r10 r3 addr_1
and r0 r12 #128 addr_3
br jz r0 [42]

add r10 r10 #1 addr_3

and r0 r7 #128 addr_3
br jz r0 [29]

add r7 r7 r9 addr_1
jp r0 [33]

add r7 r7 r9 addr_1
sub r7 r7 r8 addr_1
add r11 r11 #1 addr_3
jp r0 [33]

mov [off:0,154] r10 addr_5
mov [off:0,155] r11 addr_5
or r11 r11 #64 addr_3
mov [off:0,155] r11 addr_5
or r11 r11 #32 addr_3
mov [off:0,155] r11 addr_5
and r11 r11 #31 addr_3
mov [off:0,155] r11 addr_5

jp r0 [21]

jp r0 [42]
