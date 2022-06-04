from tkinter import *
from tkinter import messagebox
from numpy import NaN
from pandas import *
from datetime import date
from numpy import *

class user_dataframe:
    #파일 불러옴
    def __init__(self):
        self.data = DataFrame(columns=['USER_NAME', 'USER_BIRTH', 'USER_PHONE', 'USER_SEX', 'USER_MAIL',
                                       'USER_IMAGE','USER_RENT_CNT', 'USER_QUIT_DATE', 'USER_RENT_ALW', 'USER_WARN'])
           

    #일반 회원 조회
    def now_list(self):
        self.show = self.data[self.data['USER_QUIT_DATE'].isnull()]
        intext = list()
        for i in range(len(self.show)):
            intext.append([self.show.iloc[i]['USER_NAME'], self.show.iloc[i]['USER_BIRTH'], '0'+self.show.iloc[i]['USER_PHONE'], '  '])
        return intext
            
    
    #탈퇴회원 조회
    def re_list(self):
        self.show_re = self.data[self.data['USER_QUIT_DATE'].notnull()]
        intext = list()
        for i in range(len(self.show_re)):
            intext.append([self.show_re.iloc[i]['USER_NAME'], self.show_re.iloc[i]['USER_BIRTH'], '0'+self.show_re.iloc[i]['USER_PHONE'], '탈퇴'])
        return intext
    
    #모든회원 조회
    def all_list(self):
        intext = list()
        for i in range(len(self.data)):
            if notna(self.data.iloc[i]['USER_QUIT_DATE']):
                remove = "탈퇴"
            else:
                remove = '회원'
            intext.append([self.data.iloc[i]['USER_NAME'], self.data.iloc[i]['USER_BIRTH'], '0'+self.data.iloc[i]['USER_PHONE'], remove])
        return intext
    
    #검색을 통해 특정 회원만 목록에 표기
    def searchdata(self, searchvalue):
        if not((self.data['USER_PHONE'].str.contains(searchvalue)).any()) and not((self.data['USER_NAME'].str.contains(searchvalue)).any()):
            errshow = messagebox.showerror('ERR','\n등록되어 있지 않은 회원입니다.')
        else:
            self.sch_data = self.data.loc[self.data['USER_PHONE'].str.contains(searchvalue) | self.data['USER_NAME'].str.contains(searchvalue), ['USER_NAME', 'USER_BIRTH', 'USER_PHONE', 'USER_QUIT_DATE']]
            intext = []
            for i in range(len(self.sch_data)):
                if notna(self.sch_data.iloc[i]['USER_QUIT_DATE']):
                    remove = "탈퇴"
                else:
                    remove = '회원'
                intext.append([self.sch_data.iloc[i]['USER_NAME'], self.sch_data.iloc[i]['USER_BIRTH'], '0'+self.sch_data.iloc[i]['USER_PHONE'], remove])
            return intext
                
    #회원 상세 정보(탈퇴회원, 회원 포함)      
    def userinfo(self, inwindow, phone):
        #showindex = self.data.index[self.data['USER_PHONE'].isin([phone])].tolist()
        self.info = self.data.loc[self.data['USER_PHONE'].str.contains(phone)]
        if (self.info.iloc[0]['USER_SEX']):
            sex = '남'
        else:
            sex = '여'
        if((self.info['USER_IMAGE'].notnull()).any()):
            IMAGE = PhotoImage(file = self.info.iloc[0]['USER_IMAGE'])
        else:
            IMAGE = None
        #탈퇴회원
        if((self.info['USER_QUIT_DATE'].notnull()).any()):
            removeuser = '탈퇴회원'
            showit = [self.info.iloc[0]['USER_NAME'], self.info.iloc[0]['USER_BIRTH'], self.info.iloc[0]['USER_PHONE'], sex, self.info.iloc[0]['USER_MAIL'], IMAGE, removeuser]
            #해당 부분은 UI에 적용할 떄 목록UI형태에 맞추어 변형할 예정
            for i in range(7):
                if(showit[i] == IMAGE):
                    label = Label(inwindow, image = showit[i])
                    label.pack()
                else:
                    label = Label(inwindow, text = showit[i])
                    label.pack()
        #비탈퇴회원
        else:
            showit = [self.info.iloc[0]['USER_NAME'], self.info.iloc[0]['USER_BIRTH'], self.info.iloc[0]['USER_PHONE'], sex, self.info.iloc[0]['USER_MAIL'], IMAGE]
            #해당 부분은 UI에 적용할 떄 목록UI형태에 맞추어 변형할 예정
            for i in range(6):
                if(showit[i] == IMAGE):
                    label = Label(inwindow, image = showit[i])
                    label.pack()
                else:
                    label = Label(inwindow, text = showit[i])
                    label.pack()
    
    
                
                
    #회원목록에서 선택 수정할 경우의 함수 (수정할 회원의 USER_PHONE 값을 넘겨받아 진행)
    def modidata(self, phone):
        if (self.data['USER_PHONE']!=phone).all():
            errshow = messagebox.showerror('ERR','\n등록되어 있지 않은 회원입니다.')
        else:
            #입력받은 수정할 데이터
            name = None
            birth = None
            phonenum = None
            sex  = None
            mail = None
            image = None
            #UI를 보고 입력을 어떻게 받을건지 수정할 예정(전화번호의 010은 외국에서 개통한게 아닌이상 동일하니 따로 표기해서 받을 생각 [010][   ][   ]이런 느낌)
            modivalue = [name, birth, phonenum, sex, mail, image]
            column_name = ['USER_NAME', 'USER_BIRTH', 'USER_PHONE', 'USER_SEX', 'USER_MAIL', 'USER_IMAGE']
            for value, column in zip(modivalue, column_name):
                if value == None:
                    continue
                else:
                    if (value == phonenum):
                        if (self.data['USER_PHONE'] == phonenum).any():
                            errshow = messagebox.showerror('ERR','\n등록되어 있는 회원입니다.')
                        else:
                            self.data.loc[self.data['USER_PHONE'].str.contains(phone), (column)] = (value)
                    else:
                        self.data.loc[self.data['USER_PHONE'].str.contains(phone), (column)] = (value)
    
    #회원 등록 함수        
    def add_data(self):
        #입력받은 추가할 데이터
        name = None
        birth = None
        phonenum = None
        sex  = None
        mail = None
        image = None
        #수정과 마찬가지로 입력받은 값을 바탕으로 등록진행하도록 수정 예정
        adduser = DataFrame({'USER_NAME' : [name], 'USER_BIRTH': [birth], 'USER_PHONE' : [phonenum], 'USER_SEX' : [sex], 'USER_MAIL' : [mail], 'USER_IMAGE' : [image],
                             'USER_RENT_CNT': 0})
        if (self.data['USER_PHONE'] == phonenum).any():
            errshow = messagebox.showerror('ERR','\n등록되어 있는 회원입니다.')
        else:
            self.data = concat([self.data, adduser])
            self.data.sort_values('USER_NAME')
        
        
    #선택한 회원의 탈퇴시 실행할 함수        
    def removedata(self, phone):
        if(self.data['USER_PHONE']==phone).any():
            showmessage = messagebox.askquestion('탈퇴', '\n정말로 탈퇴 하시겠습니까?')
            if showmessage == 'yes':
                removeindex = self.data.index[self.data['USER_PHONE'].isin([phone])].tolist()
                if(self.data.loc[removeindex[0]]['USER_RENT_CNT'] != 0):
                    show = messagebox.showinfo('탈퇴','\n대여한 도서가 있는 회원입니다.')
                else:
                    self.data.loc[self.data['USER_PHONE'].str.contains(phone), ('USER_QUIT_DATE')] = (date.today())
                    show = messagebox.showinfo('탈퇴','\n탈퇴 되었습니다.')
            else:
                show = messagebox.showinfo('탈퇴','\n탈퇴 취소 되었습니다.')
     #탈퇴 회원 복원           
    def resetremove(self, phone):
        if((self.data.loc[self.data['USER_PHONE'].str.contains(phone), ('USER_QUIT_DATE')].notnull()).any()):
            self.data.loc[self.data['USER_PHONE'].str.contains(phone), ('USER_QUIT_DATE')] = None
    
        
    #csv 불러오기        
    def readcsv(self):
        self.data = read_csv('user.csv', dtype={"USER_PHONE": str, "USER_SEX": bool, 'USER_RENT_CNT' : int}, encoding='cp949')
        self.data.drop(['Unnamed: 0'], axis = 1, inplace = True)
        self.data['USER_QUIT_DATE'] = to_datetime(self.data['USER_QUIT_DATE'])
        self.data.sort_values('USER_NAME')
    
    #CSV 저장
    def tocsv(self):
        self.data.to_csv('user.csv', encoding='cp949')
