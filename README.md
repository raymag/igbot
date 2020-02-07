# IGBOT
Instagram bot for following users that doesn't follow you back.

## Installing
First you have to set up the chrome webdriver which can be found [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).   You also need to include the webdriver exectuable in the PATH variable.  

Then you must install the selenium package with the following command.  
```pip install selenium```

If you wish, you can install all dependecies from the requirements file.  
```pip install -r requirements.txt```

## Running
You must then set up the secret file with your account password and your username at the end of the main.py file.  
Finally you can use the following command to run the bot.  
```python main.py```

We strongly recommend you to use the interactive mode. To do so, run the following instead.  
```python -i main.py```
