# 문제
# 커서는 문장의 맨 앞(첫 번째 문자의 왼쪽), 문장의 맨 뒤(마지막 문자의 오른쪽), 또는 문장 중간 임의의 곳(모든 연속된 두 문자 사이)에 위치할 수 있다. 즉 길이가 L인 문자열이 현재 편집기에 입력되어 있으면, 커서가 위치할 수 있는 곳은 L+1가지 경우가 있다.
# L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
# D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
# B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨) 삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
# P $	$라는 문자를 커서 왼쪽에 추가함
# 초기에 편집기에 입력되어 있는 문자열이 주어지고, 그 이후 입력한 명령어가 차례로 주어졌을 때, 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 구하는 프로그램을 작성하시오. 단, 명령어가 수행되기 전에 커서는 문장의 맨 뒤에 위치하고 있다고 한다.
# 입력
# 첫째 줄에는 초기에 편집기에 입력되어 있는 문자열이 주어진다. 이 문자열은 길이가 N이고, 영어 소문자로만 이루어져 있으며, 길이는 100,000을 넘지 않는다. 둘째 줄에는 입력할 명령어의 개수를 나타내는 정수 M(1 ≤ M ≤ 500,000)이 주어진다. 셋째 줄부터 M개의 줄에 걸쳐 입력할 명령어가 순서대로 주어진다. 명령어는 위의 네 가지 중 하나의 형태로만 주어진다.
# 출력
# 첫째 줄에 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 출력한다.

import sys

string_list = list(sys.stdin.readline()) # 문자열을 list 한다
cursor = len(string_list) # 문자열 길이

for _ in range(int(input())):
    command = list(sys.stdin.readline()) # 명령값
    if command[0] == 'P':
        string_list.insert(cursor, command[1]) # 문자열 길이만큼 이동 후 command[1] 입력
        cursor += 1 # 문자 1개 추가되었으니 +1
    elif command[0] == 'L': 
        if cursor > 0: 
            cursor -= 1  # L은 [1]부터 맨 뒤자리에서만 의미있다. 0은 의미가 없다. cursor -1 해서 커서를 왼쪽으로 옮긴다. 
    elif command[0] == 'D':
        if cursor < len(string_list): 
            cursor += 1  # D는 [0]부터 len(string_list)-1 에서만 의미있다. 맨 뒤는 의미가 없다. cursor +1 해서 커서를 오른쪽으로 옮긴다.  
    else:
        if cursor > 0:
            string_list.remove(string_list[cursor-1]) # B 커서는 문장의 맨 뒤에 있다. 따라서, 왼쪽 문자열을 지우기위해 전체 문자열 길이 - 1의 인덱스를 넣어야함. 

print(''.join(string_list))
