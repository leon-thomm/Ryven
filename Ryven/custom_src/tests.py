import sys
import types
import inspect
from optparse import OptionParser
import random
import math
import pickle
import os
from pyowm import OWM

from PySide2.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QPlainTextEdit, QGraphicsView, QGraphicsScene, QGraphicsProxyWidget, QAction, QMenu
from PySide2.QtGui import QFont, QColor, QImage, QPainter, QPen, QBrush
from PySide2.QtCore import Qt, QRectF


from PySide2.QtWidgets import QGraphicsItem
import pickle

from custom_src.retain import retain


class Test(QGraphicsItem):
    def __init__(self):
        super(Test, self).__init__()
        self.a = 1
        self.fancy_widget = QWidget()

    def __setstate__(self, state):
        self.a = state["a"]
        self.w = self.fancy_widget

    def __getstate__(self):
        return {'a':self.a,
                'fancy widget':self.fancy_widget}

class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()

        self.a = 42


class MyView(QGraphicsView):
    def __init__(self):
        super(MyView, self).__init__()

        self.setScene(QGraphicsScene())
        self.scene().setSceneRect(300, 300)

        self.scene().addItem(Test())




# class CodeWidget(QWidget):
#     def __init__(self):
#         super(CodeWidget, self).__init__()
#
#         # UI
#         self.setLayout(QVBoxLayout())
#
#         self.add_new_script()
#
#     def add_new_script(self):
#         code_text_edit = QPlainTextEdit('test code')
#         code_text_edit.setStyleSheet('background: black; color: grey;')
#         print('before: ', self.height())
#         self.layout().addWidget(code_text_edit)
#         print('after: ', self.height())
#
#     def mousePressEvent(self, event):
#         print('mouse pressed! adding new script')
#         self.add_new_script()
#
#
# class MyView(QGraphicsView):
#     def __init__(self):
#         super(MyView, self).__init__()
#
#
#         # create UI
#         scene = QGraphicsScene(self)
#         scene.setSceneRect(0, 0, 500, 500)
#
#         self.setScene(scene)
#
#         self.code_proxy = QGraphicsProxyWidget()
#         self.code_widget = CodeWidget()
#         self.code_proxy.setWidget(self.code_widget)
#
#         scene.addItem(self.code_proxy)
#         self.code_proxy.setPos(50, 50)
#
#
#
#
# class MyAction(QAction):
#     def __init__(self, text, menu):
#         super(MyAction, self).__init__(text=text, parent=menu)
#
#
# class MyWidget(QWidget):
#     def __init__(self):
#         super(MyWidget, self).__init__()
#
#     def contextMenuEvent(self, event):
#         menu = QMenu()
#         menu.addAction(MyAction('action 1', menu))
#         menu.addAction(MyAction('action 2', menu))
#         menu.exec_(event.globalPos())


# class A:
#     def __init__(self):
#         pass
#
#     def __call__(self, *args, **kwargs):
#         pass
#
# class B:
#     def __init__(self):
#         self.a = A()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # w = MyView()
        w = QWidget()

        self.setCentralWidget(w)




def replace_in_folder(path):
    print(path)
    for (dirpath, dirnames, filenames) in os.walk(path):
        print('filenames:', filenames)
        for f_name in filenames:
            print(path+'/'+f_name)
            try:
                f = open(path+'/'+f_name, 'r')
                content = f.read()
                f.close()
                content = content.replace('''if configuration:\n            self.set_data(configuration['state data'])''',
                                          'self.initialized()')
                f = open(path+'/'+f_name,'w')
                f.write(content)
                f.close()
            except Exception as e:
                print(e)
        for d in dirnames:
            replace_in_folder(path+'/'+d)


# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def meow(self):
#         print('meow!')
#
#     def say_name(self):
#         print(self.name)
#         self.meow()


class A:
    def foo(self):
        print('A')

class B:
    def foo(self):
        print('B')

class C:
    def __init__(self, a):
        self.func = Retain(a.foo)

    def do_something(self):
        self.func()

class Retain:
    def __init__(self, func):
        self.func_name = func.__name__
        self.func = retain(func)

    def __call__(self, *args, **kwargs):
        self.func(*args, **kwargs)


if __name__ == '__main__':

    a = A()
    c = C(a)

    method_name = 'foo'  # it has to be dynamic
    new_method = getattr(B, method_name)
    setattr(a, method_name, types.MethodType(new_method, a))

    c.do_something()  # still prints A, I want it to print B now

    # mymodule = types.ModuleType('temporary')
    # exec(class_code, mymodule.__dict__)
    # new_cat_class = getattr(mymodule, 'Cat')
    #
    # # members = inspect.getmembers(OptionParser, predicate=inspect.isfunction)
    # members = [func for func in dir(new_cat_class) if callable(getattr(new_cat_class, func)) and not func.startswith("__")]
    # for m in members:
    #     # print(type(m))
    #     method = getattr(new_cat_class, m)
    #     # smartie.method = method
    #     setattr(smartie, m, types.MethodType(method, smartie))
    #
    # smartie.say_name()
    #
    # print(inspect.getsource(smartie))
    #
    # cat = new_cat_class('Smartie')
    # cat.say_name()
    #
    #
    #
    # t = MyWidget()
    #
    # pickle_string = pickle.dumps(t)
    # print("pickled")
    # b = pickle.loads(pickle_string)
    #
    # print(b.a)
    #
    #
    # attributes = {}
    # b = B()
    # for e, v in b.__dict__.items():
    #     if not callable(v):
    #         attributes[e] = v
    # print(attributes)
    # print(callable(A))
    # print(callable(A()))
    # print(b.__dir__())
    #
    #
    #
    # sys.exit(app.exec_())


    # path = ''
    # replace_in_folder(path)


    # db = QFontDatabase()
    # print(QFontDatabase.families())


    # owm = OWM('0d8e9bf72996017261a908e7bf71e5b4')
    #
    # mgr = owm.weather_manager()
    # observation = mgr.weather_at_place('Tromsø')
    # w = observation.weather
    # print(w.__dict__)
    # print(w.ref_time)