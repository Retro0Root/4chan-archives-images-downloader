# 4chan archived images downloader

This script allows you to download all images from a archived thread on : https://archived.moe/b/

Images will be saved in the images folder, filtered by category and thread number. 

## What do you need :

You need Python 3 => https://docs.python.org/fr/3/installing/index.html

All requirements are in the requirement.txt file. 

`python -m pip install -r requirements.txt`

Only use the https://archived.moe/b/ website.

That's all (normally).

## Script arguments :

An argument is necessary, you have two choices : 

- The direct url of the thread and the category like this : `python3 main.py https://archived.moe/b/thread/832333440/#834258799 example_category` 
- A CSV file (use the format of example.csv) like this : `python3 main.py example.csv`

Enjoy ! 