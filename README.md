# Make Python Talk

Dear Readers: 

This is the repository for the book Make Python Talk. You can find all resources for the book here.

Please start the book with the introduction, then Chapter 1, Chapter 2, and so on. Skip a chapter only if you are sure what's covered in it. 
Resources are placed in their own chapter folders such as ch01, ch02... 

In Chapter 3, you'll place all speech-recognition related code in a local module mysr.py so that the main script is short, clean, and concise.
However, you need to place the file mysr.py in the same folder as the script that uses the module.
In Chapter 4, you'll do the same for text-to-speech related code in a local module mysay.py. 

Once you reach Chapter 5, you'll install a custom-made package named mptpkg for the book.
This way, you don’t need to copy and paste local module files such as mysr.py and mysay.py to all individual chapter folders.
This also helps keep the code consistent throughout the book. You’ll learn how a Python package works and how to create one yourself along the way.

In Chapter 7, you'll add more modules to the package mptpkg. Make sure you add the following five lines in /mpt/mptpkg/\_\_init__.py \
from .mywakeup import wakeup \
from .mytimer import timer \
from .myalarm import alarm \
from .myjoke import joke \
from .myemail import email

In Chapter 8, you'll add the know_all module to the package mptpkg. Make sure you add the following in /mpt/mptpkg/\_\_init__.py \
from .myknowall import know_all

In Chapter 17, add the following in /mpt/mptpkg/\_\_init__.py \
from .mymusic import music_play, music_stop \
from .mynews import news_brief, news_stop \
from .myradio import live_radio, radio_stop \
from .myttt import ttt \
from .myconn import conn \
from .mystock import stock_market, stock_price \
from .mytranslate import voice_translate

The appendix discusses how to install modules to play audio files for the book: you need to install either pygame or vlc
in order to have the ability to stop playing audio via voice control; 
you'll also need to install either pydub or playsound
in roder to play audio files so that the script won't go to the next line of code while the audio is playing. 

Should you have any questions or problems, please contact me at mark.liu@uky.edu

Happy coding!
