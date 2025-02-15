STATION_CODE = {
    "수서": "0551",
    "동탄": "0552",
    "평택지제": "0553",
    "천안아산": "0502",
    "오송": "0297",
    "대전": "0010",
    "공주": "0514",
    "익산": "0030",
    "정읍": "0033",
    "광주송정": "0036",
    "나주": "0037",
    "목포": "0041",
    "김천구미": "0507",
    "서대구": "0506",
    "동대구": "0015",
    "신경주": "0508",
    "울산(통도사)": "0509",
    "울산": "0509",
    "통도사": "0509",
    "부산": "0020",
}

STATION_NAME = {v: k for (k, v) in STATION_CODE.items()}

TRAIN_NAME = {
    "00": "KTX",
    "02": "무궁화",
    "03": "통근열차",
    "04": "누리로",
    "05": "전체",
    "07": "KTX-산천",
    "08": "ITX-새마을",
    "09": "ITX-청춘",
    "10": "KTX-산천",
    "17": "SRT",
}

WINDOW_SEAT = {None: "000", True: "012", False: "013"}
