import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from PIL import ImageTk,Image
from datetime import datetime

win = tk.Tk()
win.geometry('1900x1100+0+0')
win.title("부산 노선도")

def time():
    settime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    timelabel.config(text="현재시각 : " + settime)
    win.after(1000, time)
    
def set_start_station(e):
    selected_station = start_combobox.get()
    input_entry.delete(0, END)
    input_entry.insert(0, selected_station)
    
def set_end_station(e):
    selected_station = end_combobox.get()
    destination_entry.delete(0, END)
    destination_entry.insert(0, selected_station)
    
def start_info():
    label_1.config(text="출발 : " + input_entry.get())
    
def end_info():
    label_2.config(text="도착 : " + destination_entry.get())
    
def reset_func():
    input_entry.delete(0, END)
    destination_entry.delete(0, END)
    searchlist1.delete(0, END)
    searchlist2.delete(0, END)
    
def doubleclick1(e):
    double1 = searchlist1.get(ACTIVE)
    input_entry.delete(0, END)
    input_entry.insert(0, double1)
    label_1.config(text="출발 : " + input_entry.get())
    
def doubleclick2(e):
    double2 = searchlist2.get(ACTIVE)
    destination_entry.delete(0, END)
    destination_entry.insert(0, double2)
    label_2.config(text="도착 : " + destination_entry.get())
    
def word1():
    keyword_list = keyword.get(input_entry.get()[0], [])
    searchlist1.delete(0, END)
    for item in keyword_list:
        searchlist1.insert(END, item)
    
    label_1.config(text="출발 : " + input_entry.get())

def word2():
    keyword_list = keyword.get(destination_entry.get()[0], [])
    searchlist2.delete(0, END)
    for item in keyword_list:
        searchlist2.insert(END, item)
        
    label_2.config(text="도착 : " + destination_entry.get())
    
def word3():
    keyword_list = keyword.get(start_combobox.get()[0], [])
    searchlist1.delete(0, END)
    for item in keyword_list:
        searchlist1.insert(END, item)
        
    label_1.config(text="출발 : " + start_combobox.get())
    
def word4():
    keyword_list = keyword.get(end_combobox.get()[0], [])
    searchlist2.delete(0, END)
    for item in keyword_list:
        searchlist2.insert(END, item)
        
    label_2.config(text="도착 : " + end_combobox.get())
    
    
def Enterfunc1(e):
    word1()
    
    
def Enterfunc2(e):
    word2()
    
    
def Enterfunc3(e):
    word3()
    
def Enterfunc4(e):
    word4()

frame1came1 = tk.Frame(win, height=1100 , width=400 ,background='lightgray')
frame1came1.grid(row=0, column=0,sticky="nwse")   
frame2came1 = tk.Frame(win, height=1100, width=1500, background='white')
frame2came1.grid(row=0, column=1)

Lframe_top = tk.Frame(frame1came1, width=400, height=275, background='lightgray')
Lframe_top.pack(anchor='nw',expand=True,fill='both')

Lframe_bottom = tk.Frame(frame1came1, width=400, height=275, background='lightgray')
Lframe_bottom.pack(anchor='se',expand=True,fill='both')


traincanvas = tk.Canvas(frame2came1,width=1485,height=1080,relief='solid',bd=0,background='white')
traincanvas.place(x=5,y=10)   #노선도 그리는 칸

