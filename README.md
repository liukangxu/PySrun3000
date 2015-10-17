# PySrun3000
A Srun3000 client for BUAA in Python3

## Usage
Modify the server, username and password fields based on your actual situation.

### Windows
    python3 srun3000.py

### OpenWRT
Attention: Python3 requires more than 5MB of free space.

    opkg install python3-light python3-codecs python3-email
    cp srun3000.py /usr/sbin/
    cp srun3000 /etc/init.d/
    chmod /usr/sbin/srun3000.py 755
    chmod /etc/init.d/srun3000 755
    /etc/init.d/srun3000 enable

## License
[The MIT License (MIT)](https://raw.githubusercontent.com/liukangxu/PySrun3000/master/LICENSE)