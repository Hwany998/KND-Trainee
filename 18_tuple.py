tup = (
    "normal",
    "normal", 
    "warning", 
    "normal",
    "warning"
)
print(len(tup)) #5
print(tup.count("warning")) #2  warning 2개 - 없는 값 찾으면 0
print(tup.index("warning")) #2  첫 위치, 2번 인덱스 - 없는 값 찾으면 오류
#count와 index의 차이, 없는 값 찾을 시 count는 0, index는 오류