start_list = ["노포","범어사","남산","두실","구서","장전","부산대","온천장","명륜","동래","교대","연산",
            "시청","양정","부전","서면","범내골","범일","좌천(1호선)","부산진","초량","부산역","중앙",
            "남포","자갈치","토성","동대신","서대신","대티","괴정","사하","당리","하단","신평","동매",
            "장림","신장림","낫개","다대포항","다대포해수욕장","양산","남양산","부산대양산캠퍼스","증산",
            "호포","금곡","동원","율리","화명","수정","덕천","구명","구남","모라","모덕","덕포","사상",
            "감전","주례","냉정","개금","동의대","가야","부암","전포","국제금융센터·부산은행","지게골",
            "못골","대연","경성대·부경대","남천","금련산","광안","수영","민락","센텀시티","백스코(시립미술관)",
            "동백","대저","체육공원","강서구청","구포","숙등","남산정","만덕","미남","사직","종합운동장",
            "거제","물만골","배산","망미","수안","낙민","충렬사","명장","서동","금사","반여농산물시장",
            "석대","영산대","윗반송","고촌","안평","거제해맞이","동래(동해선)","안락","부산원동","재송",
            "센텀","신해운대","송정","오시리아","기장","일광","좌천(동해선)","월내","서생","남창","망양",
            "덕하","개운포","태화강","가야대","장신대","연지공원","박물관","수로왕릉","봉황","부원","김해시청",
            "인제대","김해대학","지내","불암","대사","평강","대저","등구","덕두","김해공항","서부산유통지구",
            "괘법르네시떼","사상"]

end_list = ["노포","범어사","남산","두실","구서","장전","부산대","온천장","명륜","동래","교대","연산",
            "시청","양정","부전","서면","범내골","범일","좌천(1호선)","부산진","초량","부산역","중앙",
            "남포","자갈치","토성","동대신","서대신","대티","괴정","사하","당리","하단","신평","동매",
            "장림","신장림","낫개","다대포항","다대포해수욕장","양산","남양산","부산대양산캠퍼스","증산",
            "호포","금곡","동원","율리","화명","수정","덕천","구명","구남","모라","모덕","덕포","사상",
            "감전","주례","냉정","개금","동의대","가야","부암","전포","국제금융센터·부산은행","지게골",
            "못골","대연","경성대·부경대","남천","금련산","광안","수영","민락","센텀시티","백스코(시립미술관)",
            "동백","대저","체육공원","강서구청","구포","숙등","남산정","만덕","미남","사직","종합운동장",
            "거제","물만골","배산","망미","수안","낙민","충렬사","명장","서동","금사","반여농산물시장",
            "석대","영산대","윗반송","고촌","안평","거제해맞이","동래(동해선)","안락","부산원동","재송",
            "센텀","신해운대","송정","오시리아","기장","일광","좌천(동해선)","월내","서생","남창","망양",
            "덕하","개운포","태화강","가야대","장신대","연지공원","박물관","수로왕릉","봉황","부원","김해시청",
            "인제대","김해대학","지내","불암","대사","평강","대저","등구","덕두","김해공항","서부산유통지구",
            "괘법르네시떼","사상"]

keyword = {
    "ㄱ" : ['가야', '가야대', '감전', '강서구청', '개금', '개운포', '거제', '거제해맞이', '경성대·부경대', '고촌'
, '광안', '괘법르네시떼', '괴정', '교대', '구남', '구명', '구서', '구포', '국제금융센터·부산은행'
, '금곡', '금련산', '금사', '기장', '김해공항', '김해대학', '김해시청'],
    
    "ㄴ" : ['낙민', '남산', '남산정', '남양산', '남창', '남천', '남포', '낫개', '냉정', '노포'],
    "ㄷ" : ['다대포항', '다대포해수욕장', '당리', '대사', '대연', '대저', '대저',
           '대티', '덕두', '덕천', '덕포', '덕하', '동대신', '동래', '동래(동해선)', '동매', '동백', '동원', '동의대', '두실', '등구'],
    "ㅁ" : ['만덕', '망미', '망양', '명륜', '명장', '모덕', '모라', '못골', '물만골', '미남','민락'],
    "ㅂ" : ['박물관', '반여농산물시장', '배산', '백스코(시립미술관)', '범내골', '범어사', '범일', '봉황', '부산대', '부산대양산캠퍼스', '부산역', '부산원동', '부산진', '부암', '부원', '부전'],
    "ㅅ" : ['사상', '사상','사직', '사하', '서대신', '서동', '서면', '서부산유통지구', '서생', '석대', '센텀', '센텀시티', '송정', '수로왕릉', '수안', '수영', '수정', '숙등', '시청', '신장림', '신평', '신해운대'],
    "ㅇ" : ['안락', '안평', '양산','양정', '연산', '연지공원', '영산대', '오시리아', '온천장', '월내', '윗반송', '율리', '인제대', '일광'],
    "ㅈ" : ['자갈치', '장림', '장신대', '장전', '재송', '전포', '종합운동장', '좌천(1호선)', '좌천(동해선)', '주례','중앙', '증산', '지게골', '지내'],
    "ㅌ" : ['태화강', '토성'],
    "ㅎ" : ['하단', '호포', '화명']
}

