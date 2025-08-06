import re

def is_valid_email(email: str) -> bool:
    """
    이메일 주소가 유효한지 정규표현식으로 검사합니다.
    """
    # 정규표현식 패턴 설명:
    # ^ : 문자열의 시작
    # [a-zA-Z0-9_.+-]+ : 영어 대소문자, 숫자, 밑줄(_), 점(.), 더하기(+), 빼기(-) 중 하나 이상이 올 수 있음 (이 부분이 이메일의 '이름' 부분)
    # @ : 꼭 @ 기호가 있어야 함 (이메일의 이름과 도메인을 구분)
    # [a-zA-Z0-9-]+ : 영어 대소문자, 숫자, 빼기(-) 중 하나 이상이 올 수 있음 (이 부분이 도메인 이름)
    # \. : 꼭 점(.)이 있어야 함 (도메인과 확장자를 구분)
    # [a-zA-Z0-9-.]+ : 영어 대소문자, 숫자, 점(.), 빼기(-) 중 하나 이상이 올 수 있음 (이 부분이 도메인의 확장자 부분)
    # $ : 문자열의 끝
    #
    # 쉽게 말하면, '이름@도메인.확장자' 모양이어야 하고,
    # 이름에는 영어, 숫자, _, ., +, -가 올 수 있고,
    # 도메인에는 영어, 숫자, -가 올 수 있고,
    # 확장자에는 영어, 숫자, ., -가 올 수 있어요!
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}$'
    #pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

if __name__ == "__main__":
    test_emails = [
        "test@example.com",
        "user.name+tag@domain.co.kr",
        "invalid-email@",
        "another.test@domain",
        "good_email123@sub.domain.com",
        "hello.world@sample.net",
        "user@localhost",
        "user@.com",
        "user_name@domain.org",
        "user-name@domain.io",
        "user@domain",
        "user@domain.c"
    ]
    for email in test_emails:
        print(f"{email}: {'유효함' if is_valid_email(email) else '유효하지 않음'}")