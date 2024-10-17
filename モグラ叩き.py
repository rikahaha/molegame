#72344146蒋理嘉
#モグラ叩きのゲームです。

import pyxel

class Mole:
    def __init__(self,):
        self.is_hidden = True
        self.i = 30
        #早くなる時間設定
        self.frame_count_threshold1 = 30 * 30 
        self.frame_count_threshold2 = 30 * 45
    def update(self):
        if pyxel.frame_count < self.frame_count_threshold1:
            # 最初 30 秒モグラ1秒一個現れる
            self.i = 30
        elif pyxel.frame_count > self.frame_count_threshold1 and pyxel.frame_count < self.frame_count_threshold2:
            # 30秒後頻度早くなる
            self.i = 15
        else:
            #一番早い速度
            self.i = 5
        if pyxel.frame_count % self.i == 0:
            self.is_hidden = not self.is_hidden
            if not self.is_hidden:
                #x、ｙは穴の番号
                x = pyxel.rndi(0,4)
                y = pyxel.rndi(0,4)
                #座標
                self.molex=30+(x) * 30
                self.moley=45+(y) * 30
                #色はランダム生成
                self.c = pyxel.rndi(8,10)

    def draw(self):
        #穴を描く
        for i in range (0,5):
            for b in range (0,5):
                pyxel.circ(35+(i) * 30,50+(b) * 30,10,7)
        #モグラを描く
        if not self.is_hidden:            
            pyxel.rect(self.molex, self.moley, 11, 11, self.c)
            pyxel.circ(self.molex+5, self.moley, 5, self.c)
            pyxel.rect(self.molex + 2, self.moley, 2, 2, 0)
            pyxel.rect(self.molex + 8, self.moley, 2, 2, 0)
            pyxel.rect(self.molex + 5, self.moley+4, 2, 2, 7)

class Hammer:
    def __init__(self):
        self.is_hitting = False

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            #マウスを左クリックするとき,叩いているハンマーの場所を記録します
            self.is_hitting = True
            self.x = pyxel.mouse_x
            self.y = pyxel.mouse_y
            #マウスをクリックしたところとモグラ表れた場所と比べます
            if (self.is_hitting and not Mole.self.is_hidden and
                self.x > Mole.molex and self.x < Mole.molex + 10 and
                self.y > Mole.moley and self.y < Mole.moley + 10):        
                Score.update(Mole.c)
                Mole.self.is_hidden = True
            else:
                #タイムアップ
                self.Gameover=True

        else:
            self.is_hitting = False
                    

    def draw(self):
        if self.is_hitting:
            #叩いているところに赤い線を引く
            pyxel.line(self.x, self.y, self.x, self.y - 10, 8)

class Score:
    def __init__(self):
        self.score = 0
    def update(self, mole_color):
        if mole_color == 8:
            self.score += 1
        elif mole_color == 9:
            self.score += 2
        elif mole_color == 10:
            self.score += 3

class App:
    def __init__(self):
        pyxel.init(200, 200)
        pyxel.mouse(True)
        self.mole = Mole()
        self.hammer = Hammer()
        self.s = Score()
        self.time_remaining = 60* 30
        self.Gameover = False
        self.mouseleft = False
        pyxel.run(self.update, self.draw)

        
        

    def update(self):
        self.mole.update()
        self.hammer.update()
        #時間内の時
        if self.time_remaining > 0:
            self.time_remaining -= 1


    def draw(self):

        if self.Gameover == False:
            #背景を描く
            pyxel.cls(0)
            pyxel.line(20,35,20,185,7)
            pyxel.line(20,35,170,35,7)
            pyxel.line(170,185,20,185,7)
            pyxel.line(170,185,170,35,7)
            pyxel.text(10, 10, f'Score: {self.s.score}', 7)
            pyxel.text(120, 10, f'Time: {self.time_remaining // 30}', 7)
            self.mole.draw()
            self.hammer.draw()
        else:
            #ゲームオーバーの時、画面中央にGAME OVERを表す。
            pyxel.cls(0)
            pyxel.text(80, 100, 'GAME OVER', 7)
            pyxel.text(80, 120, f'Score: {self.s.score}', 7)

# アプリを実行
App()

