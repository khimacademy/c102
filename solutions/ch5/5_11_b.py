'''
5-11. 순번
순번은 1st나 2nd처럼 리스트에서의 위치를 나타냅니다. 1, 2, 3을 제외한 대부분의 순번은 th로 끝납니다.
- 1부터 9까지의 숫자를 리스트에 저장하세요.
- 리스트에 루프를 실행하세요.
- 루프 안에서 if-elif-else 문을 실행해 각 숫자에 맞는 순번을 출력하세요. 출력 결과는 "1st 2nd 3rd 4th 5th 6th 7th 8th 9th" 여야 하며 각 결과가 서로 다른 행에 있어야 합니다.

Output:
1st
2nd
3rd
4th
5th
6th
7th
8th
9th
'''

numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(str(number) + 'th')

