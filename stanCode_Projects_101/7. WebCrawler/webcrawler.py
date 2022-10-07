"""
File: webcrawler.py
Name: Chunya Tsai
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #
        tags = soup.find_all('table', {"class": 't-stripe'})
        total_m = 0                                             # total number of male
        total_f = 0                                             # total number of female
        for tag in tags:
            all_info = tag.tbody.text
            a = all_info.split()
            for i in range(len(a)):
                if i % 5 == 2:
                    total_m += int(string_manipulation(a[i]))
                elif i % 5 == 4:
                    total_f += int(string_manipulation(a[i]))
            print('Male Number: ', total_m)
            total_f -= 2022                                     # 網頁最下面有一個2022位置剛好 %5 == 4 會影響total_f @@
            print('Female Number: ', total_f)


def string_manipulation(s):
    # return string without comma, if s is None, return 0
    ans = ''
    for ch in s:
        if ch.isdigit():
            ans += ch
    if ans != '':
        return ans
    else:
        return 0


if __name__ == '__main__':
    main()
