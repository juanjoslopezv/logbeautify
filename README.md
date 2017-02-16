#Logbeautify.py

## How to use the script ##

To use this script you just need to have python installed on your computer and clone this repo 

After you have cloned the repo navigate using the terminal/command line to the directory you cloned the logbeautify.py

### Example of usage ###

if you have a file in your Desktop named test.txt and let say that has the following content:

test.txt
--------
hello
hello
hellow
important log
bye
bye
bye
--------

and you want to remove all the lines that contain hello you can run the script like this:
```terminal
python logbeautify.py ~/Desktop/test.txt 'hello'

After you run the command you will get and output like this:

```terminal
Reading file  /Users/juanlap/Desktop/test.txt
Script will remove all ocurrences of:  hello
File cleaned saving changes...
Completed, lines removed  3

Now your test.txt file will look like this:

test.txt
--------
important log
bye
bye
bye
--------

I hope this is helpful to someone because it was really helpful for me, please shoot me any comments or questions to juanjo@soyfullstack.com