# 지하철 역과 노선 정보
subway_stations_1 = {
    '노포': (1415, 98),
    '범어사': (1343, 98),
    '남산': (1272, 98),
    '두실': (1200, 98),
    '선릉': (1129, 98),
    '장전': (1057,98),
    '부산대': (986,98),
    '온천장': (915,98),
    '명륜': (843,98),
    '동래': (807,251),
    '교대': (807,385),
    '연산': (807,510),
    '시청': (807,582),
    '양정': (807,666),
    '부전': (807,750),
    '서면': (807,837),
    '범내골': (807,909),
    '범일': (807,980),
    '좌천': (778,1020),
    '부산진': (744,1020),
    '초량': (711,1020),
    '부산역': (677,1020),
    '중앙': (643,1020),
    '남포': (610,1020),
    '자갈치': (577,1020),
    '토성': (543,1020),
    '동대신': (510,1020),
    '서대신': (476,1020),
    '대티': (443,1020),
    '과정': (410,1020),
    '사하': (376,1020),
    '당리': (343,1020),
    '하단': (309,1020),
    '신평': (275,1020),
    '동매': (241,1020),
    '장림': (208,1020),
    '신장림': (175,1020),
    '낫개': (142,1020),
    '다대포항': (108,1020),
    '다대포해수욕장': (74,1020),
}

subway_lines_1 = [
    ['노포', '범어사', '남산', '두실', '선릉', '장전', '부산대', '온천장', '명륜', '동래', '교대', '연산', '시청', '양정', '부전', '서면', '범내골', '범일', '좌천', '부산진', '초량', '부산역', '중앙',
     '남포', '자갈치', '토성', '동대신', '서대신', '대티', '과정', '사하', '당리', '하단', '신평', '동매', '장림', '신장림', '낫개', '다대포항', '다대포해수욕장'],

] 

subway_stations_2 = {
    '양산': (728,98),
    '남양산': (682,98),
    '부산대중앙캠퍼스': (635,98),
    '중산': (586,98),
    '호포': (539,98),
    '금곡': (492,98),
    '동원': (445,104),
    '율리': (429,148),
    '화명': (429,288),
    '수정': (429,391),
    '덕천': (429,510),
    '구명': (429,561),
    '구남': (429,619),
    '모라': (429,675),
    '모덕': (429,732),
    '덕포': (429,787),
    '사상': (453,837),
    '감전': (504,837),
    '주례': (547,837),
    '냉정': (589,837),
    '개금': (632,837),
    '동의대': (675,837),
    '가야': (719,837),
    '부암': (761,837),
    '서면': (807,837),
    '전포': (853,837),
    '국제금융센터 - 부산은행': (883,837),
    '문현': (915,837),
    '지게골': (947,837),
    '못골': (976,837),
    '대연': (1006,837),
    '경성대*부경대': (1039,805),
    '남천': (1041,735),
    '금련산': (1041,665),
    '광안': (1041,594),
    '수영': (1055,510),
    '민락': (1113,510),
    '센텀시티': (1172,510),
    '벡스코': (1226,510),
    '동백': (1277,510),
    '해운대': (1322,510),
    '중동': (1368,510),
    '장산': (1415,510),   
}

