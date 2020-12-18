# Ip_Proxy_tool
Get proxy, establish proxy pool, provide ip network interface

# Ip_Proxy_tool

## installation

### Install Python

At least Python3.5 or above

### Install mysql
Configuring MySQL Repository on Debian
To add the MySQL APT repository to your system go to the repository download page and download the latest release package using the following wget command :

```
wget http://repo.mysql.com/mysql-apt-config_0.8.15-1_all.deb
```

Once the download is completed install the release package as a user with sudo privileges :

```
sudo apt install ./mysql-apt-config_0.8.15-1_all.deb
```

You will be presented with the configuration menu from where you can select the MySQL version you want to install.

Update the package list with and install the MySQL server package by running:

```
sudo apt update
sudo apt install mysql-server
```

Once the installation is completed, the MySQL service will start automatically, you can verify it by typing:

```
sudo systemctl status mysql
```

### Securing MySQL 
Run the mysql_secure_installation command to set the root password and to improve the security of the MySQL installation:

```
sudo mysql_secure_installation
```

### Connecting to the MySQL Server

If you selected the default authentication method to log in to the MySQL server as the root user type:

```
sudo mysql
```


Otherwise, if you selected the legacy authentication method to log in type:

```
mysql -u root -p
```

You will be prompted to enter the root password you have previously set when the mysql_secure_installation script was run.


After installation, turn on the mysql service


### Configure proxy pool

```
cd Ip_Proxy_tool
```

Enter the Ip_Proxy_tool directory and modify the settings.py file

Modify mysql username and password


#### Installation dependencies

```
pip3 install -r requirements.txt
```

#### First create a database table

```
python CreateTable.py
```

#user='root', passwd='toor', db='spiders' Note the database, username and password here


Second, open the proxy pool and API

```
python run.py
```

## Get an agent


Use requests to obtain an instance of a method proxy


```
 python get_proxy_example.py

details as follows:

def get_proxy():
    r = requests.get('http://127.0.0.1:5555/random')
    soup = BeautifulSoup(r.text, "lxml")
    trs=soup.find("div",id="container").find_all("tr")
    for tr in trs[1:]:
        IP = tr.find_all("td")[0].get_text()
        PORT = tr.find_all("td")[1].get_text()
    proxies = {
        'http': 'http://' +IP+":"+PORT,
        'https': 'https://' +IP+":"+PORT
    }    
    return proxies
```

If you need to add some other proxy websites, you can modify crawler.py


## Open Proxy Resources

```
https://www.proxyscan.io/
https://spys.one/en/
https://lite.ip2location.com/database/px8-ip-proxytype-country-region-city-isp-domain-usagetype-asn-lastseen
http://www.freeproxylists.net/
http://www.freeproxylists.net/?c=&pt=&pr=HTTPS&a%5B%5D=0&a%5B%5D=1&a%5B%5D=2&u=70
https://hidemy.name/en/proxy-list/
https://www.kuaidaili.com/free/
https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-1
http://www.us-proxy.org/
http://spys.me/proxy.txt
```
