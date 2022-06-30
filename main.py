import json

json_directory = "style_data.json"

with open('style_data.json', encoding="utf-8") as f:  # 데이터 불러오기
    data = json.load(f)

result = set()

while True:
    input_data = input("입력 : ")
    sliced_input = input_data.split(" ")

    index = sliced_input[0]  # index이름
    act = sliced_input[1]  # 추가 or 제거

    if act == 0 or act == "추가":
        result = result | set(data[index])  # 합집합
    elif act == 1 or act == "제거":
        result = result - set(data[index])  # 차집합
    print(result)
