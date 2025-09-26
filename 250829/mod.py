# class 선언
class Bank():
    # class 변수 선언
    total_cost = 0 # 유저가 입금 시 증가, 출금 시 감소
    user_cnt = 0 # class 가 생성이 될 때(유저가 계좌를 생성할 때) 1씩 증가한다

    # 생성자 함수(__init__) 선언
    def __init__(self, _name, _age) :
        self.name = _name
        self.age = _age
        self.cost = 0
        self.log = []
        # 유저의 수(cass변수)를 1 증가시킨다
        Bank.user_cnt += 1
    
    # 입/출금 함수 선언
    def change_cost(self, _type, _cost):
        # _type = 0 이라면 ->입금
        if _type == 0 :
            # self.cost에 _cost 만큼 증가
            # sefl.cost = self.cost + _cost
            self.cost += _cost
            # Bank.total_cost 에 _cost 만큼 증가
            Bank.total_cost += _cost
            # log를 추가 -> dict 형태의 데이터를 추가
            dict_data = {
                "타입" : "입금",
                "금액" : _cost,
                "잔액" : self.cost
            }
            # self.log에 dict_data를 추가 -> self.log는 2차원 데이터 생성
            self.log.append(dict_data)
            print(f"입금완료 : 잔액 {self.cost}입니다") # f-string : 문자와 변수의 조합을 편하게 {변수}를 통해서 구현함.
        elif _type == 1:
            # 출금
            # self.cost가 _cost보다 크거나 같은 경우
            if self.cost >= _cost :
                # 출금이 가능
                # self.cost 를 _cost만큼 감소
                self.cost -= _cost
                # Bank.total_cost 를 _cost만큼 감소
                Bank.total_cost -= _cost
                # dict_data 생성 -> self.log 추가
                dict_data = {
                    "타입" : "출금",
                    "금액" : _cost,
                    "잔액" : self.cost
                }
                self.log.append(dict_data)
                print(f"출금완료 : 잔액 {self.cost}입니다")
            else :
                print("현재 잔액이 부족합니다.")
        else :
            print("_type 값이 잘못되었습니다.")

    def view_log(self, _mode = 9) :
        # 입출금 내역(self.log)을 출력
        # _mode = 9 인 경우 : 전체 내역 출력
        if _mode == 9 :
            # self.log를 기준으로 반복문을 생성
            for log_data in self.log :
                print(log_data)
        # 입금 내역만 출력, mode == 0 이라면
        elif _mode == 0:
            for log_data in self.log :
                # log_data 의 타입 -> dict {"타입" : "xx", "금액" : xxxx, "잔액" : xxxx}
                # log_data에서 key가 '타입'인 value의 값이 '입금' 이라면
                if log_data['타입'] == '입금':
                    print(log_data)
        elif _mode == 1:
            for log_data in self.log :
                if log_data['타입'] == '출금':
                    print(log_data)
        else :
            print("_mode 값이 잘못되었습니다.")
            


         
# User class 선언하고 Bank class의 기능을 상속 받는다
class User(Bank):
    # 클래스 변수 생성
    work_types = {
        'A' : 10000,
        'B' : 20000,
        'C' : 30000
    }
    item_list = {
        "돈까스" : 7000,
        "학식" : 6000,
        "햄버거" : 8000,
        "탕수육" : 19000
    }
    # 생성자 함수 -> 변수들을 저장
    def __init__(self, _name, _age) :
        # _name, _age는 부모클래스의 생성자 함수를 이용하여 저장
        super().__init__(_name,_age)
        # 유저가 구매한 물건의 목록을 생성하여 비어있는 리스트를 대입
        self.items = []
    
    # work함수를 생성
    def work(self, _type):
        # _type에 따라 금액이 지정 -> work_types에 저장
        try:
            # 실행할 코드 작성
            cost = User.work_types[_type]
            # 잔액을 증가시킨다.
            # 부모 클래스에 있는 change_cost() 함수를 호출
            super().change_cost(_type = 0, _cost = cost)
        except : 
            # try 영역에서 있는 코드들이 실행되다가 문제가 발생했을때
            print("work_type에 존재하지 않는 _type 을 입력하였습니다.")
    
    # buy() 함수를 생성
    def buy(self, _type, _cnt = 1):
        # cnt는 물건의 개수(기본값 = 1)
        # _type 에 따라 금액 지정
        # cost = User.item_list[_type] <--- 여기서 선언하지 않은 이유? try 안에 포함시키려고
        try :
            # item_list에 있는 물건의 금액을 불러온다
            cost = User.item_list[_type] * _cnt
            # 현재 잔액과 cost를 비교
            if self.cost >= cost :
                # 구매가 성공하는 조건
                # 부모 클래스에서 change_cost() 함수 호출 (_type =1)
                super().change_cost(_type =1 , _cost = cost)
                # self.items에 구매한 물건(개수)을 추가한다
                self.items.append(
                    f"{_type} x {_cnt}"
                )
            else :
                # 구매가 실패하는 조건
                print('구매 실패 : 잔액이 부족합니다.')
        
        except :
            print('구매 실패 : 구매하려는 물건에 정보가 존재하지 않습니다.')


    # 유저의 정보를 출력해주는 함수 생성
    def user_info(self):
        print(f""" 
            이름 : {self.name}
            나이 : {self.age}
            잔액 : {self.cost}
            구매한 물건의 목록 : {self.items}
        """)
    # 함수 생성 -> 메개변수 3개 (_select, _key, _value)
    def add_type(self, _select, _key, _value):
        self.select = _select
        self.key = _key
        self.value = _value
        # _select가 "work" 라면
        if _select == "work":
            # 클래스변수 work_type에 _key : _value 추가
            # User.work_type = [ _key : _value] -=---> 내 오답
            User.work_types[_key] = _value
        # _select "item" 이면
        elif _select == "item":
            # 클래스변수 item_list에 _key : _value 추가
            # User.item_list = [ _key : _value]  ----> 마찬가지
            User.item_list[_key] = _value
        # 그 외의 경우
        else : 
            # "_select에는 work와 item 만 기입이 가능합니다" 메세지 출력
            print("_select 에는 work 와 item 만 기입이 가능합니다")



test_vari = "모듈 안에 있는 텍스트"

def func_1(_a,_b):
    return _a+_b