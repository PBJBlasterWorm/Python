import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image



win = tk.Tk()
win.geometry('1900x1100+0+0')
win.title("부산 노선도")

frame1came1 = tk.Frame(win, height=1100 , width=400 ,background='lightgray')
frame1came1.pack(side="left")   
frame2came1 = tk.Frame(win, height=1100, width=1500, background='white')
frame2came1.pack(side="right")

traincanvas = tk.Canvas(frame2came1,width=1485,height=1080,relief='solid',bd=0,background='white')
traincanvas.place(x=5,y=10)   #노선도 그리는 칸

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

subway_lines_Donhae = {
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

subway_lines_BusanGimhae = {
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
            canvas.create_line(start_station[0], start_station[1], end_station[0], end_station[1], fill='#ff0000', width=3)

    # 지하철 역 표시
    for station, (x, y) in subway_stations_1.items():
        canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='#000000')
        
    for station, (x, y) in subway_stations_2.items():
        canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='#000000')

# 지하철 노선도 그리기
draw_subway_map(traincanvas)

# 마우스 이벤트 바인딩
traincanvas.bind("<Motion>", show_coordinates)

# 마우스 이벤트로 표시될 텍스트 객체
cursor_text = traincanvas.create_text(10, 10, text="", anchor="nw")

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

win.mainloop()