subway_lines_2 = ['양산', '남양산','부산대양산캠퍼스','중산','호포','금곡','동원','율리','화명','수정','덕천','구명',
                  '구남','모라','모덕','덕포','사상','감전','주례','냉정','개금','동의대','가야','부암','서면','전포',
                  '국제금융센터*부산은행','문헌','지게골','못골','대연','경성대*부경대','남천','금련산','광안','수영',
                  '민락','센텀시티','벡스코','동백','해운대','중동','장산']

subway_stations_3 = {
    '대저': (74,510),
    '체육공원': (165,510),
    '강서구청': (253,510),
    '구포': (342,510),
    '덕천': (429,510),
    '숙동': (488,510),
    '남산정': (532,510),
    '만덕': (578,510),
    '미남': (611,510),
    '사직': (658,510),
    '종합운동장': (694,510),
    '거제': (739,510),
    '연산': (807,510),
    '물만골': (867,510),
    '배산': (922,510),
    '망미': (976,510),
    '수영': (1055,510),
}

subway_lines_3 = ['대저','체육공원','강서구청','구포','덕천','숙동','남산정','만덕','미남','사직','종합운동장','거제','연산',
                  '물만골','배산','망미','수영']

subway_stations_4 = {
    '안평': (1415,251),
    '고촌': (1364,251),
    '웟반송': (1314,251),
    '영산대': (1263,251),
    '석대': (1213,251),
    '반여농산물시장': (1163,251),
    '금사': (1113,251),
    '서동': (1062,251),
    '명장': (1012,251),
    '충렬사': (962,251),
    '낙민': (908,251),
    '수안': (861,251),
    '동래': (807,251),
    '미남': (611,510),
}

subway_lines_4 = ['안평','고촌','웟반송','영산대','석대','반여농산물시장','금사','서동','명장','충렬사','낙민',
    '수안','동래', '미남']

subway_stations_Donhae = {
    '태화강': (1415,836),
    '개운포': (1390,836),
    '덕하': (1966,836),
    '망양': (1341,836),
    '남창': (1317,836),
    '서생': (1293,836),
    '월내': (1269,836),
    '좌천': (1226,780),
    '일광': (1226,737),
    '기장': (1226,694),
    '오시리아': (1226,651),
    '송정': (1226,608),
    '신해운대': (1226,565),
    '벡스코': (1226,510),
    '센텀': (1205,385),
    '재송': (1126,385),
    '부산원동': (1047,385),
    '안락': (969,385),
    '동래': (891,385),
    '교대': (807,385),
    '거제': (739,510),
    '거제해맞이': (739,614),
    '부전': (739,721)
}

subway_lines_Donhae = [
    ['태화강', '개운포', '덕하', '망양', '남창', '서생', '월내', '좌천', '일광', '기장', '오시리아', '송정', '신해운대', '벡스코',
     '센텀', '재송', '부산원동', '안락', '동래', '교대', '거제', '거제해맞이', '부전']

]

subway_stations_BusanGimhae = {
    '가야대': (408,98),
    '장신대': (375,98),
    '연지공원': (338,98),
    '박물관': (301,98),
    '수로왕릉': (265,98),
    '봉황': (228,98),
    '부원': (192,98),
    '김해시청': (155,98),
    '인제대': (118,98),
    '김해대학': (85,109),
    '지내': (74,173),
    '불암': (74,251),
    '대사': (74,328),
    '평강': (74,406),
    '대저': (74,510),
    '등구': (74,627),
    '덕두': (74,755),
    '공항': (149,837),
    '서부산유통지구': (235,837),
    '괘법르네시떼': (320,837),
    '사상': (453,837)  
}

