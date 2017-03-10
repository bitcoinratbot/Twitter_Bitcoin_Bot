Twitter Bot Bitcoin Development Running In Python

### Setting up bitcoin python module

## Installing the modules that are required

```
git clone https://github.com/laanwj/bitcoin-python
```

### Then run the following commands to install

```
cd bitcoin-python
sudo python setup.py build
sudo python setup.py install
```

```
git clone https://github.com/petertodd/python-bitcoinlib
```

### Then run the following commands to install

```
cd python-bitcoinlib
sudo python setup.py build
sudo python setup.py install
```

### Setting up one of the twitter modules

```
pip install twython
```

### Setting up the other twitter module

```
git clone https://github.com/tweepy/tweepy.git
cd tweepy
sudo python setup.py install
```

## You have to also execute the .py file like you would with a bash script

### sudo chmod +x ./hello.py ./code.py ./newupdate.py ./block.py

command to put in bitcoin.conf
### blocknotify='location of the file' %s

