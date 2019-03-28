
def large_add(num1, num2):

	num1 = list(str(num1))							#先转变为str,再转为list，元素为字符
	num1 = [int(i) for i in num1]
	num2 = list(str(num2))
	num2 = [int(i) for i in num2]
	print(num1)
	print(num2)
	
	num1 = list(reversed(num1))						#再反转列表
	num2 = list(reversed(num2))
	print(num1)
	print(num2)
	
	len1 = len(num1)								#计算最大长度
	len2 = len(num2)
	if len1 > len2:									#并用零把两个列表补齐
		for i in range(len2,len1):
			num2.append(0)
	else:
		for i in range(len1,len2):
			num1.append(0)
	print(num1)
	print(num2)
	
	for i in range(len(num1)-1):							#开始相加：补齐后位数相等
			num1[i] = num1[i]+num2[i]
			if num1[i] > 9:
				num1[i]-= 10
				num1[i+1]+=1
	num1[-1] = num1[-1]+num2[-1]
	if num1[-1] > 9:
		num1[-1]-=10
		num1.append(1)
		
	num1 = list(reversed(num1))					#再反转回去
	
	sum = 0
	for i in num1:
		sum = sum*10 + i
	
	return sum

def main():
	
	num1 = input("请输入第一个大数：")
	num2 = input("请输入第二个大数：")
	try:
		int(num1)
		int(num2)
		print("输入正确")
	except:
		print("输入错误")
		return 
	
	sum = large_add(int(num1),int(num2))
	
	print("大数相加之和为：%d"%sum)


if __name__ == '__main__':
	main()


	
	
	
	
	
	