subway_lines_BusanGimhae = [
    ['가야대', '장신대', '연지공원', '박물관', '수로왕릉', '봉황', '부원', '김해시청', '인제대', '김해대학', '지내', '불암',
     '대사', '평강', '대저', '등구', '덕두', '공항', '서부산유통지구', '괘법르네시떼', '사상']
    
]




#노선도 좌표 만들기
line_1= traincanvas.create_line(1415,98,1343,98,1343,98,1272,98,1200,98,1129,98,1057,98,986,98,915,98,843,98,807,251,807,385,
                                807,510,807,582,807,666,807,750,807,837,807,909,807,980,778,1020,744,1020,711,1020,677,1020,643,1020,
                                610,1020,577,1020,543,1020,510,1020,476,1020,443,1020,410,1020,376,1020,343,1020,309,1020,
                                275,1020,241,1020,208,1020,175,1020,142,1020,108,1020,74,1020,width=10, fill="orange")    #1호선

line_2= traincanvas.create_line(728,98,682,98,635,98,586,98,539,98,492,98,445,104,429,148,429,288,429,391,429,510,429,561,429,619,
                                429,675,429,732,429,787,453,837,504,837,547,837,589,837,632,837,719,837,761,837,807,837,853,837,883,837,
                                915,837,947,837,976,837,1006,837,1039,805,1039,735,1039,665,1039,594,1055,510,1113,510,1172,510,
                                1172,510,1226,510,1277,510,1322,510,1368,510,1415,510, width=10, fill="light green")  #2호선

line_3= traincanvas.create_line(74,510,165,510,253,510,342,510,428,510,488,510,532,510,611,510,658,510,694,510,739,510,807,510,
                                867,510,922,510,976,510,1055,510, width=10,fill="gold")   #3호선

line_4= traincanvas.create_line(1415,251,1364,251,1314,251,1263,251,1213,251,1163,251,1113,251,1062,251,962,251,908,251,861,251,
                                807,251,611,251,611,510, width=10, fill="skyblue")  #4호선

line_5= traincanvas.create_line(408,98,375,98,338,98,301,98,265,98,228,98,192,98,155,98,118,98,85,109,74,173,74,251,74,328,74,406,
                                74,510,74,627,74,755,149,837,235,837,320,837,453,837, width=10,fill="mediumpurple")   #부산김해경전철

line_6= traincanvas.create_line(1415,836,1390,836,1366,836,1341,836,1317,836,1293,836,1269,836,1226,780,1226,737,1226,694,1226,651,
                                1226,608,1226,565,1226,511,1205,385,1047,385,969,385,891,385,807,385,739,510,739,614,739,721, width=10, fill="blue")    #동해선


# 함수 추가: 마우스 클릭 이벤트 핸들러
def show_station(event):
    x = event.x
    y = event.y
    # 반복문을 통해 클릭한 좌표와 가장 가까운 역을 찾음
    closest_station = None
    min_distance = float('inf')
    for station, (station_x, station_y) in subway_stations_1.items():
        distance = ((x - station_x) ** 2 + (y - station_y) ** 2) ** 0.5
        if distance < min_distance:
            closest_station = station
            min_distance = distance
    for station, (station_x, station_y) in subway_stations_2.items():
        distance = ((x - station_x) ** 2 + (y - station_y) ** 2) ** 0.5
        if distance < min_distance:
            closest_station = station
            min_distance = distance
    for station, (station_x, station_y) in subway_stations_3.items():
        distance = ((x - station_x) ** 2 + (y - station_y) ** 2) ** 0.5
        if distance < min_distance:
            closest_station = station
            min_distance = distance
    for station, (station_x, station_y) in subway_stations_4.items():
        distance = ((x - station_x) ** 2 + (y - station_y) ** 2) ** 0.5
        if distance < min_distance:
            closest_station = station
            min_distance = distance
    for station, (station_x, station_y) in subway_stations_Donhae.items():
        distance = ((x - station_x) ** 2 + (y - station_y) ** 2) ** 0.5
        if distance < min_distance:
            closest_station = station
            min_distance = distance
    for station, (station_x, station_y) in subway_stations_BusanGimhae.items():
        distance = ((x - station_x) ** 2 + (y - station_y) ** 2) ** 0.5
        if distance < min_distance:
            closest_station = station
            min_distance = distance                                        
    # 클릭한 역을 캔버스에 표시
    if closest_station:
        if input_entry.get() == "":  # 출발역이 입력되지 않은 경우
            input_entry.delete(0, tk.END)
            input_entry.insert(0, closest_station)  # 출발역 입력
        else:
            destination_entry.delete(0, tk.END)
            destination_entry.insert(0, closest_station)  # 도착역 입력


