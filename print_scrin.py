from bs4 import BeautifulSoup
import urllib.request
import random
import string


url_base = 'https://prnt.sc/'


def get_html():
    global url_rand
    url_rand = str(''.join(random.choice(string.digits + string.ascii_lowercase) for _ in range(6)))
    req = str(url_base + url_rand)
    html = urllib.request.urlopen(req).read()
    return html


def main():
    count = input('Pic count: ')
    pic_count = int(count)
    print('Download ' + count + ' pic...')

    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)

    i = 1
    while i <= pic_count:
        html = get_html()
        soup = BeautifulSoup(html, 'html.parser')
        try:
            picture_url = soup.find(id='screenshot-image')['src']
            if picture_url[0] != '/' and picture_url[9] != '.':
                urllib.request.urlretrieve(picture_url, picture_url[40:])
                print (str(i) + ' [' + str(url_rand) + '] - [' + picture_url + '] - DONE!')
                i = i + 1
        except Exception:
            print('ERROR...')


if __name__ == '__main__':
    main()
