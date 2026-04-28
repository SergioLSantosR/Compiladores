; === Código principal ===
x = 10
y = 20
z = 0
t1 = y * 2
t2 = x + t1
z = t2
print z
t3 = x > 10
t4 = y < 20
t5 = t3 || t4
if t5 == false goto L1
t6 = x / 2
z = t6
goto L2
L1:
t7 = y - 5
z = t7
L2:
print z
i = 0
L3:
t8 = i < 5
if t8 == false goto L4
print i
t9 = i + 1
i = t9
goto L3
L4:
j = 0
L5:
t10 = j < 3
if t10 == false goto L6
print j
t11 = j + 1
j = t11
goto L5
L6:
; Fin del programa