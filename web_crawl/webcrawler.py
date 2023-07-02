"""
File: webcrawler.py
Name: Andy
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
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
        male = 0   # male number
        female = 0  # female number
        for tr in soup.tbody.find_all("tr"):   # get all tr label content
            x = tr.text.split()
            if len(x) == 5:  # get rank data
                a1 = x[2].split(",")   # deal with male number data
                a1 = int(a1[0])*1000 + int(a1[1])
                male += a1
                a2 = x[4].split(",")   # deal with female number data
                a2 = int(a2[0]) * 1000 + int(a2[1])
                female += a2
        print("Male Number:" + str(male))
        print("Female Number:" + str(female))


if __name__ == '__main__':
    main()
