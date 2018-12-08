import re 
file_obj=open("email.txt",'r')
while True:
	file_read=file_obj.readline()
	if file_read=="":
		break
	else:
		print(type(file_read))
		regex= "[a-zA-Z0-9]+@[a-z]+.[a-z]+"
		match_obj = re.search(regex,file_read)
		if match_obj:
			print("EMAIL : {}".format(match_obj.group(0)))
		else:
			print("match not found")
		print(file_read)
		