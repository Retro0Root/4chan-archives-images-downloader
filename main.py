import urllib3
from bs4 import BeautifulSoup
import sys
import os
import re
import random
import string
from PIL import Image
import csv


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def remove_char(str, n):
    first_part = str[:-n]
    last_part = str[-n + 1:]
    return first_part + last_part


def check_integrity(path):
    try:
        img = Image.open(path)
        img.verify()
    except (IOError, SyntaxError) as e:
        print('Bad file:', path)
        os.remove(path)


def check_size(path):
    try:
        img = Image.open(path)
        width, height = img.size

        if height <= 1080:
            os.remove(path)

    except (IOError, SyntaxError, FileNotFoundError) as e:
        print('Bad path:', path)


def download_images(url, category):
    # Get source code
    http = urllib3.PoolManager()
    response = http.request('GET', url)

    # Get images
    soup_mysite = BeautifulSoup(response.data, 'html.parser')
    images = soup_mysite.find_all("img", {"class": "post_image"})

    # Get thread Number
    regex = r"(?<=\/)[^\/]*(?=\/[^\/]*$)"
    matches = re.findall(regex, url, re.MULTILINE)
    threadNumber = matches[0]

    # Create folder to download images
    exist = os.path.exists(defaultPath + "/Images/")
    if exist is False:
        os.mkdir(defaultPath + "/Images/")

    # Create sub folder
    exist = os.path.exists(defaultPath + "/Images/" + category)
    if exist is False:
        os.mkdir(defaultPath + "/Images/" + category)

    # Create sub folder of the thread
    exist = os.path.exists(defaultPath + "/Images/" + category + "/" + threadNumber)
    if exist is False:
        os.mkdir(defaultPath + "/Images/" + category + "/" + threadNumber)

    pathToSave = defaultPath + "/Images/" + category + "/" + threadNumber

    for image in images:
        regex = r"thumb(.*)"
        matches = re.findall(regex, image.attrs['src'], re.MULTILINE)
        tmp = remove_char(matches[0], 5)
        finalPath = pathToSave + "/" + get_random_string(10) + ".jpg"
        urlImage = "https://thebarchive.com/data/b/image" + tmp
        os.system("wget -O {0} {1}".format(finalPath, urlImage))
        # time.sleep(random.randint(0, 5))
        check_integrity(finalPath)
        check_size(finalPath)


# Arguments
try:
    url = sys.argv[1]
    defaultPath = os.getcwd()
    pattern = ".csv"

    if pattern in url:
        with open(url, "r") as infile:
            read = csv.reader(infile)
            for row in read:
                print(row[0])
                download_images(row[0], row[1])
    else:
        try:
            category = sys.argv[2]
            download_images(url, category)
        except IndexError as ie:
            print("Category is missing.")
            print("---------------------------------")
            print("Run : ")
            print("python3 main.py <URL> <Category>")
            print("or")
            print("python3 main.py <CSV File>")

except IndexError as ie:
    print("Arguments are necessaries !")
    print("---------------------------------")
    print("Run : ")
    print("python3 main.py <URL> <Category>")
    print("or")
    print("python3 main.py <CSV File>")

