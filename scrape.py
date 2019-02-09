import lxml.html
import requests
import string, datetime, os, csv, time, random,sys

# Set time in between requests
SLEEP_TIME = 86000 # 1 day
SLEEP_TIME_BUFFER = 800 # 15 mins


csv_name = 'mvp_probabilities.csv'
schema = ['Date','Rk','Player','Tm','W','L','W/L%', 'G','GS', 'MP','FG','FGA','FG%','3P','3PA','3P%','2P','2PA','2P%','eFG%', 'FT', 'FTA','FT%', 'ORB','DRB','TRB','AST','STL','BLK','TOV','PF','PTS','Prob%']


def main(*args):
    url = 'https://www.basketball-reference.com/friv/mvp.html'

    while True:



        response = requests.get(url)
        tree = lxml.html.fromstring(response.text)
        #tree = lxml.html.parse('sample.html').getroot()
        rows = tree.xpath("//table[@id ='players']/tbody//tr")
        table = []
        for row in rows:
            rank = row.xpath('./th')[0].text_content()
            td_list = row.xpath('./td')
            table.append([rank] + [t.text_content() for t in td_list if len(t.text_content())>0])

        file_exists = os.path.exists(csv_name)
        mode = 'a' if file_exists else 'w'
        d = datetime.datetime.now()
        if len(args) > 1:
            d = d - datetime.timedelta(hours=8)
        date, current_time = str(d).split(' ')

        with open(csv_name, mode) as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(schema)
            for row in table:
                print([date]+row)
                writer.writerow([date]+row)

        delay = SLEEP_TIME + (random.random() * SLEEP_TIME_BUFFER)
        print('Sleeping for {}'.format(str(datetime.timedelta(seconds=delay))))
        time.sleep(delay)

if __name__ == '__main__':
    main(*sys.argv)
