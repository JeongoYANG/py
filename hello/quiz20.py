import random
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen

from hello.domains import memberlist, myRandom, my100


class Quiz20:

    def quiz20list(self) -> str:
        return None

    def quiz21tuple(self) -> str:
        return None

    def quiz22dict(self) -> str:
        return None

    def quiz23listcom(self) -> str:
        print('---------- legacy ----------')
        a = []
        for i in range(5):
            a.append(i)
        print(a)
        print('---------- comprehension ----------')
        a2 = [i for i in range(5)]
        print(a2)
        return None

    def quiz24zip(self) -> str:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml')  # html.parser vs lxml
        ls1 = self.find_music(soup, 'title')
        ls2 = self.find_music(soup, 'artist')
        dict = {}
        for i in range(0, len(ls1)):
            print(type(f'타입: {ls1[i]}'))
            dict[ls1[i]] = ls2[i]
        print(dict)
        return None

    def print_music_list(self, soup):
        artists = soup.find_all('p', {'class': 'artist'})
        # print(type(artists)) # <class 'bs4.element.ResultSet'>
        artists = [i.get_text() for i in artists]
        # print(type(artists))
        print(''.join(i for i in artists))
        titles = soup.find_all('p', {'class': 'title'})
        titles = [i.get_text() for i in titles]
        print(''.join(i for i in titles))

    def find_rank(self, soup):
        for i, j in enumerate(['artist', 'title']):
            for i, j in enumerate(self.find_music(soup, j)):
                print(f'{i}위 : {j}')
            print('#' * 100)

    @staticmethod
    def find_music(soup, cls_nm) -> []:
        ls = soup.find_all('p', {'class': cls_nm})
        return [i.get_text() for i in ls]

    def quiz25dictcom(self) -> str:
        # memberlist()[myRandom(0,23)] 이것이 한 명인데 5명 추출
        # scores는 0~100점 사이 랜덤
        students = [memberlist()[myRandom(0, 23)] for i in range(5)]
        scores = [str(my100()) for i in range(5)]
        dict = {}
        for i, j in zip(students, scores):
            dict[i] = j
        print(dict)

    def quiz26map(self) -> str:
        return None

    def quiz27melon(self) -> str:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')
        '''
        a = [i if i == 0 or i ==0 else i for i in range()]
        b = [ i if i ==0 or i ==0 else i for i in []]
        c = [(i,j) for i,j in enumerate([])]
        d = ''.join(i for i in [])
        '''
        return None

    def quiz28(self) -> str:

        return None

    def quiz29(self) -> str:
        return None
