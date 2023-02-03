# professor = "Honggeol Ryu"
# a = 1
# # 이건 주석이라고 합니다.
# print("professor")
# print("a")
# print("b")
#
#
#
# print(professor)
# print("Honggeol Ryu")
# print("Honggeol Ryu")
# a = 7
# b = 5
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)
#
# print("a+b")
import string

# a = 1
# b = 1
# print(a, b)
# print(type(a), type(b))
# a = 1.5
# b = 3.5
# print(a, b)
# print(type(a), type(b))
# a = "ABC"
# b = "10101010"
# print(a, b)
# print(type(a), type(b))
#
# a = True
# b = False
# print(a, b)
# print(type(a), type(b))
#
# print(2 ** 8)
# print(7 / 2) #자동으로 실수형
# print(7 // 2) # 정수형으로 몫만 알고 싶을 때


# a = input()
# b = input()
# num1 = int(a)
# num2 = int(b)
# print(num1 + num2)
# # print(type(a))
# userInput = input() #type = string
# celisius = float(userInput) #float
# fahrenhit = (celisius * 1.8) + 32
#
# print(f"사용자가 입력한 섭씨 온도: {celisius} 입니다.")
# print(f"변환한 화씨 온도: {fahrenhit} 입니다.")
#
# # print("썹시온도" + celisius + "입니다.") #비효율적
# a = "썹시온도는 {0},{1}입니다.".format(celisius, fahrenhit)
# print(a)

# a = 'red'
# b = 'blue'
# c = 'green'
# clolors = ['red', 'blue', 'green']
#
# print(clolors[0])
# print(clolors[1])
# print(clolors[2])
# print(clolors)
# clolors = [a, b, c]
#
# numbers = [5, 6, 8, 9]

# cities = ['서울', '부산', '인천', '대구', '대전', '광주', '울산', '수원']
# print(cities[0:6])
# print(cities[3])
# print(cities[5:])
# print(cities[-1])

# color = ['red', 'blue', 'green']
# color2 = ['orange', 'black', 'white']
#
# print(len(color))
# total_color = color + color
# print(total_color)
#
# print('blue' in color)
# print('blue' in color2)
# color.append('purple')
# print(color)
#
# color.extend(['black', 'white'])
# print(color)
#
# color.insert(0, 'orange')
# print(color)
#
# color.remove('red')
# print(color)
#
# print(color[0])
# color[0] = 'skyblue'
# print(color)
#
# #패킹 언패킹
# t = [1, 2, 3]
# a, b, c = t

# print(a, b, c)

# a_list = [1, 2, 3]
# b_list = [4, 5, 6]
# c_list = [a_list, b_list]
# print(c_list)
# print(c_list[0])
# print(c_list[1])

# print("I eat %d apples" % 3) #정수 넣기
# print("I eat %s apples" % "five") #문자열 넣기
# number = 3
# print("I eat %d apples" % number) #변수 넣기
# print("I eat %0.2f apples" % 1.456465) #소수점 자리수 지정
# print("%10s" % "hi") #공백주기
# print("%-10sjane" % "hi")

kor_score = [49, 70, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]

midterm_score = [kor_score, math_score, eng_score]
math_score[0] = 1000
print(math_score)
print(midterm_score[1][2])

print(midterm_score)





