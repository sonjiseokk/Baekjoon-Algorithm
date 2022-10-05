# 문제
# 입력받은 문자열에서 자주 쓰인 알파벳이 무엇인지 알려줘야하는 문제

# upper을 통해 대문자로 전부 변환 후, 집합 자료형을 통해 카운팅 해야할 문자들만 추리고
# 반복문을 돌려가며 카운팅을 하고 이후에 max를 통해 가장 많이 사용된(숫자가 큰) 인덱스를 찾아 출력

word = input()

word = word.upper()
check_set = list(set(word))
count_num_list = []
for i in check_set:
    count_repeat = word.count(i)
    count_num_list.append(count_repeat)

if count_num_list.count(max(count_num_list)) > 1:
    print('?')
else:
    max_index = count_num_list.index(max(count_num_list))
    print(check_set[max_index])