'''
적성일자 : 25-04-26
작성자 : 장준영
목적 : 파이썬 기초 실습
'''
# print("Hello World!")#출력해주는 함수
# 한거번에 주석처리하는 방법
# 원한는 부분을 드래그해서 컨트롤 누르고 / 누른다
# 주석을 해제할 대도 독같이 컨트롤 누르고 / 누른다
# 저장하는 방법
# 파일 --> 저장(ctrl + s)
# <변수 만들기>
# 변수이름 = 값
# 가독성! --> 알아보기 쉬어야 함함
# 예약어(키워드)
# -->특별한 의미기 부여된 단어
# -->파이썬이 미리 특징 의미로 사용하기로 약속해놓은 것
# -->대소문자 구분
# ex) 예약어를 확인하는 방법
# import keyword
# print(keyword.kwlist)
# 띄어쓰기는 '_'를 사용
# 변수 만들기
# number = 4 number 
# print(number)
# 개인정보 출력하기
# name = 'Junyoung'
# age = 12
# address = '''대구 용산서로 21
# 미진태왕아파트 102동 1303호'''
# girlfriend = None 없다 의미
# height = 153.2 실수(mistake 아님) 임
#print(name)
# print(age)
# print(address)
# print(girlfriend)
# print(height)
# 여러개의 변수
# a, b, c = 1, 2, 3, 짝에 맞춰 대입입
# print(a)
# print(b)
# print(c)
# a, b, c = 4, 4, 4
# =
# a, b, c = 4
# print = 표준 출력 함수(화면에 보여줌)
# print('Hello') 문자열을 출력하려면 앞뒤로 작은따움표 또는 큰따움표를 붙인다
# print(1)
# print(2)
# print(3)
# print() 빈줄(다른언어는 \n 도 됨)
# 출력해 보면 저절로 enter가 되어있음
# print(1, 2, 3) 구분자는 실행 시 space로 표현
# print(4, 'hello', 's', 'name') 여러 종류도 가능
# print('     ', 'space') 공백도 글자임
# print(1, 2, 3, sep =',') sep를 이용해 쉼표를 표시할수 있음
# print(4, 5, 6, sep ='') #붙어나옴
# sep는 print만 가능
# print(1, 2, end ='') 엔터 기능을 없에는 것
# 이스케이프 문자
# --> 출력물을 보기 좋게 보는 용도로 사용
# --> 대표적인 것 \n(enter)
# print('hello \'world\'') /'를 이용해 hello 'world' 가 가능
# print("hello 'world'") 파이썬 만 가능(63줄 이랑 같은 거임)
# 자료형
# --> 프로그래밍 할 대 쓰이는 숫자, 문자열 들 자료형태로 사용하는 모든 것
# --> 다른 언어의 경우 변수 설정시 애초에 자료형(타입)을 설정해야 하는 경우가 많다
# --> 파이썬의 경우는 값을 대입(활당)하면 그 대 자료형(타입)이 결정되기 때문에 초보자가 배우기 쉽다.(우리가 자료형 생각 안해도 된다!) 때문에 초보자가 배우기 쉽다.
# --> type() 함수로 자료형을 알아볼 수 있다.
# --> 기본 자료형 : 정수(int), 실수(float), 문자열(str), 불(bool)
# --> 컬렉션 자료형 : 리스트(list), 튜플(tuple), 딕서니리(dict), 세트(set)
# num1 = 100
# num2 = 300
# print(num1 + num2) 산술 계산 가능
# print(type(num1)) print 에 type를 너으면 어느거인지 알수 있음
# PY 2회차
'''
작성일자 : 25-04-27
작성자 : 장준영
목적 : 자료형
'''
# 실수형
# width = 30.5 #실수형태
# height = 25.3
# print(width)
# print(height)
# print(type(width))
# print(type(height))
# print(width + height)
# print(width - height) #오차가 나옴
# print(width * height)
# print(width / height)
# 정수와 실수 계산
# x = 7.0
# y = 3
# print(x + y) #두개중애 하나라도 실수이면, 결과도 실수
# print(x - y)
# print(x * y)
# print(x / y)
# bool 자료형
# x = 100
# y =99
# result = x > y
# print(result)
# print(type(result))
# 잘료형의 형 변환
# bool() : 불 자료형으로 변환
# print(bool(0)) #0은 거짓을 의미함
# print(bool(1)) #1은 진실을 의미함
# print(bool(3)) #0빼고 모든수는 진실을 의미함
# print(bool('')) #비어있는 것도 거짓으로 의미함
# print(bool([])) #기호도 거짓으로 의미함
# float() : 실수형으로 형 변환
# print(float(True))
# print(float(False))
# print(float(100))
# print(float('abc')) #문자열은 실수로 바꿀수없음
# int() : 정수형으로 형 변환
# print(int(True))
# print(int(False))
# print(int(3.14)) #뒤에 소수점이 날아간다다
# str() : 문자열 형태로 형 변환
# a = '100'
# print(type(a))
# b = 100
# print(type(b))
# c =str(b) #문자열 형태로 형변환해서 C변수에 담았다
# print(c)
# print(type(c))
# d = int(a) #정수 형태로 형 변환해서 d변수에 담았다
# print(d)
# print(type(d))
# 퀴즈 정답
# a = 'Jang_jun_young'
# print(a)
# 문장열 연산
# first_name = 'Fu'
# last_name = 'bao'
# full_name = first_name + last_name
# print(full_name)
# 문자열 반복하기
# full_name5 = full_name * 5
# print(full_name5,)
# -, /는 없다
# 문자열 연사은 +, * 만 가능하다
# 문자열 index
#  -->문자열을 담은 변수명[index 번호]
#  --> [0] : 문자열 처음
#  --> [-1] : 문자열의 마지막(끝글자)
# index로 추출하기
# s = 'hello'
# print(s)
# print(s[0])
# print(s[5]) #애러
# first_char = s[0] #새로운 변수에 indexing 결과를 저장장
# print(first_char)
# last_char = s[-1] #맨 끝 글자
# print(last_char)
# 문자열 slicing
#  -->문자열의 구간을 표시(어디서부터 어디까지)
#  -->예를 들어 a라는 변수가 있다면
#  --> a[시작 index번호 : 끝 index번호+1 : 증감값]
# 증감값은 1씩 증가인 경우 생략한다
# --> [:] : 처음부터 끝까지. 모두를 의미
# text = 'i love Python'
# print(text)
# substring1 = text[2:6] #2번 index부터 6번앞까지
# print(substring1) #2~5번 글자 추출
# substring3 = text[7:13:2] #2씩 증가
# print(substring3) #7, 9, 11번 글자 추출
# print(text[:]) #모두 다 전체가 출력됨
# substring4 = text[:5] #처음부터~5앞까지
# print(substring4) #시작번호 생략
# substring5 = text[7:] #7번부터 끝까지
# print(substring5) #끝번호를 생략
# indexing / slicing 은 원본에 영향을 주지 않는다!
# 문자열 관련 함수들
# text = 'Python'
# text_length = len(text) #글자 수(길이)
# print(text_length)
# upper_text = text.upper() #대문자로 변환
# print(upper_text)
# lower_text = text.lower() #소문자로 변환환
# print(lower_text)
# text2 = '   i love Python   '
# pure_text2 = text2.strip() #양쪽 공백을 지워준다
# print(text2)
# print(pure_text2)
# text3 = '***i love Python***'
# pure_text3 = text3.strip('*') #양쪽의 '*'를 지워준다
# left_text3 = text3.lstrip('*') #왼쪽의 '*'를 지워준다
# right_text3 = text3.rstrip('*') #오른쪽의 '*'를 지워준다
# print(pure_text3)
# print(left_text3)
# print(right_text3)
# split_text3 = text3.split() #공백을 기준으로 분리리
# print(split_text3)
# phone = '010-6628-1957'
# split_phone = phone.split('-') #'-'을 기준으로 분리
# print(split_phone)
# re_phone = phone.replace('-', '') #'-'을 없앴다. 글자를 바꾸어준다
# print(re_phone)
# re2_phone = phone.replace('-', ',')
# print(re2_phone)
# re3_phone = phone.replace('6628', '0000')
# print(re3_phone)
# 문자열 formatting
# -->문자열 표현을 편리하게 해준다
# -->1.% 연산자 formatting(기본 formatting)
#    2. format()
#    <형식>
#    '문자열 {}'.format(변수 명)
#    3. f-strings (f 문자열 포매팅) --> Python 3.6 이후
#    <형식>
#    f'문자열 {변수명}'
# name = 'Poubao'
# age = 4
# print("My name is {}, My age is {}".format(name, age))
# print("Next year is {}".format(age + 1))
# year, mont, day = 2020, 7, 20
# print("My 생년월일은 {} years {} monts {} days" .format(year, mont, day))
# print()
# f-strings
# print(f"My name is {name}, My age is {age}")
# print(f"Next year is {age + 1}")
# print(f"My 생년월일은 {year} year {mont} mont {day} day")
# intput() : 표준 입력 함수
# name = input('input the name : ')
# age = input('input a age : ')
# print(f"input a name is {name}")
# print(f"input a age is {age}")
'''
작성일자 : 25-05-03
작성자 : 장준영
목적 : 연산자, 제어문(조건문, 반복문)
'''
# input 함수의 자료형
# number = input("첫번째 숫자 입력 : ") #문자형형
# number2 = input("두번재 숫자를 입력 : ")
# print(f"number + number2 = {number + number2}")
# print(f"더하기 한 것의 자료형 = {type(number + number2)}")
# input 함수로 입력받은 값은 무조건 str(문자열)
# 정수로 형 변환
# number = int(input("첫번째 숫자 입력 : ")) #정수형형
# number2 = int(input("두번재 숫자를 입력 : "))
# print(f"number + number2 = {number + number2}")
# print(f"더하기 한 것의 자료형 = {type(number + number2)}")
# 실수로 형 변환
# number = float(input("첫번째 숫자 입력 : ")) #실수형
# number2 = float(input("두번재 숫자를 입력 : "))
# print(f"number + number2 = {number + number2}")
# print(f"더하기 한 것의 자료형 = {type(number + number2)}")
# 연산자
# 산술연산자
# num = 100
# num2 = 3
# print(num + num2)
# print(num - num2)
# print(num / num2) #나누기 연산자는 무조건 실수형
# print(num // num2) #몫
# print(num % num2) #나머지
# print(num ** num2) #거듭제곱
# 복합대입연산자
# num = 77
# num2 = 23
# num3 = num + num2
# print(f"num : {num}, num2 : {num2}, num3 : {num3}")
# num += num2
# print(f"num : {num}, num2 : {num2}, num3 : {num3}")
# 비교연산자
# a = 70
# b = 60
# a_is_bigger = a > b
# a_is_smaller = a < b
# is_equal = a == b
# is_not_equal = a != b
# print(a_is_bigger)
# print(a_is_smaller)
# print(is_equal)
# print(is_not_equal)
# 논리연산자
# is_snowing = True
# is_cold = True
# is_winter = is_snowing and is_cold
# print(is_winter)
# is_snowing = False
# is_spring = is_snowing or is_cold
# print(is_spring)
# is_false = False
# print(not is_false)
# is_True = True
# print(not is_True)
# 조건연산자
# x = 21
# y = 20
# x가 y보다 크다면 max, x값을 할당(대입, 담는다)하고.
# 그렇지 않으면 max변수에 y값을 할당.
# 결과를 담을 변수 = 참일 경우 if 조건식 else 거짓일 경우
# max = x if x > y else y
# print(max)
# membership 연산자(in 연산자)
# in : 포함되어 있니?
# print("안녕"in"안녕하세요") #포함되어있음
# print("메롱"in"안녕하세요") #포함되어있지 않음
# # not in : 포함되어 있지 않니?
# print("안녕"not in"안녕하세요") #포함되어있지 않음
# print("메롱"not in"안녕하세요") #포함되어있음
# 조건문
# age = 20
# if age >= 20:
#     print("20 이상입니다.")
# fruit = '딸기'
# if fruit == '바나나':
#     print("i like banana.")
# else 사용하기
# fruit = '망고'
# if fruit == '바나나':
#     print("i like banana")
# else:
#     print("i dont like banana")
# age = 14
# if age >= 20:
#     print("im more than 20 years old")
# else:
#     print("im less than 20 years old")
# 실습 문제 #correct
# age = int(input("input ages : "))
# if age >= 20:
#     print("youre more than 20 years old")
# else:
#     print("youre are less than 20 years old")
# 짝수/홀수
# num = int(input("input numbers : "))
# if num % 2 == 0: #2로 나눈 나머지와 같다면...
#     print("짝수 임")
# else:
#     print("홀수 임")
# elif 사용
# num  = int(input("input numbers : "))
# if num > 0:
#     print("양수 임")
# elif num == 0:
#     print("0임")
# else:
#     print("음수 임")
# score = int(input("input scores : "))
# if score >= 90:
#     print('A')
# elif score >= 80:
#     print('B')
# elif score >= 70:
#     print('C')
# elif score >= 60:
#     print('D')
# elif score < 100:
#     print("ERROR")
# else:
#     print('F')
# month = int(input("input months : "))
# if 3 <= month <= 5: #3, 4, 5
#     print("봄")
# elif 6 <= month <= 8: #6, 7, 8
#     print("여름")
# elif 9 <= month <= 11: #9, 10, 11
#     print("가을")
# else: #12, 1, 2
#     print("겨울")
# age = int(input("input ages : "))
# if age <= 7:
#     print("no school")
# elif age <= 13:
#     print("초등")
# elif age <= 16:
#     print("중등")
# elif age <= 19:
#     print("고등")
# elif age <= 99:
#     print("성인")
# else:
#     print("DEAD")
# login 프로그램
# id = 'korea'
# password = 1234
# if id == 'korea' and password == 1234:
#     print("succeed")
# elif id == 'korea' and password != 1234:
#     print("no succeed")
# elif id != 'korea' and password == 1234:
#     print("no succeed")
# else:
#     print("first, join")
# 반복 문
# while
# -- >조건식이 참일 경우 계속 반복
# --> while 조건식:
#    참일 경우 계속 실행
# --> 반복 횟수가 정해진 경우(변수 - 카운팅 이용)
# --> 시작값을 담을 변수
# --> while 조건식:
#     참일 경우 실행
#     변수에 증감값
# while 반복 횟수가 정해진 경우
# count = 0
# while count < 3: #참일 동안 반복
#     print(count)
#     count += 1 #count = count + 1 --> count를 1씩 증가
# 1씩 감소하기
# count = 10
# while count > 5:
#     count -= 1 #count = count - 1 --> 1씩 감소
#     print(count)
# 실습 문제 #실패
# name = input("input a name : ")
# 국어 = int(input("input scores : "))
# 수학 = int(input("input scores : "))
# 영어 = int(input("input scores : "))
# print(f"{name}님의 성적은...")
# print(f"성적 합계 = {국어 + 수학 + 영어}") #틀림
# total = 국어 + 수학 + 영어
# average = total / 3
# print(f"{total}, 평균은 {average:.lf}")
'''
작성일자 : 25-05-11
작성자 : 장준영
목적 : 사용자 정의 함수(def)
'''
# number = int(input("값을 입력하세요 : "))
# total = 0 # 합계를 저장할 변수
# for i in range(1, number + 1,):
#     total += i
# print(f"1 ~ {number} 합 : {total}")
# number1 = int(input("시작값 입력 : "))
# number2 = int(input("끝값 입력 : "))
# number3 = int(input("증감값 입력 : "))
# total = 0
# for i in range(number1, number2 + 1, number3):
#     total += i
# print(f"{number1} ~ {number2} {number3}씩 증가시킨 값의 합계 : {total}")
# ----------------------------------------------------------------------------
# 함수
# 함수 용어 정리
# --> 입력 관련 : 인수, 인자, 매개변수, 파라미터
# --> 출력 관련 : 반환값, 결과값, return 값
# 입력(매개변수), 출력(반환값)이 없는 가장 간단한 함수 --> 장난꾸러기 자판기
# <형식>
# def 함수이름(): # 함수 정의의
#   수행할 코드
# 함수이름() # 함수 호출
# def coffee():
#     print("커피가 나왔을 까요?")
#     print("응 아니야ㅋ XD")
# coffee() # 함수 호출
# -----------------------------
# 입력(매개변수)만 있는 함수 --> 날강도 자판기
# <형식>
# def 함수이름(매개변수1, 매개변수2): #함수 정의
#   수행할 코드(함수 몸통)
# 함수이름(인수1, 인수2) # 함수 호출
# def add(num1, num2): # 함수 정의의
#     print(num1 + num2) # num1의 값과 num2의 값을 더한 것을 화면에 보여준다
# add(1, 2) #함수 호출
# print("XD")
# add(10, 20) # 함수 호출
# x = 6
# y = 3
# add(x, y) # 함수 호출
# n1 = int(input("첫번째 정수 입력 : "))
# n2 = int(input("두번째 정수 입력 : "))
# add(n1, n2)
# add("대한", "민국")
# -----------------------------------------
# 반환값(출력)만 있는 함수
# <형식>
# def 함수이름(): # 함수 정의
#   수행할 코드(함수 몸통 - 있어도 되고, 없어도 되고 만드는 사람 마음)
#   return 반환값(출력값/결과값)
# 결과변수 = 함수이름() # 함수 호출
# def coffee(): # 함수 정의
#     result = 'delicious coffee👍'
#     return result
# x = coffee() # 함수 호출
# print(x) # 결과변수에 담을 내용을 print함수로 확인한다
# print(coffee()) # 한번만 호출해서 print함수로 바로 결과를 볼 수도 있다
# -------------------------------------------------------------------
# 입력(매개변수), 출력(변환값)이 1개인 함수 --> 일반자판기
# <형식>
# def 함수이름(매개변수1, 매개변수2): #함수 정의
#   수행할 코드(함수 몸통)
#   return 변환값(결과값)
# 결과변수 = 함수이름(인수1, 인수2) # 함수 호출
# def add(number1, number2):
#     print("지금부터 더하기를 합니다")
#     return number1 + number2
# result1 = add(1, 2) # 함수 호출 후 반환값을 result에 딤았다
# print(result1) # 실재로 잘 담겼는지 결과를 print함수에서 확인
# result2 = add(30, 40) # 함수 호출
# print(result2)
# print(add(50, 60)) # 함수 호출한 결과를 결과변수에 담지않고 print함수로 바로 본다
# ------------------------------------------------------------------------------
# 입력(매개변수), 출력(변환값)이 2개 이상인 함수
# <형식>
# def 함수이름(매개변수1, 매개변수2): #함수 정의
#   수행할 코드(함수 몸통)
#   return 반환값1, 반환값2
# 결과변수1, 결과변수2 = 함수이름(인수1, 인수2) # 함수 호출
# def add_sub(number1, number2):
#     return number1 + number2, number1 - number2
# x, y = add_sub(1, 2) # 함수호출
# print(x)
# print(y)
# print(add_sub(200, 100))  # 함수 호출, print함수로 바로 결과만 확인
# (300, 100) --> 결과는 튜플 1개 -> 튜플 언패킹 -> 각각의 변수에 따로 담기 가능
# ----------------------------------------------------------------------------
# def add_sub(number1, number2):
#     print("앞부분은 더하기한 결과입니다")
#     print("뒷부분은 빼기한 결과입니다")
#     return number1 + number2, number1 - number2
# x, y = add_sub(55, 33) # 함수 호출
# print(f"두 숫자를 더하기 한 결과 : {x}, 두 숫자를 빼기 한 결과 : {y}")
# ------------------------------------------------------------------------
# 조건문을 활용한 함수
# def check_divide_seven(num): #함수 정의
#     if num % 7 == 0: # 7의 배수라면
#         return True
#     else:
#         return False
# # 함수 호출
# print(check_divide_seven(3))
# print(check_divide_seven(14))
# print(check_divide_seven(7.1))
# --------------------------------
# 리스트로 평균 반환하기
# 매개변수 성적(리스트) -> 합계 -> 평균 -> 평균 반환
# def calculate_average(scores): #함수 정의
#     sum = 0 #합계 변수 초기화
#     for score in scores:
#         sum += score # sum = sum + score
#     average = sum / len(scores) # 평균 = 합계 / scores의 개수
#     return average # 평균을 반환(리틴)
# 함수 호출
# average1 = calculate_average([55, 70, 100])
# print(f"average1 : {average1}")
# average2 = calculate_average([100, 99, 88, 77])
# print(f"average2 : {average2}")
# --------------------------------------------------
# def info(name, age, address): #함수 정의
#     print(f"name : {name}")
#     print(f"age : {age}")
#     print(f"address : {address}")
# # 함수 호출
# info("장준영", 12, "대구 달서구 용산서로 21 미진태왕 아파트")
# ---------------------------------------------------------
# 키워드 변수
# def info(name, age, address): #함수 정의
#     print(f"name : {name}")
#     print(f"age : {age}")
#     print(f"address : {address}")
# 함수 호출
# info('장준영', 12, "대구 달서구 용산서로 21 미진태왕 아파트") # 일반적인 함수 호출
# info(name = '장준영', age =  12, address = "대구 달서구 용산서로 21 미진태왕 아파트") # 키워드 인수
# info(age = 12, address = "대구 달서구 용산서로 21 미진태왕 아파트", name = '장준영') # 순서를 다르게 해도 됨
# -----------------------------------------------------------------------------------------------------------
# 디폴트 매개변수(기본 매개변수) --> 매개변수에 초깃값을 미리 설정
# def info(name, age, address = '비공개'): #함수 정의
#     print(f"name : {name}")
#     print(f"age : {age}")
#     print(f"address : {address}")
# # 함수 호출
# info('장준영', 12)
# info('장준영', 12, "대구 달서구 용산서로 21 미진태왕 아파트")
# ----------------------------------------------------------
# 가변 매개변수 --> 매개변수의 개수를 정확하게 모를 때 사용
# <형식>
# def 함수이름(*args): # 함수정의
#   수행할 코드(함수 몸통)
# 함수이름(필요한 인수만큼 입력) # 함수 호출
# def adder(*args): # 함수정의
#     print(f"{args}의 합은 {sum(args)}입니다")
# 함수호출
# adder(1, 2)
# adder(3, 5, 7)
# adder(1.5, 2, 3, 4)
# ----------------------
'''
작성일자 : 25-05-17
작성자 : 장준영
목적 : 험수 고급(콜백 함수, 람다함수), 파일입출력
'''
# 일반 매개변수와 가변매개변수를 함께 사용하기
# --> 가변 매개변수를 맨 뒤로 위치시킨다
# def add_mul(name, choice, *args):
#     print("더하기, 곱하기만 가능")
#     print(f"나의 이름은 {name} 이다, 지금 부터 개산 시작")
#     if choice == 'add': #더하기기
#         answer = 0 # 합계를 담을 변수 초기값을 0으로 한다
#         for i in args:
#             answer += i #ansewr = answer + i
#     elif choice == 'mul': #곱하기
#         answer = 1 # 초기값을 1로 한다(0을 곱하면 0이 되서)
#         for i in args:
#             answer *= i # answer = answer * i
#     return answer # 최종 answer에 담긴 값을 변환한다
# result = add_mul('Chill_Guy', 'add', 1, 2, 3) # 함수호출
# print(f"최종값 : {result}")
# ---------------------------------------------------------
# 콜백 함수
# def caluculator(x, y, operation): # 매개변수 --> x(정수), y(정수), operation(함수)
#     return operation(x, y) # 함수명(x, y) --> 함수호출
# def plus(x, y): # 더하기
#     return x + y
# def minus(x, y): # 빼기
#     return x - y
# def multiple(x, y): # 곱하기
#     return x * y
# def divide(x, y): # 나누기
#     return x / y
# 함수 호출
# plus_result = caluculator(2, 3, plus)
# print(plus_result)
# minus_result = caluculator(2, 3, minus)
# print(minus_result)
# multi_result = caluculator(2, 3, multiple)
# print(multi_result)
# divide_result = caluculator(2, 3, divide)
# print(divide_result)
# --------------------------------------------
# 람다 함수
# 필터 함수를 활용한 람다 함수
# 0 ~ 19 리스트 생성 --> range() 함수
# numbers = list(range(20))
# print(numbers)
# filter() --> 특정 조건에 맞는 값만 추출(필터, 걸러낸다)
# <형식>
# filter(특징 조건, 시퀀스 자료형)
# 람다함수를 사용하려면 --> filter(람다 함수, 시퀀스 자료형)
# 시퀀스 자료형 --> 문자열, 리스트, 튜플
# 0 ~ 19 짝수만 걸러내기(람다함수, 필터사용)
# even_numbers = filter(lambda x: x % 2 == 0, numbers)
# even_numbers = list(even_numbers) # 리스트로 형 변환해서 다시 저장
# print(even_numbers)
# sorted() 함수에서 람다 함수를 이용한 정렬
# tuple_num = [(1, 10), (4, 20), (99, 6), (8, 12), (-3, 20)]
# sorted_tuple = sorted(tuple_num) # 오름차순 정렬
# print(sorted_tuple)
# sorted_tuple2 = sorted(tuple_num, reverse = True) # 내림차순 정렬
# print(sorted_tuple2)
# 튜플 인댁스번호 1번의 값을 기준으로 오름차순 정렬, ex -> (1, 10)
# sorted_tuple3 = sorted(tuple_num, key = lambda x: x[1])
# print(sorted_tuple3)
# ---------------------------------------------------------------------
# 커피 자판기
# 커피 종루 3가지 --> 아매리카노(1000원), 카페라떼(1500원), 카푸치노(2000원)
# 고객이 자판기에 입려해야 하는 것 --> 돈, 선택할 메뉴 --> 매개변수
# 자판기에서 나오는 것 --> 주문한 커피, 잔돈 --> 반환값(return)
# 1. 생각해야 하는 상황 : 1. 없는 메뉴를 주문했을 경우
#                        2. 구매 금액이 부족한 경우
#                        3. 정상 경우 -> 거스름돈 O, 거스름돈 X
# 실행할 때 돈과 메뉴를 입력한다 --> input() 사용할거다
# money = int(input("얼마를 입력할거야? : ")) # 돈
# pick = input("커피 선택 : [아매리카노, 카페라때, 카푸치노] : ") # 선택할 메뉴
# 매개변수 money, pick은 coffee_vedingmachine함수 안에 속해 있는 변수 --> 지역변수(함수가 실행이 끝이 나면 지역변수도 사라짐)
# def coffee_vedingmachine(money, pick): # 함수 정의
#     """커피자판기 함수 구현"""
#     print(f"{money}원에 {pick}을 선택하셨습니다")
#     menu = {
#         '아메리카노' : 1000, #메뉴이름:메뉴가격
#         '카페라때' : 1500,
#         '카푸치노' : 2000
# } # 자판기 메뉴판 정의
# 1. 없는 메뉴를 주문했을 경우
# if pick not in menu:
#     print(f"{pick}은/는 판매하지 않습니다")
#     return money, 'NOT IN MENU'
# 2. 구매 금액이 부족했을 경우
# elif money < menu[pick]:
#     print(f"{pick}은/는 {menu[pick]}원 입니다")
#     return money, '금액 부족'
# 3. 정상인 경우 -> 거스름돈이 있을 경우
# else:
#     return money - menu[pick], pick
# 함수 호출 : 반환값이 2개이므로, 결과변수도 2개(돈, 메뉴이름)
# change, coffee = coffee_vedingmachine(money, pick)
# print(f"거스름돈 : {change}원, 커피 : {coffee}")
# ------------------------------------------------------
# 파일 입출력
# 파일 쓰기 -> hello.txt 라는 파일을 생성해서 'hello, world!' 넣을 거임
# file = open('test.txt', 'w') # 파일 열기(쓰기 모드)
# file.write("fuck") # 문자열 쓴다
# file.close() # 파일 닫기
# for를 이용해서 파일에 문자열 쓰기
# file = open('hello.txt', 'w', encoding = 'utf-8') # 파일 열기(쓰기 모드)
# for i in range(1, 11):
#     data = f"{i}번째 줄임\n"
#     file.write(data)
# file.close() # 파일 닫기
# ----------------------------------------
# 파일 경로
# 상대 경로 : 현재 풀더 기준으로 그 안에 있는가?
# ./ --> 현재 풀더
# ../ --> 상위 풀더(부모 풀더)
# ./test/hello.text --> 현자 풀더 안에 hello.txt
# 절대 경로 : 주소 전체
# C:\python_weekends
# -------------------------------------------------
# 기존 파일에 새로운 내용을 추가하기 -> 추가모드(a)
# 글자 깨졌을 때 --> encoding = 'utf-8'
# file = open('hello.txt', 'a', encoding = 'utf-8') # 파일 열기(추가 모드)
# file.write('--------------------------\n')
# for i in range(11, 21):
#     data = f"{i}번째 줄임\n"
#     file.write(data)
# file.close() #파일 닫기
# class 만들기
# class noob:
#     def introduce(self):
#         print("hi")
# vip = noob()
# vip.introduce()
'''
작성일자 : 25-05-24
작성자 : 장준영
목표 : 클래스-생성자, 클래스변수, 상속, 예외처리(가능하면)
'''
# 클래스 : Book --> 이름 : title(인스턴스 변수), 저자 : author(인스턴스변수)
# 인스턴스 매서드 --> set_info --> title, author 에 값을 담는다
# 인스턴스 매서드 --> print_info --> title, author 화면에 보여주는 역할
# class Book: # 클래스 정의
#     def set_info(self, author, title):
#         '''책 이름과 저자를 저장하는 역할을 하는 함수'''
#         self.title = title # 책 이름 저장
#         self.author = author # 저자 저장
#     def print_info(self):
#         '''책 이름과 저자를 화면에 보여주는 함수'''
#         print(f"책 제목 : {self.title}")
#         print(f"책 저자 : {self.author}")
# Book_nob = Book() # 객체(인스턴스)생성
# Book_nob.set_info('it세계의 괴물들', '아무순수') # 인스턴스 매서드 호출
# Book_nob.print_info() # 인스턴스 매서드 호출
# Book_vip = Book() # 객체(인스턴스)생성
# Book_vip.set_info('개발자 기술 면접 노트', '이남화')
# Book_개발자 = Book() # 객체(인스턴스)생성
# Book_개발자.set_info('혼자 공부하는 얄팍한 코딩지식', '고현민') # 객체(인스턴스)생성
# Book_개발자.print_info() # 객체(인스턴스)생성
# --------------------------------------------------------------------------------------
# 생성자
# --> 객체(인스턴스)가 생성될 대 자동으로 호출(실행) 되는 메서드(함수)
# --> __int__(self)
#   스폐셜 메서드(매직 메서드) --> 파이썬이 목적에 따라 자동으로 호출해주는 메서드 앞뒤로 __가 붙은 메서드
# -----------------------------------------------------------------------------------------------------
# 생성자2
# class animal: # 클래스 생성 정의
#     def __init__(self, sound): # 생성자 정의
#         '''인스턴스(객체) 변수 self.sound에 값(sound)을 지정하는 역할'''
#         self.sound = sound # 인스턴스 변수에 값 저장
#     def cry(self): # 일반적인 인스턴스 메서드(함수)
#         '''인스턴스 변수(self.sound)에 저장된 값을 두 번 출력'''
#         print(self.sound * 2) # 맴매 * 2 --> 맴맴맴맴
# cat = animal('야옹') # 객체(인스턴스) 생성과 동시에 생성자(__init__) 로출(실행)
# # cat.sound = '야옹'
# cat.cry() # 인스턴스 메서드(함수) 호출(실행)
# dog = animal('멍멍') # 객체(인스턴스) 생성과 동시에 생성자(__init__) 로출(실행)
# # dog.sound = '멍멍'
# dog.cry() # 인스턴스 메서드(함수) 호출(실행)
# chiken_jokie = animal('꼬기오') # 객체(인스턴스) 생성과 동시에 생성자(__init__) 로출(실행)
# # chiken_jokie.sound = '꼬끼오'
# chiken_jokie.cry() # 인스턴스 메서드(함수) 호출(실행)
# ------------------------------------------------------------------------------------------
# 생성자와 소멸자
# class cup: # 클래스 정의
#     def __init__(self, color, brand):
#         '''인스턴스 변수에 컵의 색깔(color)과 컵의 브랜드(brand)를 저장'''
#         self.color = color
#         self.brand = brand
#     def print_info(self):
#         '''인스턴스 변수에 담긴 값을 화면에 보여주는 함수'''
#         print(f"컵의 색상은 {self.color} 색 입니다")
#         print(f"컵의 브랜드는 {self.brand} 입니다")
#     def __del__(self): # 소멸자
#         print(f"{self.brand} 컵 객체가 소멸되었습니다 :)")
# vip_cafe_cup = cup('black', 'vip_cafe') # 객체(인스턴스) 생성과 동시에 생성자(__init__) 로출(실행)
# vip_cafe_cup.print_info() # 인스턴스 메서드(함수) 호출(실행)
# del vip_cafe_cup # vip_cafe_cup 객체(인스턴스) 삭제 --> 소멸자 실행 :)
# noob_cafe_cup = cup('yellow', 'noob_cafe') # 객체(인스턴스) 생성과 동시에 생성자(__init__) 로출(실행)
# noob_cafe_cup.print_info() # 인스턴스 메서드(함수) 호출(실행)
# del noob_cafe_cup # noob_cafe_cup 객체(인스턴스) 삭제 --> 소멸자 실행 :)
# ---------------------------------------------------------------------------------------------------
# 상속
# class parent: # 부모(슈퍼) 클래스
#     def hello(self): # 인스턴스 메서드
#         print("ㅎ2")
# class child(parent): # 자식(서브) 클래스 --> 상속받은 클래스
#     def bye(self): # 자식의 인스턴스 메서드
#         print("ㅃ2")
# ㅅㅂ = parent() # 부모 클래스를 이용한 인스턴스(객체) 생성
# ㅅㅂ.hello() # 인스턴스 메서드 호출
# ㅂㅅ = child() # 자식 클래스를 이용한 인스턴스(객체) 생성
# ㅂㅅ.hello() # 부모 클래스의 인스턴스 메서드 호출(상속받아서 가능)
# ㅂㅅ.bye()  # 인스턴스 메서드 호출
# ----------------------------------------------------------------------------
# 생성자 추가
# class parent: # 부모(슈퍼) 클래스
#     def __init__(self, name): # 생성자
#         self.name = name # 인스턴스변수 self.name에 값name을 넣었다
#     def hello(self): # 인스턴스 메서드
#         print(f"ㅎ2 나는 {self.name} 입니다")
# class child(parent): # 자식(서브) 클래스
#     def bye(self):
#         print("ㅃ2")
# chill_gay = parent('칠 게이') # 부모 클래스를 통한 인스턴스(객체) 생성 -> 생성자
# chill_gay.hello()
# chill_guy = child('칠 가이')
# chill_guy.hello()
# chill_guy.bye()
# --------------------------------------------------------------------------------------------
# 자식의 생성자, super()
# class parent: # 부모(슈퍼) 클래스
#     def __init__(self, name):
#         self.name = name
#     def hello(self):
#         print(f"ㅎ2 저는 {self.name} 입니다")
# class child(parent): # 상속
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age # 나이 넣는다
#     def bye(self):
#         print(f"{self.name} 은/는 {self.age}살 입니다, 안녕히 계세요")
# person1 = parent('짱구')
# person1.hello()
# person2 = child('훈이', 7)
# person2.hello()
# person2.bye()
# -------------------------------------------------------------------------
# try ~ except
# try: # 예외가 발생할 수 있는 코드 영역역
#     num1 = int(input("첫 번재 정수를 입력하세요 : "))
#     num2 = int(input("두 번째 정수를 입력하세요: "))
#     print(f"num1 나누기 num2의 결과는 {num1/num2} 입니다")
# except:
#     print("예외가 발생했습니다")
# -----------------------------------------------------------------
# 발생 예외(상황에 따른 예외 처리)
# try:
#     num1 = int(input("첫 번째 정수를 입력 : "))
#     num2 = int(input("두 번째 정수 입력 : "))
#     print(f"num1 나누기 num2의 결과는 {num1/num2} 입니다")
# except ZeroDivisionError: # 0으로 나누기 했을대 생기는 예외클래스
#     print("0으로 나눌 수 없습니다")
# except ArithmeticError:
#     print("산술 연산 예외가 발생했습니다")
# except ValueError:
#     print("입력값 예외가 발생했습니다")
# ------------------------------------------------------------
# try:
#     li = [1, 2, 3, 4]
#     index = int(input("인덱스 번호를 입력하세요(0 ~ 3) : "))
#     print(li[index]) # li리스트의 해당 인덱스번호의 값을 출력
# except IndexError:
#     print("인덱스 범위를 벗어났습니다")
'''
작성일자 : 25-05-31
작성자 : 장준영
목표 : 모듈, 표준 라이브러리, 외부 라이브러리
'''
# 패키지 안에 있는 모듈 사용하기,
#   애스터리스크(*) 사용해서 모든 함수 호출
# from converter.length_converter import *
# kilometer = int(input("kilometer 입력 : "))
# meter = int(input("meter 입력 : "))
# miles_from_kilometer = kilometer_to_miles(kilometer) # 함수 호출
# print(f"{kilometer}km miles로 환산 : {miles_from_kilometer}mile")
# kilometer_from_meter = meter_to_killometer(meter) # 함수 호출
# print(f"{meter}미터를 kilometer로 환산 : {kilometer_from_meter}km")
# -----------------------------------------------------------------------
# 패키지 -> import만
# import converter.length_converter
# kilometer = int(input("kilometer 입력 : "))
# meter = int(input("meter 입력 : "))
# restlt1 = converter.length_converter.kilometer_to_miles(kilometer)
# print(f"{kilometer}km를 miles로 환산 :  {restlt1}mile입니다")
# restlt2 = converter.length_converter.meter_to_killometer(meter)
# print(f"{meter}미터를 kilometer로 환산 : {restlt2}km입니다")
# -------------------------------------------------------------------------
# 별명 붙이기
# import converter.length_converter as con
# kilometer = int(input("kilometer 입력 : "))
# meter = int(input("meter 입력 : "))
# restlt1 = con.kilometer_to_miles(kilometer)
# print(f"{kilometer}km를 miles로 환산 :  {restlt1}mile입니다")
# restlt2 = con.meter_to_killometer(meter)
# print(f"{meter}미터를 kilometer로 환산 : {restlt2}km입니다")
# -----------------------------------------------------------------------
# 표준 모듈 - 원주율(파이)을 이용하여 원의 둘레 구하기
# import math
# def calculate_circumference(radius):
#     '''반지름을 입력받아 원의 둘래를 구하는 함수'''
#     # 원의 둘래 공식 : 반지름 * 2 * 원주율(파이)
#     circumference = radius * 2 * math.pi
#     return circumference
# # 반지름을 입력받기
# r = float(input("원의 반지름을 입력하세요 : "))
# result = calculate_circumference(r) # 함수 호출 -> 원의 둘레 구한다
# print(f"입력하신 원의 둘레 : {result:.2f}입니다")
# -------------------------------------------------------------------------
# math 관련 함수들
# import math
# print(f"1.2를 올림 처리 : {math.ceil(1.2)}")
# print(f"-1.2올림 처리 : {math.ceil(-3.5)}")
# print()
# print(f"1.7을 내림 처리 : {math.floor(1.7)}")
# print(f"-1.7을 내림 처리 : {math.floor(-1.7)}")
# print(f"1.3을 소수점 이하 버림처리 : {math.trunc(1.3)}")
# print(f"-1.3을 소수점 이하 버림처리 : {math.trunc(-1.3)}")
# print()
# result_sqrt = math.sqrt(49)
# print(f"sqrt() 제곱근을 구하는 함수 : {result_sqrt}")
# result_pow = math.pow(2, 10) # **연산자와 같다
# print(f"pow() 거듭제곱을 구하는 함수 : {result_pow}")
# print(f"round() 내장함수 -> 반올림 : {round(1.7)}") # 일의자리까지 반올림림
# print(f"round() 내장함수 -> 반올림 : {round(1.756, 2)}") # 소수둘째자리까지 반올림
# --------------------------------------------------------------------------------------
# random 모듈
# import random
# print(f"1 ~ 45 random 정수 : {random.randint(1, 45)}") # 1 ~ 45 정수하나
# print(f"0 ~ 10(9) 정수 : {random.randrange(10)}")
# print(f"1 ~ 20(19) 홀수 정수 : {random.randrange(1, 20, 2)}")
# def generate_lotto():
#     '''로또 번호 구하는 함수 : 1 ~ 45사이의 임의의 숫자 6개를 선택'''
#     lotto = random.sample(range(1, 46, 6)) # sample(범위, 숫자) : 중복없이 숫자만큼 개수를 뽑는다, 리스트로 변환
#     return lotto
# lotto_numbers = generate_lotto()
# print(f"로또 번호 : {lotto_numbers}")
# -----------------------------------------------------------------------------------
# 랜덤으로 뽑기(임이의 값을 선택)
# import random
# def generate_win(pandas):
#     '''랜덤으로 당첨판다 뽑기 --> choice() : 임이의 값을 선택'''
#     winner = random.choice(pandas)
#     return winner
# # 5마리의 판다를 입력받아서 리스트에 추가
# list_pandas = [] # 빈 리스트
# for p in range(5):
#     panda = input("참여할 판다이름을 입력 : ")
#     list_pandas.append(panda) # 입력한 panda값을 list_pandas에 추가
# print(f"아이스크림 내기에 참여할 판다들은{list_pandas}입니다")
# # 당첨판다 및 출력
# result = generate_win(list_pandas)
# print(f"내기에 걸린 판다는 {result}입니다🤣")
# -----------------------------------------------------------------
# 무작위 실수 추출 & list형 정수 썪기
# import random
# random_float1 = random.random() # 0 ~ 1 사이의 무작위 실수 추출
# print(random_float1)
# list_num = [10, 20, 30, 40, 50]
# random.shuffle(list_num) # list_num 원본을 섞는다
# print(list_num)
# -------------------------------------------------------------------------------
# datetime
# import datetime
# 현자 날씨와 시간 반환
# present = datetime.datetime.now()
# print(present)
# print(f"오늘 날짜는 {present.date()}입니다")
# print(f"올해는 {present.year}년입니다")
# print(f"이번달은 {present.month}월입니다")
# print(f"이번달은 {present.day}일입니다")
# print(f"현재 시간은 {present.time()}입니다")
# print(f"현재 시간은 {present.hour}시입니다")
# print(f"현재 분은 {present.minute}분입니다")
# print(f"현재 초는 {present.second}초입니다")
# --------------------------------------------------
# timedelta() 함수
# import datetime
# password = input("설정할 비번 입력 : ")
# print("비밀번호 설정이 완료되었습니다")
# today = datetime.datetime.now()
# # 365일이 지나면 비번 완료 --> 예상
# day365 = today + datetime.timedelta(days = 365) # 90이 지난 날짜 저장
# print(f"비번은 365일 후 {day365.date()}에 만료됩니다")
# -----------------------------------------------------------------------------
# time 모듈
# import time
# print(time.time())
# time.sleep(3) # 잠시 쉰다(3초 쉰다)
# print("이 문장은 3초 후에 나옵니다")
# ---------------------------------------
# 터틀 그래픽스 모듈로 그림그리기
# 원 그리기
# import turtle as t # turtle 라이브러리의 별명을 t로 설정
# t.shape('turtle') # 마우스포인터 모양이 거북이 모양
# t.color('red') # 선 색깔을 빨강으로 설정
# t.circle(100.0) # 반지름이 200인 원을 그린다
# t.mainloop() # 창이 계속 열려있는 상태, # 쓰거나 말거나
# -------------------------------------------------------------
# 사각형 그리기
# import turtle as t # turtle 라이브러리의 별명을 t로 설정
# t.shape('turtle') # 마우스포인터 모양이 거북이 모양
# t.color('blue') # 선 색깔을 파랑으로 설정
# t.speed(2)
# for i in range(4):
#     t.forward(150) # 앞으로 150
#     t.right(90) # 오른쪽으로 90도 회전
# t.mainloop() # 창이 계속 열려있는 상태, # 쓰거나 말거나
# ---------------------------------------------------------------
# 별 그리기
# import turtle as t # turtle 라이브러리의 별명을 t로 설정
# t.shape('turtle') # 마우스포인터 모양이 거북이 모양
# t.color('blue') # 선 색깔을 파랑으로 설정
# t.speed(2)
# for i in range(5):
#     t.forward(200)
#     t.right(144) # 오른쪽으로 144(72도 * 2)도 회전
#     t.forward(200)
#     t.left(72) # 왼쪽으로 72도(360 / 5)회전
# t.mainloop() # 창이 계속 열려있는 상태, # 쓰거나 말거나
# ------------------------------------------------------------------
# 사용자가 입력한 도형 그리기(vs code recoder! : long code)
# import turtle as t # turtle 라이브러리의 별명을 t로 설정
# t.shape('turtle') # 마우스포인터 모양이 거북이 모양
# t.color('blue') # 선 색깔을 파랑으로 설정
# t.speed(2)
# t.shapesize(3, 5) # 거북이 3배 확대
# shapes = t.textinput('창제목', '도형을 입력하세요(원, 사각형, 별)')
# if shapes == '원':
#     radius = int(t.textinput('원', '반지름 : ')) # 반지름을 입력받는다
#     t.circle(radius)
# elif shapes == '사각형':
#     width = int(t.textinput('사각형', '가로 : ')) # 가로길이 입력받는다
#     height =  int(t.textinput('사각형', '세로 : ')) # 세로길이를 입력받는다
#     for i in range(2):
#         t.forward(width) # 가로변
#         t.left(90)
#         t.forward(height) # 세로변
#         t.left(90)
# elif shapes == '별':
#     size = int(t.textinput('별', ' 크기 : ')) # 크기를 입력받는다
#     for i in range(5):
#         t.forward(size)
#         t.right(144)
#         t.forward(size)
#         t.left(72)
# else:
#     print("잘못입력 했어🤣")
# t.mainloop() # 창이 계속 열려있는 상태, # 쓰거나 말거나
'''
작성일자 : 25-06-07
작성자 : 석득화
목표 : 크롬 개발자, cgv영화제목 추출, 네이버it/과학 뉴스제목 추출
    파이썬 GUI 윈도우 프로그래밍(PyQt6)
'''
# vs code 외부라이브러리 설치
# 1. 테미널 켠다
# 2. pip(3) install requests
# 3. pip(3) install bs4
# CGV 영화 무비차트 -> 영화 제목 추출하기
# ------------------------------------------
# import requests
# from bs4 import BeautifulSoup
# url = 'http://www.cgv.co.kr/movies/'
# respones = requests.get(url)
# html = respones.text
# soup = BeautifulSoup(html, 'html.parser')
# ex) <srtong class = "title">드래곤 길들이기</strong>
# movies = soup.find_all('strong', {'class' : 'title'}) # 영화 제목
# print(movies[0].text) # 결과 : 드래곤 길들이기
# print('-' * 30)
# for movie_name in movies:
#     print(movie_name.text) # 영화 제목 하나하나
# print('-' * 30)
# 순위 : 영화제목 --> 1위 : 드래곤 길들이기
# for i, movie_name in enumerate(movies, start = 1):
#     print(f"{i}위 : {movie_name.text}")
# 결과
# 1위 : 드래곤 길들이기
# 2위 : 하이파이브
# 3위 : 미션 임파서블: 파이널 레코닝
# 4위 : 브링 허 백
# 5위 : 신명
# 6위 : (Live) 메이플스토리 2025 ASSEMBLE SHOWCASE
# 7위 : 소주전쟁
# 8위 : 릴로 & 스티치
# 9위 : (SX Live) 메이플스토리 2025 ASSEMBLE SHOWCASE
# 10위 : 미치광이 피에로
# 11위 : 신성한 나무의 씨앗
# 12위 : 페니키안 스킴
# 13위 : 미야자키 하야오: 자연의 영혼
# 14위 : 씨너스: 죄인들
# 15위 : 극장판 짱구는 못말려-격돌! 낙서왕국과 얼추 네 명의 용사들
# 16위 : 파과
# 17위 : 말없는 소녀
# 18위 : 기타맨
# 19위 : 브레이킹 아이스
# -------------------------------------------------------------------------------
# 네이버 IT/과학 뉴스 제목 추출하기
# import requests
# from bs4 import BeautifulSoup
# url = 'https://news.naver.com/section/105'
# response = requests.get(url)
# html = response.text
# soup = BeautifulSoup(html, 'html.parser')
# news = soup.find_all('strong', {'class' : 'sa_text_strong'})
# print(news)
# for nes_title in news:
#     print(nes_title.text) # 뉴스 제목
# print('-' * 30)
# press = soup.find_all('div', {'class' : 'sa_text_strong'}) # 신문사
# print(press)
# 뉴스 제목 <- 신문사 이름
# news2 = soup.find_all('div', {'class' : 'sa_text'}) # 뉴스 제목과 신문사
# # print(news2)
# for n in news2:
#     print(n.find('strong', {'class' : 'sa_text_strong'}).text) # 뉴스 제목
#     print(n.find('div', {'class' : 'sa_text_press'}).text) # 신문사
#     print('-' * 30)
# 결과
# 넥슨, PvPvE 신작 게임 '아크 레이더스' 10월 30일 출시
# 지디넷코리아
# ------------------------------
# 머리카락 굵기 100만분의 1 ‘양자거리’… 韓 연구진이 처음 측정했다
# 조선일보
# ------------------------------
#  “매출 왜 올랐지?” 질문 하나면 충분…AI 에이전트 체험해보니[스노우플레이크 서밋]
# 디지털데일리
# ------------------------------
# 네오위즈 'P의거짓: 서곡', 깜짝 출시...스팀 톱 셀러 진입
# 지디넷코리아
# ------------------------------
# 차기 iOS26, 주목 받지 못했던 신기능은 ‘이것’
# 지디넷코리아
# ------------------------------
# "국민과 '진짜 의료개혁' 추진…공론화위, 지속가능 로드맵 만든다"
# 뉴스1
# ------------------------------
# "넷플·디즈니 등 OTT 계정 정보 700만건 유출⋯한국도 피해 포함"
# 아이뉴스24
# ------------------------------
# 국내 게임·출판업계, 앱마켓 수수료 30% 뜯어가는 구글·애플에 소송 제기
# 조선일보
# ------------------------------
# "9시부터 줄섰어요"…美서 난리났다는데 한국도 '오픈런' 행렬
# 한국경제
# ------------------------------
# 넥슨 '메이플스토리', 여름 쇼케이스서 신규 직업 '렌' 공개
# 데일리안
# ------------------------------
# 넥슨 ‘메이플스토리’, 신규 직업 ‘렌’ 등장…여름 쇼케이스 ‘어셈블’ 개최
# 매일경제
# ------------------------------
# T1 ‘Ofel’ 강준호, FSL 결승 진출…"페이커처럼 우승하고파”
# 지디넷코리아
# ------------------------------
# 애플 앱스토어 개발자, 작년 1770조 벌었다...한국은?
# 지디넷코리아
# ------------------------------
# “보고도 눈을 의심”…삼성폰 전쟁 속 목숨까지 구했다, ‘대박’
# 헤럴드경제
# ------------------------------
# 과제 산적한 애플…WWDC, 주가 반등 촉매제될까
# 블로터
# ------------------------------
# 퀄컴, 2년 뒤 애플과 완전 결별 낙관적..."AI반도체 새 기회"
# 지디넷코리아
# ------------------------------
# 식을 줄 모르는 '셰프' 열풍…가전업계도 주목
# 지디넷코리아
# ------------------------------
# 아마존, 사람 대신 로봇이 택배 배달 한다
# 지디넷코리아
# ------------------------------
# 한 번 검사로 여러 암 포착…`다중 암 조기진단` 게인체인저 된다
# 디지털타임스
# ------------------------------
# 주인 못찾은 '위니아', 18일 상장폐지 수순
# 지디넷코리아
# ------------------------------
# 숏폼 키우고 뉴스 큐레이션…AI시대, 포털 다음 부활할까
# 디지털타임스
# ------------------------------
# 인간 보면서 더 강해진다...로보티즈, '세미 휴머노이드' 공개
# 지디넷코리아
# ------------------------------
# 막 올린 서머 게임 페스트… 한국산 게임 총출동
# 국민일보
# ------------------------------
# 2+3의 정답을 맞힌 동물 지능의 비밀 [AI오답노트]
# 아시아경제
# ------------------------------
# “계정이 갑자기 사라졌다”…인스타그램 무차별 정지에 전 세계 이용자 ‘분통’
# 서울경제
# ------------------------------
# K게임 전시관, 천안 K컬처 박람회서 문전성시
# 국민일보
# ------------------------------
# "일본서 실컷 먹고 '꽁돈' 벌었네"…행운 터진 사연[잇:써봐]
# 이데일리
# ------------------------------
# 넷플릭스 CEO 만난 네이버 최수연…'네넷' 성과 확인
# 비즈워치
# ------------------------------
# “친하게 지내자”…혹등고래, 인간 앞에서 ‘거품 고리’ 만드는 이유 [핵잼 사이언스]
# 서울신문
# ------------------------------
# [클라우드, 경계를 넘다]② MSP, 운영 대행자에서 AI 조력자로
# 디지털데일리
# ------------------------------
# [클라우드, 경계를 넘다]① CSP, 인프라 공급자에서 AI 지배자로
# 디지털데일리
# ------------------------------
# SKT 유심 교체 700만명 육박… 잔여 예약자 299만명
# 머니S
# ------------------------------
# [취재수첩] 디지털주권과 통상압박 사이, 한국의 선택은
# 디지털데일리
# ------------------------------
# 엔씨소프트 2026년 매출 2조원 달성 조건 '아이온2·타깃 마케팅'
# 블로터
# ------------------------------
# 李대통령, G7정상회의 참석...국제 외교 데뷔
# 지디넷코리아
# ------------------------------
# 바이오솔루션 "카티로이드 국내 임상 신청 반려, 호주 임상 추진"
# 이데일리
# ------------------------------
# 차기 iOS26, 주목 받지 못했던 신기능은 ‘이것’
# 지디넷코리아
# ------------------------------
# 네오위즈, ‘P의 거짓: 서곡’ 깜짝 출시…본편 ‘스팀’ 한국 판매 순위 1위
# 매일경제
# ------------------------------
# 넥슨, PvPvE 신작 게임 '아크 레이더스' 10월 30일 출시
# 지디넷코리아
# ------------------------------
# [게임위드인] '스팀'으로 몰려가는 K게임…밸브 한국 진출도 성사될까
# 연합뉴스
# ------------------------------
# 카카오게임즈, '크로노 오디세이' CBT 6월 20일부터 시작
# 뉴스1
# ------------------------------
# 넥슨, 신작 ‘아크 레이더스’ 오는 10월30일 출시
# 세계일보
# ------------------------------
# 네오위즈 'P의거짓: 서곡', 깜짝 출시...스팀 톱 셀러 진입
# 지디넷코리아
# ------------------------------
# "북한서 대규모 인터넷 접속장애...내부적 문제 가능성"
# 지디넷코리아
# ------------------------------
# PyQt6
# 첫번째 PyQt6 윈도우 만들기 - QWidget 사용
# from PyQt6.QtWidgets import QApplication, QWidget
# app = QApplication([]) # 앱 객체 생성
# window = QWidget() # 창 생성
# window.setWindowTitle('My title') # 제목
# window.show() # 창 보여주기
# app.exec() # 루프 시작(창이 계속 더있다, 우리가 종료해야 종료됨)
# ---------------------------------------------------------------
# 버튼이 있는 창 만들기 - QPushButton
# from PyQt6.QtWidgets import QApplication, QPushButton
# app = QApplication([])
# window = QPushButton('Press me 😊')
# window.setWindowTitle('There are My button and title')
# window.show()
# app.exec()
# --------------------------------------------------------------------------------
# 메인 윈도우 - QMainWindow
# from PyQt6.QtWidgets import QApplication, QMainWindow
# app = QApplication([])
# window = QMainWindow() # 매인 윈도우 창
# window.setWindowTitle("My main title")
# window.show()
# app.exec()
# --------------------------------------------------------------
# QMainWindow 를 상속해서 내 창 만들기
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__() # 부모 클래스의 생성자를 호출
#         # 창 제목
#         self.setWindowTitle('My app')
#         # 버튼 생성
#         button = QPushButton('Press me 😊')
#         self.setCentralWidget(button) # 버튼 중앙에 배치
# app = QApplication([])
# window = MainWindow() # 우리가 만든 클래스가지고 윈도우 객체 생성
# window.show()
# app.exec()
# -------------------------------------------------------------------
# 창 크기 / 버튼 크기 / 아이콘 설정
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
# from PyQt6.QtGui import QIcon
# import os
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         # 창 제목 설정
#         self.setWindowTitle('My app')
#         # 창 위치, 크기 설정
#         self.setGeometry(300, 300, 300, 200) # (x, y, w, h)
#         # 버튼 생성
#         button = QPushButton('You should click 😈', self)
#         # 버튼 위치, 크기 지정
#         button.setGeometry(80, 50, 150, 80) # (x, y, w, h)
#         # 아이콘
#         icon_path = r'cute_python_snake.ico'
#         if os.path.exists(icon_path):
#             icon = QIcon(icon_path) # 아이콘 파일 로드(불러온다)
#             self.setWindowIcon(icon) # 윈도우 타이틀 아이콘 변경
#         button.setCheckable(True) # 버튼이 눌러졌다
#         # 메서드 호출
#         self.button_click(True)
#         self.button_click(False)
#     def button_click(self, checked): # checked -> 클릭햇나? 안했나?
#         print('클릭되었다', checked)
# app = QApplication([])
# window = MainWindow()
# window.show()
# app.exec()
'''
작성일자 : 25-06-08
작성자 : 장준영
목표 : PyQt6의 여러 예제들, 위젯들
'''
# 시그널 & 슬롯(버튼 클릭 이밴트 처리)
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
# from PyQt6.QtGui import QIcon
# import os
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('My app')
#         self.setGeometry(300, 300, 300, 200)
#         button = QPushButton('You must click', self)
#         button.setGeometry(80, 50, 150, 80)
#         button.setCheckable(True)
#         # 버튼을 클릭하면(시그널) button_click함수(슬롯)실행
#         button.clicked.connect(self.button_click)
#         icon_path = 'cute_python_snake.ico'
#         if os.path.exists(icon_path):
#             icon = QIcon(icon_path) # 아이콘 로드
#             self.setWindowIcon(icon) # 윈도우 타이틀 아이콘 변경
#         else:
#             print(f"경고 : 아이콘 파일을 찾을 수 없습니다.({icon_path})")
    # 슬롯(메서드, 함수)
