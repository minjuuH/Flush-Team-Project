from email import message
from tkinter import *
from tkinter import messagebox
from pandas import *
from datetime import date
import User_View as uv
from UI_Class import *
from numpy import *

class user_dataframe:
    #파일 불러옴
    def __init__(self):
        self.data = DataFrame(columns=['USER_NAME', 'USER_BIRTH', 'USER_PHONE', 'USER_SEX', 'USER_MAIL',
                                       'USER_IMAGE','USER_RENT_CNT', 'USER_QUIT_DATE', 'USER_RENT_ALW', 'USER_WARN'])
           

    #일반 회원 조회
    def now_list(self, want = None):
        self.show = self.data[self.data['USER_QUIT_DATE'].isnull()]
        intext = list()
        info = list()
        for i in range(len(self.show)):
            info.append([self.show.iloc[i]['USER_NAME'], self.show.iloc[i]['USER_BIRTH'], self.show.iloc[i]['USER_PHONE'], '  ', False])
            intext.append(self.show.iloc[i]['USER_NAME']+'\t\t'+self.show.iloc[i]['USER_BIRTH']+'\t\t'+'0'+self.show.iloc[i]['USER_PHONE'])
        if want == 1:
            return intext
        else:
            return info
            
    
    #탈퇴회원 조회
    def re_list(self, want = None):
        self.show_re = self.data[self.data['USER_QUIT_DATE'].notnull()]
        intext = list()
        info = list()
        for i in range(len(self.show_re)):
            info.append([self.show_re.iloc[i]['USER_NAME'], self.show_re.iloc[i]['USER_BIRTH'], self.show_re.iloc[i]['USER_PHONE'], '탈퇴', True])
            intext.append(self.show_re.iloc[i]['USER_NAME']+'\t\t'+self.show_re.iloc[i]['USER_BIRTH']+'\t\t'+'0'+self.show_re.iloc[i]['USER_PHONE'])
        if want == 1:
            return intext
        else:
            return info
    
    #모든회원 조회
    def all_list(self):
        intext = list()
        for i in range(len(self.data)):
            if notna(self.data.iloc[i]['USER_QUIT_DATE']):
                remove = "탈퇴"
                choice = True
            else:
                remove = '회원'
                choice = False
            intext.append([self.data.iloc[i]['USER_NAME'], self.data.iloc[i]['USER_BIRTH'], self.data.iloc[i]['USER_PHONE'], remove, choice])
        return intext
    
    #검색을 통해 특정 회원만 목록에 표기
    def searchdata(self, searchvalue, want = None):
        if not((self.data['USER_PHONE'].str.contains(searchvalue)).any()) and not((self.data['USER_NAME'].str.contains(searchvalue)).any()):
            errshow = messagebox.showerror('ERR','\n등록되어 있지 않은 회원입니다.')
        else:
            self.sch_data = self.data.loc[self.data['USER_PHONE'].str.contains(searchvalue) | self.data['USER_NAME'].str.contains(searchvalue), ['USER_NAME', 'USER_BIRTH', 'USER_PHONE', 'USER_QUIT_DATE']]
            intext = []
            info = []
            for i in range(len(self.sch_data)):
                if notna(self.sch_data.iloc[i]['USER_QUIT_DATE']):
                    remove = "탈퇴"
                    choice = True
                else:
                    remove = '회원'
                    choice = False
                info.append([self.sch_data.iloc[i]['USER_NAME'], self.sch_data.iloc[i]['USER_BIRTH'], self.sch_data.iloc[i]['USER_PHONE'], remove, choice])
                intext.append(self.sch_data.iloc[i]['USER_NAME']+'\t\t'+self.sch_data.iloc[i]['USER_BIRTH']+'\t\t'+'0'+self.sch_data.iloc[i]['USER_PHONE'])
            if want == 1:
                return intext
            else:
                return info
                
    #회원 상세 정보(탈퇴회원, 회원 포함)      
    def userinfo(self, phone):
        #showindex = self.data.index[self.data['USER_PHONE'].isin([phone])].tolist()
        self.info = self.data.loc[self.data['USER_PHONE'].str.contains(phone)]
        if (self.info.iloc[0]['USER_SEX']):
            sex = '남'
        else:
            sex = '여'
        if(isna(self.info.iloc[0]['USER_IMAGE'])):
            IMAGE = None
        else:
            IMAGE = self.info.iloc[0]['USER_IMAGE']
        #탈퇴회원      
        showit = [self.info.iloc[0]['USER_NAME'], self.info.iloc[0]['USER_BIRTH'], self.info.iloc[0]['USER_PHONE'], sex, self.info.iloc[0]['USER_MAIL'], IMAGE]
        return showit
    
    def modiuserinfo(self, phone):
        self.info = self.data.loc[self.data['USER_PHONE'].str.contains(phone)]
        if(isna(self.info.iloc[0]['USER_IMAGE'])):
            IMAGE = None
        else:
            IMAGE = self.info.iloc[0]['USER_IMAGE']
        showit = [self.info.iloc[0]['USER_NAME'], self.info.iloc[0]['USER_BIRTH'], self.info.iloc[0]['USER_PHONE'], self.info.iloc[0]['USER_SEX'], self.info.iloc[0]['USER_MAIL'], IMAGE]
        return showit
    
    def checkphone(self, phonenum):
        if (self.data['USER_PHONE'] == phonenum).any():
            messagebox.showerror('중복확인','\n중복되는 전화번호 입니다.')
        else:
            messagebox.showinfo('중복확인', '\n중복되지 않습니다.')
                
    #회원목록에서 선택 수정할 경우의 함수 (수정할 회원의 USER_PHONE 값을 넘겨받아 진행)
    def modidata(self, phone, list):
        if (self.data['USER_PHONE']!=phone).all():
            messagebox.showerror('ERR','\n등록되어 있지 않은 회원입니다.')
        
        if(len(list[2]) != 10):
            messagebox.showerror('ERR', '\n알맞은 전화번호\n양식이 아닙니다.')
        else:
            #입력받은 수정할 데이터
            name = list[0]
            birth = list[1]
            phonenum = list[2]
            sex  = list[3]
            mail = list[4]
            image = list[5]
            if image == None:
                image = '사진등록'
            modivalue = [name, birth, phonenum, sex, mail, image]
            column_name = ['USER_NAME', 'USER_BIRTH', 'USER_PHONE', 'USER_SEX', 'USER_MAIL', 'USER_IMAGE']
            if (self.data['USER_PHONE'] == phonenum).any():
                if(phone == phonenum):
                    ask = messagebox.askquestion('수정', '\n정말 수정하시겠습니까?')
                    if ask == 'yes':
                        for value, column in zip(modivalue, column_name):
                            if value == None:
                                continue
                            self.data.loc[self.data['USER_PHONE'].str.contains(phone), (column)] = (value)
                        messagebox.showinfo('수정', '\n수정 완료 되었습니다.')
                        return True
                    else:
                        messagebox.showinfo('수정', '\n수정 취소 되었습니다.')
                else:
                    messagebox.showerror('ERR','\n등록되어 있는 회원입니다.')
            else:
                ask = messagebox.askquestion('수정', '\n정말 수정하시겠습니까?')
                if ask == 'yes':
                    for value, column in zip(modivalue, column_name):
                        if value == None:
                            continue
                        self.data.loc[self.data['USER_PHONE'].str.contains(phone), (column)] = (value)
                    messagebox.showinfo('수정', '\n수정 완료 되었습니다.')
                    return True
                else:
                    messagebox.showinfo('수정', '\n수정 취소 되었습니다.')
                    
    
    #회원 등록 함수        
    def add_data(self, list):
        #입력받은 추가할 데이터
        name = list[0]
        birth = list[1]
        phonenum = list[2]
        sex  = list[3]
        mail = list[4]
        image = list[5]
        if image == '':
            image = '사진등록'
        #수정과 마찬가지로 입력받은 값을 바탕으로 등록진행하도록 수정 예정
        adduser = DataFrame({'USER_NAME' : [name], 'USER_BIRTH': [birth], 'USER_PHONE' : [phonenum], 'USER_SEX' : [sex], 'USER_MAIL' : [mail], 'USER_IMAGE' : [image],
                             'USER_RENT_CNT': 0})
        if (self.data['USER_PHONE'] == phonenum).any():
            errshow = messagebox.showerror('ERR','\n등록되어 있는 회원입니다.')
        if(len(list[2]) != 10):
            messagebox.showerror('ERR', '\n알맞은 전화번호\n양식이 아닙니다.')
        else:
            ask = messagebox.askquestion('등록', '\n정말 등록하시겠습니까?')
            if ask == 'yes':
                self.data = concat([self.data, adduser])
                self.data.sort_values('USER_NAME')
                messagebox.showinfo('등록', '\n등록이 완료 되었습니다.')
                return True
            else:
                messagebox.showinfo('등록', '\n등록 취소 되었습니다.')
        
        
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
                    return True
            else:
                show = messagebox.showinfo('탈퇴','\n탈퇴 취소 되었습니다.')
     #탈퇴 회원 복원           
    def resetremove(self, phone):
        #if((self.data.loc[self.data['USER_PHONE'].str.contains(phone), ('USER_QUIT_DATE')].notnull()).any()):
        #    self.data.loc[self.data['USER_PHONE'].str.contains(phone), ('USER_QUIT_DATE')] = None
        ask = messagebox.askquestion('복구', '\n복구 하시겠습니까?')
        if ask == 'yes':
            self.data.loc[self.data['USER_PHONE'].str.contains(phone), ('USER_QUIT_DATE')] = None
            messagebox.showinfo('복구', '\n복구 되었습니다.')
            return True
        else:
            messagebox.showinfo('복구', '\n복구 취소 되었습니다.')
        
    
        
    #csv 불러오기        
    def readcsv(self):
        self.data = read_csv('user.csv', dtype={"USER_PHONE": str, "USER_SEX": bool,'USER_RENT_CNT' : int}, encoding='cp949')
        self.data.drop(['Unnamed: 0'], axis = 1, inplace = True)
        self.data['USER_QUIT_DATE'] = to_datetime(self.data['USER_QUIT_DATE'])
        self.data = self.data.sort_values('USER_NAME')
    
    #CSV 저장
    def tocsv(self):
        self.data.to_csv('user.csv', encoding='cp949')
'''
a = user_dataframe()
a.readcsv()
b = a.now_list(1)
print(b[0][-10:])
'''