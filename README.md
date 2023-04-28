```console
(venv) ziadh@Ziads-MacBook-Air assignment % curl -X POST -H "Content-Type: multipart/form-data" -F "file=@/Users/ziadh/Desktop/college/spring-2023/big-data/assignment/assets/1.png" http://localhost:5002/recognize_plate
{"plate_number":"ABC123"}

uvicorn main:app --host 0.0.0.0 --port 8000
```

ziadh

```console
ssh -i ~/.ssh/bigdata-computervision_key.pem ziadh@20.219.159.85

ziadh@bigdata-computervision:~$ ls
ziadh@bigdata-computervision:~$ pwd
/home/ziadh
ziadh@bigdata-computervision:~$ 

ziadh@bigdata-computervision:~$ git clone https://github.com/ZiadMansourM/plate-numbers.git
Cloning into 'plate-numbers'...
remote: Enumerating objects: 41, done.
remote: Counting objects: 100% (41/41), done.
remote: Compressing objects: 100% (35/35), done.
remote: Total 41 (delta 3), reused 41 (delta 3), pack-reused 0
Unpacking objects: 100% (41/41), 22.12 MiB | 15.16 MiB/s, done.
ziadh@bigdata-computervision:~$ ls
plate-numbers


```