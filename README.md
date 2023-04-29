# Lecture assignment "Cloud Computing" Bigdata Course - [API](http://bigdata.centralindia.cloudapp.azure.com/)
This is a dummy API hosted on Azure Virtual machines on a `Standard_D2s_v3` instance. It sympolize an API that radars can consume by sending cars plates images and the return would be plate numbers.


## Examples:

<div class="center">

Image | Return Value
:--:|:--:
![image-one](https://user-images.githubusercontent.com/64917739/235271735-803be379-22d4-409b-b158-743d13976f25.jpg) | KL 55R 2473
![image-two](https://user-images.githubusercontent.com/64917739/235271835-0b2d25e1-a38b-4212-ba63-277adcb028e1.jpg) | HR.26 BR.9044
![image-three](https://user-images.githubusercontent.com/64917739/235271906-0fe812be-4664-45cf-8a18-29f075f23ed8.jpg) | H982 FKL
![image-four](https://user-images.githubusercontent.com/64917739/235272070-c405cbfe-9e24-44df-97fe-5cd39f821070.jpg) | HR 26 DA 2330

</div>

```console
(venv) ziadh@Ziads-MacBook-Air assignment % curl -X POST -H "Content-Type: multipart/form-data" -F "file=@/Users/ziadh/Desktop/college/spring-2023/big-data/assignment/assets/license-plates/image1.jpg" http://bigdata.centralindia.cloudapp.azure.com/predict
{"plate_number":"HR.26 BR.9044"}
```

<img width="1440" alt="Screenshot 2023-04-29 at 3 13 52 AM" src="https://user-images.githubusercontent.com/64917739/235272295-be80f107-b601-4ca7-81e1-3bf30fe621d6.png">


```console
ziadh@bigdata-computervision:~/plate-numbers$ sudo nohup uvicorn main:app --host 0.0.0.0 --port 80 > /dev/null 2>&1 &
[1] 22245
```


```config
Host bigdata-hw
  HostName bigdata.centralindia.cloudapp.azure.com
  User ziadh
  IdentityFile ~/.ssh/bigdata-computervision_key.pem
```

```console
ziadh@Ziads-MacBook-Air assignment % ssh bigdata-hw
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.15.0-1036-azure x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sat Apr 29 00:18:54 UTC 2023

  System load:  0.0                Processes:             127
  Usage of /:   57.5% of 28.89GB   Users logged in:       0
  Memory usage: 11%                IPv4 address for eth0: 10.0.0.4
  Swap usage:   0%


 * Introducing Expanded Security Maintenance for Applications.
   Receive updates to over 25,000 software packages with your
   Ubuntu Pro subscription. Free for personal use.

     https://ubuntu.com/azure/pro

Expanded Security Maintenance for Applications is not enabled.

26 updates can be applied immediately.
24 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status

New release '22.04.2 LTS' available.
Run 'do-release-upgrade' to upgrade to it.


Last login: Fri Apr 28 23:42:58 2023 from XXX.XXX.XXX.XXX
ziadh@bigdata-computervision:~$ 
```
