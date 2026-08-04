# 지금까지 학습한 내용 통해 재밌는 함수 만들기 예제
import random # random 기능 사용하겠다는 의미

groups = ["에스파", "리센느", "엔믹스", "여자아이들", "아일릿"]

# 랜덤 뽑기
my_group = random.choice(groups)
print(my_group)

def get_random_group():
    groups = [
        {
            "이름": "에스파",
            "리더": "카리나"
        },
        {
            "이름": "리센느",
            "리더": "원이"
        },
        {
            "이름": "여자아이들",
            "리더": "전소연"
        }
    ]
    my_group = random.choice(groups)

    return my_group.get("이름"), my_group.get("리더")
group_name, group_leader = get_random_group()
print(f'{group_name}의 리더는 {group_leader}이다.')

# 3 - 4인 파티
# 가봤거나, 가고싶은 여행지 정보 모으기 (최소 5개 이상)
# 함수 호출 시, 랜덤으로 모아 해당 여행지의 국가이름과 수도
# "환영합니다! 000 나라의 수도 000 입니다!" 출력

# 스페인, 잉글랜드, 프랑스, 이탈리아, 독일
# 마드리드, 런던, 파리, 로마, 베를린

def get_random_country():
    groups = [
        {
            "이름": "스페인",
            "도시": "까탈루냐"
        },
        {
            "이름": "잉글랜드",
            "도시": "런던"
        },
        {
            "이름": "프랑스",
            "도시": "파리"
        },
        {
            "이름": "이탈리아",
            "도시": "밀라노"
        },
        {
            "이름": "독일",
            "도시": "뮌헨"
        }
    ]
    my_country = random.choice(groups)
    return my_country.get("이름"), my_country.get("도시")

group_country_name, group_country_city = get_random_country()
print(f'환영합니다! {group_country_name} 나라의 축구 성지 {group_country_city}입니다!')
