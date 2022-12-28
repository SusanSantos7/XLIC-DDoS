<h1 align="center">Introduction</h1>

This [DDoS attack](https://en.wikipedia.org/wiki/Denial-of-service_attack) python script is an experimental tool meant to be used for educational and research purposes only. It is not intended to be used to launch attacks against any systems or networks. Please use this script responsibly, making sure to have the proper permissions and authorization before running any code. This script is provided “as is” and the author makes no warranties or guarantees as to its accuracy or safety. Use at your own risk.

This script is a Distributed Denial of Service (DDoS) attack script. It uses a large number of malicious requests to overwhelm a server, making it unable to handle legitimate requests. It starts by sending a large number of requests to the specified URL with random headers. It then checks the response of the server and adjusts the attack parameters accordingly, increasing or decreasing the number of threads and packets sent. It also reads a malicious file and sends the malicious requests to the server. Finally, it starts the attack with the specified number of threads.

This Python script is a serious the one which, if discovered or used without authorization, could land you in jail. It serves only educational purposes.

**Requirements:** requests,
threading,
random,
datetime,
contextlib,
werkzeug,
suppress

**Installation:**
```
git clone https://github.com/SusanSantos7/XLIC-DDoS.git | cd XLIC-DDoS
```
