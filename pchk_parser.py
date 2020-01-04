'''This is only prototype version of my program where i created a sketch of my 
   future program where i will check prices of AMAZON.COM '''
from flask import Flask,Response,request
from fbchat import *  
from fbchat.models import *
import time as t
import requests as rq
from bs4 import BeautifulSoup
from multiprocessing import Process, Value

url = 'http://warmman.pythonanywhere.com/market/item/grich_cht/'
client = Client('vova.manukyan.05@mail.ru','hellomyfriend27890')


#----------Flask app---------
app = Flask(__name__)
status = '111'
runing_code = ''

@app.route('/get_url')
def get_url():
    url = request.data
    return Response('200')

@app.route('/start_parsing/',methods=['POST'])
def start_parsing():
    if status == '111':
        print('Status 111')
        
        runing_code = request.data
        main()
        return Response('Response')
    else:
        return Response('403')

#---------Parsing Part of programm-----------
def get_html(url):
    '''Get page html code'''
    r = rq.get(url)
    return r.text

def get_price(html):
    '''gets price of item'''
    soup = BeautifulSoup(html,'lxml')
    c = soup.find('div',class_='jumbotron').find('h3').text
    return c[0:len(c)-1]

def checker_loop(loop_on):
    url = 'http://warmman.pythonanywhere.com/market/item/grich_cht/'
    html = get_html(url)
    start_price = get_price(html)
    print(start_price + '-Start price')
    while True:
        if loop_on.value == True:
            if runing_code == '112':
                print('---------')
                t.sleep(20)
                loop_price = get_price(get_html(url))
                print(loop_price + '-Loop price')
                #-----Checking price--------
                if start_price != loop_price:
                    delta_price = int(loop_price) - int(start_price) #price changing delta
                    percent_delta = abs((float(delta_price) / float(start_price))*100) #price changing in percents
                    #---------------Sending messages-----------------
                    client.send(Message(text='--------------------------------------'), thread_id = client.uid,thread_type=ThreadType.USER)
                    client.send(Message(text='Change of price!!!!!!'), thread_id = client.uid,thread_type=ThreadType.USER)
                    client.send(Message(text=f'Price change amount:  {delta_price}'), thread_id = client.uid,thread_type=ThreadType.USER)
                    client.send(Message(text=f'Change in percents:  {percent_delta}%'), thread_id = client.uid,thread_type=ThreadType.USER)
                    print('Sent')
                    start_price = loop_price  
            else:
                print('Waiting for command')
        t.sleep(20)

if __name__ == '__main__':
    recording_on = Value('b', True)
    p = Process(target=checker_loop, args=(recording_on,))
    p.start()  
    app.run(debug=True, use_reloader=False)
    p.join()

    
    
