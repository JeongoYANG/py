from hello.domains import Member
from hello.models import Quiz01Calculator, Quiz02Bmi, Quiz03Grade, Quiz05Dice, Quiz06RandomGenerator, \
    Quiz07RandomChoice, Quiz08Rps, Quiz09GetPrime

if __name__ == '__main__':
    while 1:
        menu = input('0.Exit 1.계산기 (+, - , *, /) 2.BMI 계산기 '
                     '3.성적표 4.뭐지 5.주사위 6.랜덤숫자 7.랜덤멤버 8.가위바위보 9.소수점 10.윤년팽년')
        if menu == '0':
            break
        elif menu == '1': # 계산기
            calc = Quiz01Calculator(int(input('첫 번째 수')), int(input('두 번째 수'), input('연산기호')))
            print(f'{calc.num1} {calc.opcode} {calc.num2} = {calc.opcodeSelect()}')
        elif menu == '2': # BMI
            member = Member()
            bmi = Quiz02Bmi()
            member.name = input('이름')
            member.height = float(input('키'))
            member.weight = float(input('몸무게'))
            res = bmi.op(member)
            print(f'이름 : {member.name}, 키 : {member.height}'
                  f'몸무게 : {member.weight}, BMI상태 : {res}')
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