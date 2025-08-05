# list, dict, tuple, set 형식 비교 코드

# 1. 자료형 선언
my_list = [1, 2, 3]
my_dict = {"a": 1, "b": 2, "c": 3}
my_tuple = (1, 2, 3)
my_set = {1, 2, 3}

# 2. 자료형 타입 출력
print("자료형 타입 비교:")
print(f"list 타입: {type(my_list)}")
print(f"dict 타입: {type(my_dict)}")
print(f"tuple 타입: {type(my_tuple)}")
print(f"set 타입: {type(my_set)}\n")

# 3. 특징 비교
print("자료형 특징 비교:")

# list
print("리스트(list):")
print(f"  값: {my_list}")
print("  - 순서 있음, 변경 가능 (mutable), 중복 허용\n")

# dict
print("딕셔너리(dict):")
print(f"  값: {my_dict}")
print("  - key-value 쌍, key는 중복 불가, 순서 보장(Python 3.7+), 변경 가능\n")

# tuple
print("튜플(tuple):")
print(f"  값: {my_tuple}")
print("  - 순서 있음, 변경 불가 (immutable), 중복 허용\n")

# set
print("세트(set):")
print(f"  값: {my_set}")
print("  - 순서 없음, 변경 가능 (mutable), 중복 허용 안 함, 집합 연산 가능\n")

# 4. 변경 가능 여부 테스트
print("변경 가능 여부 테스트:")

# list 변경
my_list[0] = 100
print(f"리스트 변경 후: {my_list}")

# dict 변경
my_dict["a"] = 100
print(f"딕셔너리 변경 후: {my_dict}")

# set 변경 (요소 추가)
my_set.add(4)
print(f"세트 변경(4 추가) 후: {my_set}")

# tuple 변경 시도
try:
    my_tuple[0] = 100
except TypeError as e:
    print(f"튜플 변경 시도 -> 에러 발생: {e}")
