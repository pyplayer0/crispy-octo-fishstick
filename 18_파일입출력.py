#open(파일명, 열기모드, encoding='인코딩')
#열기모드
# r: read (읽기)
# a: append (이어서 쓰기)
# w: write (쓰기)

# 파일 쓰기
f = open('list.txt','w',encoding='utf8')
f.write('김\n')
f.write('태\n')
f.write('환')

# 파일 읽기
f = open('list.txt','r',encoding='utf8')
contents = f.read()
print(contents)
f.close()

# with (자동으로 파일을 닫아주어 클로즈 함수를 호출안해도됨)
#f = open('list.txt','r',encoding='utf8')
#             ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓    
# with open('list.txt','r',encoding='utf8') as f:
#f.close()는 생략
