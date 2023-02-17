# CSRF - Cross Site Request Forgery

### What is Cross Site Request Forgery?

Cross Site Request Forgery is an attack where the attacker causes the victim user to carry out an action unintentionally while that user is authenticated.


			Attacker                                 		Victim               			   Web Application
									  				 
	https://domain.com/email/change?email=attacker@gmail.com  --->		Cookie	   --->		  	https://domain.com/email/change?email=attacker@gmail.com  								    
			            |___________________________________________________________________________________________|																		     

## End Points :
	
	Login
	Logout
	Reset Password
	Channge Password
	Add-Cart
	Like
	Comment
	Profile change
	User details change
	Balance Transffer
	Subcription

## Bypass CSRF/XSRF

	-Change Request Method [POST => GET]

	-Remove Total Token Parameter

	-Remove The Token, And Give a Blank Parameter

	-Copy a Unused Valid Token , By Dropping The Request and Use That Token

	-Use Own CSRF Token To Feed it to Victim

	-Replace Value With Of A Token of Same Length 

	-Reverse Engineer The Token

	-Extract Token via HTML injection

	-Switch From Non-Form `Content-Type: application/json` or `Content-Type: application/x-url-encoded` To `Content-Type: form-multipart`

	-Change/delete the last or frist character from the token

	-Change referrer to Referrer

	-Bypass the regex
 
## References

[OWASP](https://owasp.org/www-community/attacks/csrf)

[PortSwigger](https://portswigger.net/web-security/csrf)

[Acunetix](https://www.acunetix.com/websitesecurity/csrf-attacks/)

[Medium Writeup](https://medium.com/swlh/intro-to-csrf-cross-site-request-forgery-9de669df03de)

[Medium Writeup](https://medium.com/swlh/attacking-sites-using-csrf-ba79b45b6efe)

[Medium Writeup](https://medium.com/swlh/bypassing-csrf-protection-c9b217175ee)
	
## H1 Reports

[HackerOne](https://hackerone.com/reports/834366)

[HackerOne](https://hackerone.com/reports/419891)

[HackerOne](https://hackerone.com/reports/127703)

[HackerOne](https://hackerone.com/reports/177472)

[HackerOne](https://hackerone.com/reports/152569)

[HackerOne](https://hackerone.com/reports/293016)

[HackerOne](https://hackerone.com/reports/339352)

