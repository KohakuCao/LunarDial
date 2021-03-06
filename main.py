#月時計 ~Lunar Dial~  日历
#By: Kohaku Cao
#2022-06, For BUAA
#                             $$$$$$$$
#                           $$$$$$$$$$$$$
#                          $$$$$ $$$$$$$$
#                            $$$ $$$$$$
#                             $$ $$$$$$
#                             $$ $$$$$$
#                             $$ $$$$$$
#                           $$$$ $$$$$$
#                   $$$%&8%%%%$$ $$$$$$$$$$$$$
#              $$8%#kqa%M%$$@@@W $$$$$$$$$$$$$$
#           $$8#bh0kOfUpzW$$#WB@ $$$$$$$$$$$$$
#         $$@B*oZMkW@@       k$$ $$$$$
#       $$%Mho*  W%B$$@8    Qb@$ $$$$$         $$$$$$$$$$                  $$$          $$$$                 $$
#     $$@&om{      %8@@@$   $p$$ $$$$$     $$$$$$$$$$$$$$$$$$          $$$$$$$$$$$$$$$$$$$$$$$$$$           $$$$        $$$$
#    $B&aa     $    tkQ       $$ $$$$$     $$$$   $$$$  $$$$$          $$$$   $$$$$$$$$$$$$$$$$$$        $$$$$$$$$$     $$$$
#   $$Wh8B%$$$ %WW$           $$ $$$$$     $$$$  $$$$$  $$$$$          $$$$   $$$$      $$$$             $$$$$$$$$$     $$$$
#  $$MMa%@@$@8@@WWB$$@B       $$ $$$$$     $$$$  $$$$$  $$$$$          $$$$   $$$$$$$$$$$$$$$$$$$           $$$$   $$$$$$$$$$$$$$
#  $%ab      kda   @$$$B@     $$ $$$$$     $$$$         $$$$$          $$$$$$$$$$$$$$$$$$$$$$$$$$           $$$$   $$$$$$$$$$$$$$
# $$##               $B$@B8W  $$ $$$$$     $$$$  $$$$$  $$$$$          $$$$$$$$$$$$$$$$$$$$$$$$$$           $$$$        $$$$
# $Bba      n            %B%B$@$ $$$$$     $$$$  $$$$$  $$$$$          $$$$   $$$$$$$$$$$$$$$$$$$           $$$$        $$$$
# $$pk8%@@@BBQ              8@$$ $$$$$     $$$$         $$$$$          $$$$   $$$$   $$$$  $$$$          $$$$$$$$$$     $$$$
# $$o%BB$$@@Ba                $$ $$$$$     $$$$         $$$$$          $$$$$$$$$$$   $$$$  $$$$          $$$$  $$$$     $$$$
# $@h*$$$$$$$              $B@@$ $$$$$     $$$$         $$$$$          $$$$$$$$$$$   $$$$$$$$$$          $$$$$$$$$$     $$$$
# $$&b      $@W            $$$@$ $$$$$                                                $$$$$$$$$          $$$$$$$$$$     $$$$
#  $$hb$$@@@@@B@          *@$$$$ $$$$$
#   $@a#@$@@@@@%8        $$@  $$ $$$$$
#    $$&WBBBB@@#$  $$    $@   $$ $$$$$
#     $$%k&@$     B@@%kk      $$ $$$$$
#      $$@%*m$  $@$@@$%*     $B$ $$$$$
#        $$@@Bk#B@@B@$8      $$$ $$$$$
#             $$$$$$88#W*abk#@$$ $$$$$
#                 $$$$$$@B%%8B$$ $$$$$
#                       $$$$$$$$ $$$$$
#                             $$$$$$$$
#                              $$$$$$$
#                               $$$$
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from qt_material import *

import Home
if __name__ == '__main__':
    sys.argv.append("--disable-web-security")  #关闭Web安全限制，以免无法调用本地Web文件
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)  #高清优化
    app = QApplication(sys.argv)
    Home.init()  #把HomeController实例化到Home.py
    apply_stylesheet(app, theme='dark_blue.xml')
    stylesheet = app.styleSheet()
    with open("Resources/qss/Main.qss") as file:
        app.setStyleSheet(stylesheet + file.read())
    Home.home.show()
    sys.exit(app.exec())