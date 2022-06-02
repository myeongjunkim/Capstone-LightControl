import requests
from bs4 import BeautifulSoup
import time



request_url = 'https://www.google.com/search?q=kfc+logo&tbm=isch&ved=2ahUKEwjz2b3x6MD3AhUqIqYKHXufAAsQ2-cCegQIABAA&oq=kfc+logo&gs_lcp=CgNpbWcQARgAMgUIABCABDIFCAAQgAQyBQgAEIAEMgQIABAeMgQIABAeMgQIABAeMgQIABAeMgQIABAeMgQIABAeMgQIABAeOgcIIxDvAxAnOgQIABAYOggIABCABBCxAzoLCAAQgAQQsQMQgwE6CAgAELEDEIMBOgoIIxDvAxDqAhAnUI8hWPg3YIA6aAJwAHgAgAFyiAGMCZIBBDEuMTCYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABCsABAQ&sclient=img&ei=3M5vYvP7C6rEmAX7voJY&bih=694&biw=1440'
source = requests.get(request_url)
soup = BeautifulSoup(source.text, 'html.parser')

selector = 'img'
img_list = soup.select(selector)

img_list = img_list[1:]



# urllib.request.urlretrieve(img_list[0]["src"], "./test.png")


i = 0
start = time.time()
for img in img_list:
    # print(img["src"])
    img_file = requests.get(img['src'])
    with open(f"./img/kfc_logo{i}.jpg", "wb") as photo:
        photo.write(img_file.content)
    i +=1
end = time.time()

print(end-start)

