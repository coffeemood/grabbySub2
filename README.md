
__GrabbySub2.0 -  Grab your sub from the terminal, and grab the right one! :v: :collision: :rocket:__

_GrabbySub is a small little tool for you :cinema:/:tv: lovers out there who hates scrolling through all hundreds of choices just to find the right language, resolution and uploading version._ 

I technically live in the terminal, so I really find it painful to go through all the old school web browsing just to get my movie subtitle whenever I decide to relax. With that, I decided to write a little script to help me get my subtitle faster and also learn a thing or two from that. This is essentially just a learning tool for me, but if it improves my movie watching experience throughout the process, who cares?.

The first version was written in Bash and so as handy as it was, it wasn't really that swift and user-friendly. Thus, GrabbySub2 is born, built on Python this time. The loading speed is greatly improved, with a much more pleasant user interacting interface. 


# Getting Started

With this update, it truly transformed that sub grabbing process. You just call up the sub-servant, type in your movie/show, pick the specs and bam! You got yourself the right sub. Subscene has the right idea with the open-contribution community, which allows for precision. However, the precision should really come with ease. 


## Prerequisites 

* `Python` - If you didn't have it already, you should download it. 
* `Pip` - The python module downloader 
* `Pup` - HTML parser for shell 

## Installation

We first needs to download a couple of stuffs first

### Install `Brew` (OS X users only) 
	
Open terminal and type: 
	
```shell
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
	
### Download `Python` & `Pip`
	
#### OS X 
	
```shell
brew install python
curl -s -L 'https://bootstrap.pypa.io/get-pip.py' -O 
python get-pip.py
```

#### Linux (Debian) 

```shell
apt-get install python -y 
curl -s -L 'https://bootstrap.pypa.io/get-pip.py' -O 
python get-pip.py
```

#### Linux (RPM) 

```shell 
yum install python
curl -s -L 'https://bootstrap.pypa.io/get-pip.py' -O 
python get-pip.py
```

### Downloading additional modules: 

#### Make sure you run `pip` as root and download all of these modules: 

```shell 
sudo pip install beautifulsoup4 time zipfile re requests
```

#### Lastly, we need to install `pup` HTML-parser: 

If you have Go installed, use: 
```
go get github.com/ericchiang/pup
```

For OS X users, use 
```
brew install https://raw.githubusercontent.com/EricChiang/pup/master/pup.rb
```

To build from source, visit [pup's repo](https://github.com/EricChiang/pup/releases/tag/v0.3.9) and download your correct version.

_Note: The packages differ from machine to machine. You might have already gotten them, some people haven\'t so it doesn't hurt to go through this process just to make sure it runs swiftly._


# Usage
	
#### Creating an alias for ease of use: 

```shell 
alias grabby='python ~/Downloads/Grabby2.0.py' 
```
	
Open up terminal, go to your movie directory, and just run `grabby` 

#### Type in your `show | movie` & select the correct season/version
	
![selectmov](http://i.imgur.com/9B9zsxG.png) 
	
#### Select the `type` of media (TV/Mov) and the `Language` 
	
![selectall](http://i.imgur.com/nSm4THG.png)
	
#### Select your `episode` and `resolution`, then pick a link: 
	
![selectres](http://i.imgur.com/Q2wr1zg.png)
	
#### Et voila! :angel: :clap:
	
![download](http://i.imgur.com/ttYJOXP.png)
	
	
# Adding Languages & Encoding Version 

Your language might not be included, or maybe you want to add some vendor specific stuffs like (HDTV, YIFY, DEMAND...) in the res section, don't worry, just do this: 

#### Adding Languages
	
Just fire up your text editor, search for the pattern: `language = [` and add your language there, in quotes of course. 

E.g: 

```python 
language = ["English","Chinese","Arabian","French","Spanish","Danish","German","Vietnamese","etc...."]
```
	
#### Adding resolution
	
Do the same with language, but this time search for: `res = [` and add your resolution there. 

```python
res = ["480p","720p","1080p","HDTV","JYK","etc..."]
```

# Bugs & Improvements


- [ ] Even faster :exclamation: The current version isn't so bad. Version 2.0 runs on python so it's almost double the speed of the first one which was as slow as a bash script can get

- [ ] Work on a GUI, integrate into a small handy taskbar/dock utility which improves users' experience...

- [ ] ... Suggestions :question:

# Contact me

If you have any questions, shoot me a message at coffeeforthoughts@gmail.com 

As always, thanks for reading/using/checking out/frowning :joy_cat: :heart_eyes: :dizzy: :poop:

__All done! Enjoy!__ 