# 지하철 노선도 그리기
for line in subway_lines_BusanGimhae:
    for i in range(len(line) - 1):
        start_station = subway_stations_BusanGimhae[line[i]]
        end_station = subway_stations_BusanGimhae[line[i + 1]]
        traincanvas.create_line(start_station[0], start_station[1], end_station[0], end_station[1], fill='mediumpurple', width=3)

# 지하철 역 표시
for station, (x, y) in subway_stations_BusanGimhae.items():
    traincanvas.create_oval(x - 7, y - 7, x + 7, y + 7, fill='white', outline="mediumpurple", width=2.5)

def show_coordinates(event):
    x = event.x
    y = event.y
    traincanvas.coords(cursor_text, x, y)
    traincanvas.itemconfigure(cursor_text, text=f"   ({x}, {y})")
    
def draw_subway_map(canvas):
    # 지하철 노선 그리기
    for line in subway_lines_1:
        for i in range(len(line) - 1):
            start_station = subway_stations_1[line[i]]
            end_station = subway_stations_1[line[i + 1]]
            canvas.create_line(start_station[0], start_station[1], end_station[0], end_station[1], fill='orange', width=3)

    # 지하철 역 표시
    for station, (x, y) in subway_stations_1.items():
        canvas.create_oval(x - 7, y - 7, x + 7, y + 7, fill='white', outline="orange", width=2.5)
    for station, (x, y) in subway_stations_2.items():
        canvas.create_oval(x - 7, y - 7, x + 7, y + 7, fill='white', outline="light green", width=2.5)
    for station, (x, y) in subway_stations_3.items():
        canvas.create_oval(x - 7, y - 7, x + 7, y + 7, fill='white', outline="gold", width=2.5)       
    for station, (x, y) in subway_stations_4.items():
        canvas.create_oval(x - 7, y - 7, x + 7, y + 7, fill='white', outline="sky blue", width=2.5)
    for station, (x, y) in subway_stations_Donhae.items():
        canvas.create_oval(x - 7, y - 7, x + 7, y + 7, fill='white', outline="blue", width=2.5)
    for station, (x, y) in subway_stations_BusanGimhae.items():
        canvas.create_oval(x - 7, y - 7, x + 7, y + 7, fill='white', outline="mediumpurple", width=2.5)            

# 지하철 노선도 그리기
draw_subway_map(traincanvas)

# 마우스 이벤트 바인딩
traincanvas.bind("<Motion>", show_coordinates)
traincanvas.bind("<Button-1>", show_station)

# 마우스 이벤트로 표시될 텍스트 객체
cursor_text = traincanvas.create_text(10, 10, text="", anchor="nw")

# 입력 창 생성
input_frame = tk.Frame(Lframe_bottom, bg="lightgray", width=30, height=50)
input_frame.pack(pady=10, anchor=N)


start_label = tk.Label(Lframe_bottom, text="출발역 : ", bg="lightgray")
start_label.place(x=25, y=8)

input_entry = tk.Entry(input_frame, width=30)
input_entry.grid(row=0, column=1)
input_entry.bind("<Return>", Enterfunc1)