#     def button_click(self, checked):
#         print('clicked', checked)
# app = QApplication([])
# window = MainWindow()
# window.show()
# app.exec()
# -------------------------------------------------------------------------------------
# PyQt6의 여러 위젯
# 여러 위젯, 이벤트
# from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
# from PyQt6.QtGui import QIcon
# import os
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         # [창 제목 설정]
#         self.setWindowTitle('욕 입력ㅋㅋㅋ')
#         # [창 위치 및 크기]
#         self.setGeometry(300, 300, 300, 200)
#         # [아이콘 파일이 있으면 아이콘으로 사용]
#         icon_path = 'cute_python_snake.ico'
#         if os.path.exists(icon_path):
#             icon = QIcon(icon_path)
#             self.setWindowIcon(icon)
#         else: # 아이콘이 없을 대 경고 메세지 출력
#             print(f"경고 : 아이콘 파일을 찾을 수 없습니다. ({icon_path})")
#         ----------------------------------------------------------------------
#         위젯 : 레이블(라벨)
#         self.lable = QLabel('여기에 텍스트가 출력됩니다', self)
#         self.lable.move(20, 20) # 레이블 위치
#         self.lable.resize(250, 30) # 레이블 크기 (widget, height)
#         ---------------------------------------------------------------
#         위젯 : 입력상자(박스)
#         self.input = QLineEdit(self)
#         self.input.move(20, 60)
#         self.input.resize(200, 30)
#         self.input.textChanged.connect(self.lable.setText)
#         --------------------------------------------------------------------------
#         위젯 : 버튼 -> 종료
#         btn = QPushButton('종료', self)
#         btn.move(20, 100)
#         btn.resize(80, 40)
#         btn.clicked.connect(QApplication.instance().quit)
# --------------------------------------------------------------------------
# 메인 코드
# app = QApplication([])
# window = MainWindow()
# window.show()
# app.exec()
# ----------------------------------
# 다양한 여러 위젯
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, \
#                             QCheckBox, QRadioButton, QComboBox, QDateTimeEdit, \
#                             QFontComboBox, QVBoxLayout, QWidget, QLabel, QLineEdit
# from PyQt6.QtGui import QIcon
# import os
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#        [창 제목 설정]
#        self.setWindowTitle('[Unknow]')
#        [창 위치 및 크기]
#        self.setGeometry(300, 300, 300, 200)
#        [아이콘 파일이 있으면 아이콘으로 사용]
#        icon_path = 'cute_python_snake.ico'
#        if os.path.exists(icon_path):
#             icon = QIcon(icon_path)
#             self.setWindowIcon(icon)
#        else: # 아이콘이 없을 대 경고 메세지 출력
#           print(f"경고 : 아이콘 파일을 찾을 수 없습니다. ({icon_path})")
#        layout  = QVBoxLayout()
# 사용할 위젯 클래스들
# widgets = [
#     QCheckBox, # 체크박스
#     QRadioButton, # 라디오버튼 (여러개 중에 하나만 선택)
#     QComboBox, # 콤보박스 (드롭다운 메뉴)
#     QDateTimeEdit, # 날짜 / 시간 입력 위젯
#     QFontComboBox, # 폰트(글자) 선택 콤보박스
#     QLabel, # 텍스트 레이블(출력용)
#     QLineEdit, # 한 줄짜리 텍스트 입력박스
#     QPushButton # 일반 버튼
# ]
# 위젯을 하나씩 꺼내어 레이아웃에 추가
# for w in widgets:
#     layout.addWidget(w())
#     # Qwidget(빈 컨테이너 위젯)
#     widget = QWidget() # 빈 컨테이너 생성
#     widget.setLayout(layout) # 위에서 만든 레이아웃 붙인다
#     # 이 위젯을 QMainWindow 중앙에 배치(화면에 다 채움)
#     self.setCentralWidget(widget)
# ------------------------------------------------------------------
# QVBoxLayout --> 세로(Vertical) 방향으로 위젯들을 차곡차곡 쌓는 레이아웃
# --------------------------------------------------------------------------
# 메인 코드
# app = QApplication([])
# window = MainWindow()
# window.show()
# app.exec()
# ---------------------------------------------------------------
# 텍스트가 화면에 나온다 -> 버튼을 클릭 -> 이미지가 보여진다
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
# from PyQt6.QtGui import QIcon, QFont, QPixmap
# import os
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#       [창 제목 설정]
        # self.setWindowTitle('[Unknow]')
        # [창 위치 및 크기]
        # self.setGeometry(300, 300, 400, 400)
        # [아이콘 파일이 있으면 아이콘으로 사용]
        # icon_path = 'cute_python_snake.ico'
        # if os.path.exists(icon_path):
        #    icon = QIcon(icon_path)
        #    self.setWindowIcon(icon)
        # else: # 아이콘이 없을 대 경고 메세지 출력
        #     print(f"경고 : 아이콘 파일을 찾을 수 없습니다. ({icon_path})")
        # --------------------------------------------------------------------
        # 텍스트 / 아미지 레이블
        # self.lable = QLabel('토끼가 곧나와', self)
        # font = QFont()
        # font.setPointSize(25) # 글자 크기를 25pt로 크게
        # self.lable.setFont(font) # 폰트 크기 적용
        # setGeomeatry() --> 레이블 위치와 크기를 직접 지정
        # self.lable.setGeometry(50, 20, 300, 330)
        # button = QPushButton('클릭하셈', self)
        # button.setGeometry(50, 360, 300, 50)
        # button.clicked.connect(self.button_click) # 클릭 시 함수(슬롯) 연결
