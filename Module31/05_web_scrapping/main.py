import requests
import re

if __name__ == "__main__":
    url = 'http://www.columbia.edu/~fdc/sample.html'
    url2 = 'https://ria.ru/20230127/sanktsii-1847775186.html'
    data = requests.get(url).text

    if re.search(r'</h3>', data):
        result = re.findall(r'>(.+?)</h3>', data)
        print(result)
    else:
        print('На данной странице нет тега <h3>.')
