# MySql
###### MySql(Mariadb) 설치, 환경설정 및 기본적인 사용법 설명
</br></br>


## MySql 설치
</br>

### OS update
<pre>$ sudo apt-get update
$ sudo apt-get upgrade</pre>
> 일반적으로 우분투에서 패키지 설치 전/후에 시스템 업데이트 할 것을 기본적으로 권장함.
</br>

### MySql 설치
<pre>$ sudo apt-get install mysql-server</pre>
</br></br></br>


## MySql 기본 설정
</br>

### 외부 시스템에서 접속하기 위해 방화벽에 3306 포트 열기
<pre>$ sudo ufw allow mysql
$ sudo ufw reload</pre>
> 방화벽 규칙(ufw)을 설정하지 않은 경우에는 실행할 필요 없음.
</br>

### OS 실행 시 자동으로 MySql이 시작되도록 시스템에 등록
<pre>$ sudo systemctl enable mysql</pre>
</br></br></br>


## MySql 관련 OS 명령
</br>

### MySql 시작
<pre>$ sudo service mysql start</pre>
or
<pre>$ sudo systemctl start mysql</pre>
#### 재시작
<pre>$ sudo service mysql restart</pre>
</br>

### MySql 종료
<pre>$ sudo service mysql stop</pre>
or
<pre>$ sudo mysqladmin -uroot -p shutdown</pre>
</br>

### MySql 접속
<pre>$ mysql -u MYSQL-ID -p</pre>
