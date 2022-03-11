import random
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
from hello.domains import memberlist, myRandom, my100
from quiz00 import Quiz00


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

    @staticmethod
    def quiz25dictcom() -> str:
        # memberlist()[myRandom(0,23)] 이것이 한 명인데 5명 추출
        # scores는 0~100점 사이 랜덤
        q6 = Quiz00
        students = set([q6.quiz06memberChoice() for i in range(5)])
        scores = ([myRandom(0, 100) for i in range(5)])
        while len(students) < 5:
            students.add(q6.quiz06memberChoice())
        res = dict(zip(students, scores))
        print(res)

        return None

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
        c = [(i, j) for i, j in enumerate([])]
        d = ''.join([])
        e = {i:j for i, j zip (l1, l2)} 
        e2 = dict(zip(l1, l2))
        f = list(zip(l1, l2))
        '''
        return None

    def quiz28dataframe(self) -> None:
        dt = self.quiz24zip()
        df = pd.DataFrame.from_dict(dt, orient='index')
        print(df)
        df.to_csv('./save/bugs.csv', sep=',', na_rep='NaN')

    def quiz29_pandas_01(self) -> str:
        a = []
        b = []
        c = [chr(i) for i in range(97, 100)]  # ['a', 'b', 'c']
        [a.append(i) if i % 2 == 0 else b.append(i) for i in range(1, 7)]
        dict = {'1': b, '2': a}
        df3 = pd.DataFrame.from_dict(dict, orient='index', columns=c)
        print(df3)