import random


def main():
    while 1:
        menu = input('0.Exit 1.계산기 (+, - , *, /) 2.BMI 계산기 '
                     '3.성적표 4.뭐지 5.주사위 6.랜덤숫자 7.랜덤멤버 8.가위바위보 9.소수점 10.윤년팽년')
        if menu == '0':
            break
        elif menu == '1': # 계산기
            calc = Quiz01Calculator(int(input('첫 번째 수')), int(input('두 번째 수'), input('연산기호')))
            print(f'{calc.num1} {calc.opcode} {calc.num2} = {calc.opcodeSelect()}')
        elif menu == '2': # BMI
            bmi = Quiz02Bmi(input('이름'), int(input('몸무게')), int(input('키')))
            print(f'{bmi.name}님의 결과는 {bmi.op()}')
        elif menu == '3': #Grade
            grade = Quiz03Grade(input('이름'), int(input('국어 점수')), int(input('수학 점수')), int(input('영어 점수')))
            print (f'''\
            {grade.name} 님의 성적표
            국어 점수 : {grade.kor}
            영어 점수 : {grade.eng}
            수학 점수 : {grade.math}
            총점 : {grade.total()}
            평균 : {grade.avg()}
            ''')
        elif menu =='4': #Gradeauto
            for i in ['김유신', '강감찬', '유관순', '윤봉길','신사임당']:
                print()
        elif menu == '5':  # Dice
            print(Quiz05Dice.cast())

        elif menu == '6':  # RandomGenerator
            randonNum = Quiz06RandomGenerator(int(input('범위 설정')))
            print(randonNum.number())


        elif menu == '7':  # RandomChoice
            print(Quiz07RandomChoice().choice())
        elif menu == '8':  # RPS
            q8 = Quiz08Rps(1)
            print(q8.game())
        elif menu == '9':  # GetPrime
            primeValue = Quiz09GetPrime(int(input('숫자 값 입력')))
            print(primeValue.getP())
        elif menu == '10':  # LeapYear
            pass


class Quiz01Calculator(object):
    def __init__(self, num1, num2, opcode):
        self.num1 = num1
        self.num2 = num2
        self.opcode = opcode

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

class Quiz02Bmi(object):
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height
    def op(self):
        re = (self.weight / (self.height**2))*1000
        if re < 18.5:
            return '저체중입니다.'
        elif re < 23:
            return '정상입니다.'
        elif re < 25:
            return '과체중입니다.'
        elif re < 30:
            return '비만입니다.'
        elif re > 30:
            return '고도비만입니다.'

class Quiz03Grade(object):
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
    def total(self): return self.kor + self.eng + self.math
    def avg(self): return (Quiz03Grade.total(self))/3

class Quiz04GradeAuto(object):
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
    def total(self): return self.kor + self.eng + self.math
    def avg(self): return (self.total())/3
    def getGrade(self):pass
    def chkPass(self): # 60점 이상이면 합격
        pass

def myRandom(start, end):
    return random.randint(start, end)

class Quiz05Dice:
    @staticmethod
    def cast():
        return myRandom(1, 6)

class Quiz06RandomGenerator:
    def __init__(self,scope): #원하는 범위의 정수에서 랜덤값 1개 추출
        self.scope = scope
    def number(self): return int(random.random() * self.scope) + 1

class Quiz07RandomChoice:
    def __init__(self): #803호에서 랜덤으로 1명 이름 추출
        self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                        "권혜민", "서성민", "조현국", "김한슬", "김진영",
                        '심민혜' , '권솔이', '김지혜' , '하진희' , '최은아',
                        '최민서', '한성수', '김윤섭', '김승현',
                        "강 민", "최건일", "유재혁", "김아름", "장원종"]
    def choice(self):
        return self.members[myRandom(0, 23)]

class Quiz08Rps(object):
    def __init__(self, user):
        self.user = user
        self.com = myRandom(1.3)

    def game(self):
        c = self.com
        u = self.user
        rps = ['가위', '바위', '보']
        if u ==1:
            if c == 1:
                res = f'플레이어: {rps[0]}, 컴퓨터: {rps[0]}, 결과: 무승부'
            elif c == 2:
                res = f'플레이어: {rps[0]}, 컴퓨터: {rps[1]}, 결과: 패배'
            elif c == 3:
                res = f'플레이어: {rps[0]}, 컴퓨터: {rps[2]}, 결과: 승리'
        elif u == 2:
            if c == 1:
                res = f'플레이어: {rps[0]}, 컴퓨터: {rps[2]}, 결과: 승리'
            elif c == 2:
                res = f'플레이어: {rps[0]}, 컴퓨터: {rps[0]}, 결과: 무승부'
            elif c == 3:
                res = f'플레이어: {rps[0]}, 컴퓨터: {rps[1]}, 결과: 패배'
        elif u == 3:
            if c == 1:
                res = f'플레이어: {rps[0]}, 컴퓨터: {rps[1]}, 결과: 패배'
            elif c == 2:
                res = f'플레이어: {rps[0]}, 컴퓨터: {rps[2]}, 결과: 승리'
            elif c == 3:
                res = f'플레이어: {rps[0]}, 컴퓨터: {rps[0]}, 결과: 무승부'
            else:
                res = '1~3 입력'

            return res


class Quiz09GetPrime:
    def __init__(self, prime):
        self.prime = prime
    def getP(self):
        for i in range(2, 100):
            for j in range(2, i):
                if i%j == 0: self.prime+=1
                return self.prime

class Quiz10LeapYear:
    def __init__(self,year):
        self.year = year
    def leap(self):
        if self.year % 4 == 0 and not self.year%100 == 0 or self.year%400==0: return '윤년'
        else: return '평년'

class Quiz11NumberGolf(object):
    def __init__(self):
        pass
class Quiz12Lotto(object):
    def __init__(self):
        pass
class Quiz13Bank(object): # 이름, 입금, 출금만 구현
    def __init__(self):
        pass
class Quiz14Gugudan(object): # 책받침구구단
    def __init__(self):
        pass


if __name__ == '__main__':
    main()
