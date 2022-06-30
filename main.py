data = {"타이틀": ["티몬 몬소리체",
                "스웨거체",
                "배민 도현체",
                "여기어때 잘난체",
                "검은 고딕체",
                "g마켓 산스",
                "구글 noto sans", ],
        "본문": ["나눔 바른고딕/얇게,굵게",
               "kopup돋움",
               "rix고딕",
               "윤고딕",
               "맑은 고딕",
               "스포카 한 산스"],
        "포스터": ["양진체 - 타이포 그래피 ( 유료화됨)",
                "쿠키런",
                "검은고딕",
                "말싸미815",
                "116수박화체",
                "헤드라인",
                "hs두꺼비체",
                "hs봄바람체",
                "베스킨라빈스b"]
        }

result = set()

while True:
    input_data = input("입력 : ")
    sliced_input = input_data.split(" ")
    index = sliced_input[0]
    act = sliced_input[1]
    if act == 0 or act == "추가":
        result = result | set(data[index])
    elif act == 1 or act == "제거":
        result = result - set(data[index])
    print(result)
