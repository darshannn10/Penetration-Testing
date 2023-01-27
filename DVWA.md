#### Prerequisites: 
- Hypervisor: VirtualBox or VMWare
- Linux Distro: Kali Linux or ParrotOS ( or any Linux Distribution)


## Steps to Download and Install DVWA
1. Setting Up a Web server (Install Apache)
- To install `Apache`, Open Your Terminal and type the following
```
sudo apt install apache2
```
- Once done, type `127.0.0.1` in the browser and you will see the default `Apache 2 web page`, similar to this:

![apache](https://user-images.githubusercontent.com/87711310/215119060-661771b0-0398-42f8-a697-13e0a2d59b6e.png)


- When you are done looking at this test page, you can remove it by typing the following command:

```
sudo rm /var/www/html/info.html
```


2. Download DVWA
Now, we need to download the archive of `DVWA` from `Github`

- To install `Git`, type the following command:
```
sudo apt-get install git
```

- Go to the `apache2` folder.
```
cd /var/www/html/
```

- Clone `DVWA` from `Github`, type the following command:
```
sudo git clone https://github.com/digininja/DVWA
```

Once done, type `127.0.0.1/DVWA/` in the browser and you will see the `DVWA` page, similar to this:

![dvwa-test-page](https://user-images.githubusercontent.com/87711310/215119068-4d707482-a4d9-4d51-a283-3d6e04a7494e.png)


- Change permissions for DVWA
```
sudo chmod -R 777 /var/www/html/DVWA/
```

3. Install MySQL
The next component for Setting up DVWA is Installing MySQL.

- To install MySQL, type the following:
```
sudo apt install mysql-server
```

__Note__: the installation routine may ask you to create a new password for the `root` MySQL user. Once you have completed all of the required steps, your MySQL installation should be completed. Let’s double-check that our new MySQL server is running. Type this command:
```
mysql -u root -p
```

Enter the root password you created for MySQL when you installed the software package. Once in, the following to get the server status, version information and more:
```
status
```

This is a good way to ensure that you’ve installed MySQL and are ready for further configuration.

- Now, you'd need to restart the `Apache` Server
```
sudo service apache2 restart
```

- Then, you'd need to create a Database and a User in MySQL database. Follow these steps:

```
mysql -u root -p

Type the MySQL root password, and then press Enter.
```

- To create a database, type the following command:
```
CREATE DATABASE dvwadb;
```

- To create a database user, type the following command. Replace `dvwausr` with the user you want to create, and replace `dvwa@123` with the user’s password:
```
CREATE USER 'dvwausr'@'127.0.0.1' IDENTIFIED BY 'dvwar@123';
```

- To grant permission, type the following command:
```
GRANT ALL PRIVILEGES ON dvwadb.* TO ‘dvwausr’@’localhost’ IDENTIFIED BY ‘dvwa@123’;
```

- Once done, exit the application by typing either of the following commands:
```
\q or exit
```

4. Install PHP5
For the last component in __DVWA__ installation, we need to set up and install `PHP`. Installing `PHP` is very easy.

- To install PHP, simply type the following command:
```
sudo apt install php5
OR
sudo apt install php5.6
```

- Agree to the installation and `PHP5` will be installed on your Server.

- Now, you'd again need to restart the Apache Server 
```
sudo service apache2 restart
```

- Now, you'd probably need to test the PHP software that you just installed. Move into your `public web directory`:
```
cd /var/www/html
```
- Once there, use the text editor to create a file named `info.php` by typing the following command:
```
sudo nano info.php
```

- This command will use the command line editor `nano` to open a new blank file with this name. Inside this file, type the following:
```php
<?php phpinfo(); ?>
```
- Save the changes and exit the nano editor.

- Once done, open your web browser and type your localhost IP address in the browser.
```
http://127.0.0.1/info.php
```

- If everything you've done until now was correct, then you'll see the default PHP information page, similar to this:

![phpinfo](https://user-images.githubusercontent.com/87711310/215119213-b282f802-f7b6-4c6d-8470-330865489015.png)

- Now, that we're done installing php, we need to install `MySQL` extention for `PHP`.
```
sudo apt install php5-mysql
```

- Once done, you have completed the `PHP` installation required for `DVWA`.

- DVWA requires a module for php which is not installed into Kali Linux or ParrotOS. So we need to add a Debian source for APT.
```
sudo add-apt-repository ''http://ftp.de.debian.org/debian sid main'
sudo apt update
sudo apt install php5-gd
```

- Once done, you have completed the PHP installation for DVWA.

5. Configuring DVWA
Now, that we're done installing all the components required to run `DVWA`, we can move on to edit the source-code of `PHP config` files to make sure that the web app connects to the database.
```
sudo nano /var/www/html/dvwa/config/config.inc.php.dist
```

- Add the database `name`, `user`, and `password` of the mysql database.
- Here’s a screenshot on how your file needs to be after editing.

![db](https://user-images.githubusercontent.com/87711310/215119033-b9b2cd27-6168-4fc3-b158-1a6b047fd935.png)

- Once done, we need to edit the main `config (php.ini)` file for `apache2`, which is not correctly overridden for `DVWA` by default.
```
sudo nano /etc/php5/apache2/php.ini
```

- Enable `Allow_url_fopen`

- Enable `Allow_url_include`

- This is necessary to exploit the file upload vulnerability. Here’s a screenshot for `php.ini` after making changes.
 
![include](https://user-images.githubusercontent.com/87711310/215119052-a1dd7d1c-aa5a-4cfc-9c4a-0e0759e68d56.png)

- After saving changes for php.ini, we need to follow a few more steps.
```
sudo apt install iceweasel
```

- Restart Apache
```
sudo /etc/init.d/apache2 restart
```

- Restart MySQL Service
```
sudo /etc/init.d/mysql restart
```

Once done, you have completed the required configuration for DVWA.

To test `DVWA` installation

```
iceweasel http://127.0.0.1/DVWA/setup.php
```

You will be redirected to the web browser and the page similar to this will be in front of you.

![setup](https://user-images.githubusercontent.com/87711310/215120308-4b423024-f553-460c-bf15-eacacbda6d24.png)

- When you are done looking at this DVWA Setup page, you can click on `Create / Reset` Database button. You will be redirected to the login page.

- Use `MySQL` User and Password to Login

- Now, login to change the strength of vulnerabilities by clicking on “DVWA Security”.

