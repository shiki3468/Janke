import random
import sys

class Janken(object):
    def __init__(self,set = 0):
        self.set = 0

    def kakegoe(self):
        print("最初はグー、ジャン・ケン・")
        return input("グー ･･･ G, パー ･･･ P ,チョキ ･･･ C : ")
    
    def way_com(self):
        return (int)(random.randint(1,3))

    def aiko(self):
        print("あいこです。\nジャン・ケン・")
        x = input("グー ･･･ G, パー ･･･ P ,チョキ ･･･ C : ")
        return x
    
    def Judge(self,way,com):
        while True:
            if way == "G" or way == "g" :
                if com == 1:
                    print("コンピュータ: グー")
                    way = self.aiko()
                    com = self.way_com()
                elif com == 2:
                    print("コンピュータ: パー")
                    print("あなたの負けです")
                    break
                elif com == 3:
                    print("コンピュータ: チョキ")
                    print("あなたの勝ちです")
                    break
            elif way == "P" or "p":
                if com == 1:
                    print("コンピュータ: グー")
                    print("あなたの勝ちです")
                    break
                elif com == 2:
                    print("コンピュータ: パー")
                    way = self.aiko()
                    com = self.way_com()
                elif com == 3:
                    print("コンピュータ: チョキ")
                    print("あなたの負けです")
                    break
            elif way == "C" or "c":
                if com == 1:
                    print("コンピュータ: グー")
                    print("あなたの負けです")
                    break
                elif com == 2:
                    print("コンピュータ: パー")
                    print("あなたの勝ちです")
                    break
                elif com == 3:
                    print("コンピュータ: チョキ")
                    way = self.aiko()
                    com = self.way_com()
            else:
                print('想定していない文字が入力されましたので処理を終了します。')
                sys.exit()
            

class test:
    jan = Janken()
    x = jan.kakegoe()
    y = jan.way_com()
    jan.Judge(x,y)