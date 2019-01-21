import lxml.html
import requests
import string, datetime, os, csv, time, random


def main():
    # url = 'https://www.grousemountain.com/current_conditions'
    # response = requests.get(url)
    # tree = lxml.html.fromstring(response.text)
    tree = lxml.html.parse('sample.html').getroot()
    rows = tree.xpath("//table[@id ='players']//tr")
    table = []
    for row in rows[1:]:
        data = []
        td = row.xpath('./td')
        for t in td:
            data.append(t.text_content())
        print(data)
        table.append(data)

if __name__ == '__main__':
    main()
