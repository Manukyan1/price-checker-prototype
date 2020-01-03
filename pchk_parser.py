'''This is only prototype version of my program where i created a sketch of my 
   future program where i will check prices of AMAZON.COM '''













from fbchat import *  
from fbchat.models import *
import time as t
import requests as rq
from bs4 import BeautifulSoup


url = 'http://warmman.pythonanywhere.com/market/item/grich_cht/'

client = Client('vova.manukyan.05@mail.ru','hellomyfriend27890')


def get_html(url):
    r = rq.get(url)
    return r.text
def get_price(html):
    soup = BeautifulSoup(html,'lxml')
    c = soup.find('div',class_='jumbotron').find('h3').text
    return c[0:len(c)-1]



def main():
    html = get_html(url)
    start_price = get_price(html)
    print(start_price + '-Start price')
    while True:
        print('---------')
        t.sleep(20)
        print('60 secs completed')
        print('------------------')
        loop_price = get_price(get_html(url))
        print(loop_price + '-Loop price')
        if start_price != loop_price:
            print('IN if statement')
            delta_price = int(loop_price) - int(start_price)

            percent_delta = abs((float(delta_price) / float(start_price))*100)
            print('Sending messages')
            client.send(Message(text='--------------------------------------'), thread_id = client.uid,thread_type=ThreadType.USER)
            client.send(Message(text='Change of price!!!!!!'), thread_id = client.uid,thread_type=ThreadType.USER)
            client.send(Message(text=f'Price change amount:  {delta_price}'), thread_id = client.uid,thread_type=ThreadType.USER)
            client.send(Message(text=f'Change in percents:  {percent_delta}%'), thread_id = client.uid,thread_type=ThreadType.USER)
            print('Sent')
            start_price = loop_price            


if __name__ == '__main__':
    main()
