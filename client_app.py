import requests as rq

token = b'00125'
start = b'112'


#token_sending = rq.post('http://127.0.0.1:5000/check_token',data=token)
start_command = rq.post('http://127.0.0.1:5000/start_parsing/',data=start)
