#Timer
import time


#time 1970-01-01 00:00:00 기준으로 초 단위로
print(time.time())


print(time.gmtime())

# 한국에서 실행한다면 GMT+9가 출력
print(time.localtime())


tm = time.localtime()
str_tm = time.strftime("%Y-%m-%d %I:%M:%S %p", tm)
print(str_tm)


# 시간 줄어들기

in_sec = input("시간을 입력하세요.(초):")
sec = int(in_sec)
print(sec)

#while은 반복문으로 sec가 0이 되면 반복을 멈춰라
while (sec != 0 ):
    sec = sec-1
    time.sleep(1)
    print(sec , "초")



#타이머 시작점
start = input("Enter를 누르면 타이머를 시작합니다.")
begin = time.time()

#타이머 종료점
stop = input("Enter를 누르면 측정을 종료합니다.")
end = time.time()

#시간차
result = end - begin

#여기서 round는 파이썬에서 소수점 자리수 조절에 활용됩니다.
result = round(result,3)
print("시작 후", result, "초의 시간이 흘렀습니다.")