destination_label = tk.Label(Lframe_bottom, text="도착역 : ", bg="lightgray")
destination_label.place(x=25, y=28)

destination_entry = tk.Entry(input_frame, width=30)
destination_entry.grid(row=1, column=1)
destination_entry.bind("<Return>", Enterfunc2)

label_1 = Label(frame1came1, text="출발 : ", font=("Arial", 15))
label_1.place(x=55, y=80)

label_2 = Label(frame1came1, text="도착 : ", font=("Arial", 15))
label_2.place(x=55, y=110)

timelabel = Label(frame1came1, text="현재시각 : ", font=("Arial", 15))
timelabel.place(x=55, y=140)

start_label = Label(Lframe_top, text="출발지점", font=("Arial", 15), background="lightgray")
start_label.place(x=55, y=195)

end_label = Label(Lframe_top, text="도착지점", font=("Arial", 15), background="lightgray")
end_label.place(x=55, y=225)
 
start_combobox = ttk.Combobox(Lframe_top, height=10, values=start_list)
start_combobox.place(x=160, y=200)
start_combobox.bind("<<ComboboxSelected>>", set_start_station)
start_combobox.bind("<Return>", Enterfunc3)

searchlist1 = Listbox(Lframe_top, selectmode="single", height=10)
searchlist1.place(x=10, y=300)
searchlist1.bind("<Double-Button-1>", doubleclick1)

searchlist2 = Listbox(Lframe_top, selectmode="single", height=10)
searchlist2.place(x=240, y=300)
searchlist2.bind("<Double-Button-1>", doubleclick2)

searchbutton = Button(Lframe_bottom, text="검색", font=("Arial", 15), background="cyan")
searchbutton.place(x=112, y=60)

resetbutton = Button(Lframe_bottom, text="초기화", font=("Arial", 15), command=reset_func)
resetbutton.place(x=212, y=60)

end_combobox = ttk.Combobox(Lframe_top, height=10, values=end_list)
end_combobox.place(x=160, y=230)
end_combobox.bind("<<ComboboxSelected>>", set_end_station)
end_combobox.bind("<Return>", Enterfunc4)

btn1 = Button(frame2came1, text="포노", bd=0, highlightthickness=0, bg="white")
btn1.place(x=1405, y=78)

btn2 = Button(frame2came1, text="범어사", bd=0, highlightthickness=0, bg="white")
btn2.place(x=1328, y=78)

btn3 = Button(frame2came1, text="남산", bd=0, highlightthickness=0, bg="white")
btn3.place(x=1262, y=78)

btn4 = Button(frame2came1, text="두실", bd=0, highlightthickness=0, bg="white")
btn4.place(x=1190, y=78)

btn5 = Button(frame2came1, text="선릉", bd=0, highlightthickness=0, bg="white")
btn5.place(x=1120, y=78)

btn6 = Button(frame2came1, text="장전", bd=0, highlightthickness=0, bg="white")
btn6.place(x=1048, y=78)

btn7 = Button(frame2came1, text="부산대", bd=0, highlightthickness=0, bg="white")
btn7.place(x=971, y=78)

btn8 = Button(frame2came1, text="온천장", bd=0, highlightthickness=0, bg="white")
btn8.place(x=900, y=78)

btn9 = Button(frame2came1, text="명륜", bd=0, highlightthickness=0, bg="white")
btn9.place(x=833, y=78)

btn10 = Button(frame2came1, text="동래", bd=0, highlightthickness=0, bg="white")
btn10.place(x=777, y=230)

btn11 = Button(frame2came1, text="교대", bd=0, highlightthickness=0, bg="white")
btn11.place(x=777, y=370)

btn12 = Button(frame2came1, text="연산", bd=0, highlightthickness=0, bg="white")
btn12.place(x=777, y=490)

