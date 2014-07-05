NetPublisher
=========
desription: http://dev.chrns.com/2014/07/netpublisher.html

**step 1.** install packages

```sh
sudo apt-get install apache2 xclip nautilus-actions
```

**step 2.** setup starage

```sh
mkdir -p ~/files/public
sudo ln -s ~/files/public /var/www/html/public
```

**step 3.** copy scripts

* properties.py
* publisher.py
* [pyperclip.py]

```sh
mkdir ~\.scripts
```

**step 4.** configure nautilus contex menu

```sh
nautilus-actions-config-tool
```

> Parameters : ['copy' or 'move'] [%d] [%b]

> Example: _copy %d %b_

**step 5.** configure _properties.py_
```python
# storage folder
public_dir='/home/chrns/files/public/'
# 'properties' -> from 'ip'
# 'system' -> call get_interface_ip() with 'interface'
get_ip_from='system'
# nae of interface: 'eth0', 'eth1', ..., 'wlan0', etc.
interface='wlan0'
# ip (optional)
ip='127.0.0.1'
# protocol
protocol='http'
# with or without port
enable_port=False
# port (optional)
port=80
```
[pyperclip.py]:http://coffeeghost.net/2010/10/09/pyperclip-a-cross-platform-clipboard-module-for-python/