#   버튼 클릭 시 실행 되는 함수 -------------------------------------------------
#     def button_click(self):
#         # QPixmap --> 이미지 파일을 불러와서 레이블에 보여준다
#         pixamp = QPixmap('rabbit.png')
#         self.lable.setPixmap(pixamp)
#         self.lable.setPixmap(pixamp) # 레이블에 이미지를 적용
# ------------------------------------------------------------------
# QVBoxLayout --> 세로(Vertical) 방향으로 위젯들을 차곡차곡 쌓는 레이아웃
# --------------------------------------------------------------------------
# 메인 코드
# app = QApplication([])
# window = MainWindow()
# window.show()
# app.exec()
# ------------------------------
# 레이아웃 관리
# QVBoxLayot --> 세로 정렬 -> 위 -> 아래 쪽
# QHBoxLayot --> 가로 정렬 -> 왼쪽 -> 오른쪽 쭉
# QGirdLayout --> 엑셀처럼 격자로 배치, (행, 열)좌표 -> 가로, 세로
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, \
#                             QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
# from PyQt6.QtGui import QIcon
# import os
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#        # [창 제목 설정]
#         self.setWindowTitle('[Unknow]')
#        # [창 위치 및 크기]
#         self.setGeometry(300, 300, 400, 400)
#        # [아이콘 파일이 있으면 아이콘으로 사용]
#         icon_path = 'cute_python_snake.ico'
#         if os.path.exists(icon_path):
#            icon = QIcon(icon_path)
#            self.setWindowIcon(icon)
#         else: # 아이콘이 없을 대 경고 메세지 출력
#             print(f"경고 : 아이콘 파일을 찾을 수 없습니다. ({icon_path})")
#         # ----------------------------------------------------------------------
#         # 1. QVBoxLayout (세로로 쌓기)
#         vbox_layout = QVBoxLayout()
#         vbox_layout.addWidget(QLabel('세로로 쌓기 예제'))
#         vbox_layout.addWidget(QPushButton('버튼 1'))
#         vbox_layout.addWidget(QPushButton('버튼 2'))
#         vbox_layout.addWidget(QPushButton('버튼 3'))
#         # 2. QHBoxLayout (가로로 쌓기)
#         hbox_layout = QHBoxLayout()
#         hbox_layout.addWidget(QLabel('가로로 쌓기 예제'))
#         hbox_layout.addWidget(QPushButton('버튼 A'))
#         hbox_layout.addWidget(QPushButton('버튼 B'))
#         hbox_layout.addWidget(QPushButton('버튼 C'))
#         # 3. QGridLayout (격자 형태로 배치)
#         grid_layout = QGridLayout()
#         grid_layout.addWidget(QLabel('격자 형태 예제'), 0, 0)
#         grid_layout.addWidget(QPushButton('버튼 1st'), 1, 0)
#         grid_layout.addWidget(QPushButton('버튼 2nd'), 1, 1)
#         grid_layout.addWidget(QPushButton('버튼 3rd'), 2, 0)
#         grid_layout.addWidget(QPushButton('버튼 4th'), 2, 1)
#         # 4. 여러 레이아웃 합치기(메인)
#         main_layout = QVBoxLayout()
#         main_layout.addLayout(vbox_layout) # 세로로 쌓기
#         main_layout.addLayout(hbox_layout) # 가로로 쌓기
#         main_layout.addLayout(grid_layout) # 격자
#         # 5. 메인 레이아웃 설정
#         container = QWidget()
#         container.setLayout(main_layout) # 메인 레이아웃을 적용
#         self.setCentralWidget(container) # 중앙, 창 전체에 보이도록
# --------------------------------------------------------------------------
# 메인 코드
# app = QApplication([])
# window = MainWindow()
# window.show()
# app.exec()
# ---------------------------------------------------------------------------------
# 라디오 버튼 예제
# ex)
# from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, \
#                             QRadioButton, QVBoxLayout, QHBoxLayout, QWidget
# from PyQt6.QtGui import QIcon
# import os
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         # [창 제목 설정]
#         self.setWindowTitle('My App')
#         # [창 위치 및 크기 지정]
#         self.setGeometry(300, 300, 400, 400)
#         # [아이콘 파일이 있으면 창의 아이콘으로 사용]
#         icon_path = 'cute_python_snake.ico'
#         if os.path.exists(icon_path):
#             icon = QIcon(icon_path)
#             self.setWindowIcon(icon)
#         else: # 아이콘이 없을 때 경고 메세지 출력
#             print(f'경고: 아이콘 파일을 찾을 수 없습니다. ({icon_path})')
#         # ----------------------------------------------------------------------
#         # 1. 성별 선택 안내 레이블 생성
#         self.lable_gender = QLabel('성별 선택')
#         # 2. 라디오 버튼 2개 생성 (남성 / 여성)
#         self.radio1 = QRadioButton('남성')
#         self.radio2 = QRadioButton('여성')
#         # 3. 각 라디오 버튼이 눌릴 떄마다 update_gender 함수 연결
#         self.radio1.toggled.connect(self.update_gender)
#         self.radio2.toggled.connect(self.update_gender)
#         # 4. 성별 라디오버튼을 가로로 정렬하기 위한 레이아웃
#         gender_layout = QHBoxLayout()
#         gender_layout.addWidget(self.radio1) # 남성 라디오 버튼 추가
#         gender_layout.addWidget(self.radio2) # 여성 라디오 버튼 추가
#         # 5. 전체 레이아웃 세팅 (세로로 배치)
#         layout = QVBoxLayout()
#         layout.addLayout(gender_layout) # 성별 서택(가로) 레이아웃 추가
#         layout.addWidget(self.lable_gender)
#         # 6. QWidget 컨테이너에 레이아웃 세팅 후 메인윈도우의 중앙으로 설정
#         container = QWidget()
#         container.setLayout(layout)
#         self.setCentralWidget(container)
#     # 7. 성별 선택 시 호출되는 함수
#     def update_gender(self):
#         if self.radio1.isChecked(): # 라디오버튼1 이 선택되었다 -> 남성 선택
#             self.lable_gender.setText('선택한 성별 : 남성')
#         elif self.radio2.isChecked(): # 라디오버튼2 가 선택되었다 -> 여성 선택
#             self.lable_gender.setText('선택한 성별 : 여성')
# =====================================
# 메인 코드
# app = QApplication([])        
# window = MainWindow()
# window.show()
# app.exec()
# ---------------------------------------------------------