btn13 = Button(frame2came1, text="시청", bd=0, highlightthickness=0, bg="white")
btn13.place(x=777, y=582)

btn14 = Button(frame2came1, text="양정", bd=0, highlightthickness=0, bg="white")
btn14.place(x=777, y=666)

btn15 = Button(frame2came1, text="부전", bd=0, highlightthickness=0, bg="white")
btn15.place(x=777, y=750)

btn16 = Button(frame2came1, text="서면", bd=0, highlightthickness=0, bg="white")
btn16.place(x=777, y=817)

btn17 = Button(frame2came1, text="범내골", bd=0, highlightthickness=0, bg="white")
btn17.place(x=762, y=909)

btn18 = Button(frame2came1, text="범일", bd=0, highlightthickness=0, bg="white")
btn18.place(x=777, y=965)

btn19 = Button(frame2came1, text="좌천", bd=0, highlightthickness=0, bg="white")
btn19.place(x=772, y=1040)

btn20 = Button(frame2came1, text="부산진", bd=0, highlightthickness=0, bg="white")
btn20.place(x=727, y=1000)

btn21 = Button(frame2came1, text="초량", bd=0, highlightthickness=0, bg="white")
btn21.place(x=702, y=1040)

btn22 = Button(frame2came1, text="부산역", bd=0, highlightthickness=0, bg="white")
btn22.place(x=662, y=1000)

btn23 = Button(frame2came1, text="중앙", bd=0, highlightthickness=0, bg="white")
btn23.place(x=635, y=1040)

btn24 = Button(frame2came1, text="남포", bd=0, highlightthickness=0, bg="white")
btn24.place(x=600, y=1000)

btn25 = Button(frame2came1, text="자갈치", bd=0, highlightthickness=0, bg="white")
btn25.place(x=562, y=1040)

btn26 = Button(frame2came1, text="토성", bd=0, highlightthickness=0, bg="white")
btn26.place(x=533, y=1000)

btn27 = Button(frame2came1, text="동대신", bd=0, highlightthickness=0, bg="white")
btn27.place(x=495, y=1040)

btn28 = Button(frame2came1, text="서대신", bd=0, highlightthickness=0, bg="white")
btn28.place(x=461, y=1000)

btn29 = Button(frame2came1, text="대티", bd=0, highlightthickness=0, bg="white")
btn29.place(x=433, y=1040)

btn30 = Button(frame2came1, text="과정", bd=0, highlightthickness=0, bg="white")
btn30.place(x=400, y=1000)

btn31 = Button(frame2came1, text="사하", bd=0, highlightthickness=0, bg="white")
btn31.place(x=366, y=1040)

btn32 = Button(frame2came1, text="당리", bd=0, highlightthickness=0, bg="white")
btn32.place(x=333, y=1000)

btn33 = Button(frame2came1, text="하단", bd=0, highlightthickness=0, bg="white")
btn33.place(x=299, y=1040)

btn34 = Button(frame2came1, text="신평", bd=0, highlightthickness=0, bg="white")
btn34.place(x=265, y=1000)

btn35 = Button(frame2came1, text="동매", bd=0, highlightthickness=0, bg="white")
btn35.place(x=231, y=1040)

btn36 = Button(frame2came1, text="장림", bd=0, highlightthickness=0, bg="white")
btn36.place(x=198, y=1000)

btn37 = Button(frame2came1, text="신장림", bd=0, highlightthickness=0, bg="white")
btn37.place(x=160, y=1040)

btn38 = Button(frame2came1, text="낫개", bd=0, highlightthickness=0, bg="white")
btn38.place(x=132, y=1000)

btn39 = Button(frame2came1, text="다대포항", bd=0, highlightthickness=0, bg="white")
btn39.place(x=88, y=1040)

btn40 = Button(frame2came1, text="다대포해수욕장", bd=0, highlightthickness=0, bg="white")
btn40.place(x=39, y=1000)

time()
win.mainloop()