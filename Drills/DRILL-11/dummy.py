# class Star: # 클래스 역할: 객체 생성 용도x 관련 있는 변수를 group 으로 만드는 것
#     x = 100
#     def change():
#         x = 200
#         print('x is',x)
#
# print(Star.x) # Star 클래스 x 는 클래스 변수
# Star.change() # 클래스 함수 호출
#
# star = Star() # 객체 생성용이 아니여도 객체는 만들어진다.
# star.change()

# class Player:
#     def __init__(self):
#         self.x = 100
#
#     def where(self):
#         print(self.x)
#
# player = Player()
# player.where()
#
# # Player.where() # 클래스의 함수 호출
# Player.where(player)
#
# player.where() # 객체 함수 호출 == Player.where(player)

table = {
    'SLEEP' : {'HIT':'WAKE'},
    'WAKE' : {'TIMER10':'SLEEP'}
}

cur_state = 'SLEEP'
event = 'HIT'
next_state = table[cur_state][event]
print(table[cur_state]['HIT'])
print(table['WAKE']['TIMER10'])
