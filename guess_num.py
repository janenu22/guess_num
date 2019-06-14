import random
import random
num = random.randint(1, 100)
count = 0
while True:
	count += 1
	a = input('請輸入1~100之間的 一個數字:')
	a = int(a)
	if a == num:
		if count<7:
			print('你才猜了',count,'次，就猜對了!')
		else:
			print('你猜了',count,'次才猜對。')
		break
	elif a > num:
		print('這個數字太大了!')
	else:
		print('這個數字太小了!')