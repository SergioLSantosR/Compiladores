; ModuleID = 'MiniLang'

declare i32 @printf(i8*, ...)

@.str.int = private unnamed_addr constant [4 x i8] c"%d\0A\00", align 1

define i32 @main() {
entry:
  %x = alloca i32
  store i32 10, i32* %x
  %y = alloca i32
  store i32 20, i32* %y
  %z = alloca i32
  store i32 0, i32* %z
  %t1 = load i32, i32* %x
  %t2 = load i32, i32* %y
  %t3 = mul i32 %t2, 2
  %t4 = add i32 %t1, %t3
  store i32 %t4, i32* %z
  %t5 = load i32, i32* %z
  %call1 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.int, i32 0, i32 0), i32 %t5)
  %t6 = load i32, i32* %x
  %t7 = icmp sgt i32 %t6, 10
  %t8 = zext i1 %t7 to i32
  %t9 = load i32, i32* %y
  %t10 = icmp slt i32 %t9, 20
  %t11 = zext i1 %t10 to i32
  %t13 = icmp ne i32 %t8, 0
  %t14 = icmp ne i32 %t11, 0
  %t15 = or i1 %t13, %t14
  %t12 = zext i1 %t15 to i32
  %t16 = icmp ne i32 %t12, 0
  br i1 %t16, label %L1, label %L2

L1:
  %t17 = load i32, i32* %x
  %t18 = sdiv i32 %t17, 2
  store i32 %t18, i32* %z
  br label %L3

L2:
  %t19 = load i32, i32* %y
  %t20 = sub i32 %t19, 5
  store i32 %t20, i32* %z
  br label %L3

L3:
  %t21 = load i32, i32* %z
  %call2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.int, i32 0, i32 0), i32 %t21)
  %i = alloca i32
  store i32 0, i32* %i
  br label %L4

L4:
  %t22 = load i32, i32* %i
  %t23 = icmp slt i32 %t22, 5
  %t24 = zext i1 %t23 to i32
  %t25 = icmp ne i32 %t24, 0
  br i1 %t25, label %L5, label %L6

L5:
  %t26 = load i32, i32* %i
  %call3 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.int, i32 0, i32 0), i32 %t26)
  %t27 = load i32, i32* %i
  %t28 = add i32 %t27, 1
  store i32 %t28, i32* %i
  br label %L4

L6:
  %j = alloca i32
  store i32 0, i32* %j
  br label %L7

L7:
  %t29 = load i32, i32* %j
  %t30 = icmp slt i32 %t29, 3
  %t31 = zext i1 %t30 to i32
  %t32 = icmp ne i32 %t31, 0
  br i1 %t32, label %L8, label %L10

L8:
  %t33 = load i32, i32* %j
  %call4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.int, i32 0, i32 0), i32 %t33)
  br label %L9

L9:
  %t34 = load i32, i32* %j
  %t35 = add i32 %t34, 1
  store i32 %t35, i32* %j
  br label %L7

L10:
  ret i32 0
}