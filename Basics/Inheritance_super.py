# class Base:
#     def __init__(self):
#         print('Base.__init__')
#
#
# class Child1(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print('Child1.__init__')
#
#
# class Child2(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print('Child2.__init__')
#
#
# class Child3(Child1, Child2):
#     def __init__(self):
#         Child1.__init__(self)
#         Child2.__init__(self)
#         print('Child3.__init__')
#
# c3 = Child3()
# print(Child3.mro())

# ###############################################
# # with Super
# # even though there is only one super() in Child3, all init methods from all parents will be executed
#
# class Base:
#     def __init__(self):
#         print('Base.__init__')
#
#
# class Child1(Base):
#     def __init__(self):
#         super().__init__()
#         print('Child1.__init__')
#
#
# class Child2(Base):
#     def __init__(self):
#         super().__init__()
#         print('Child2.__init__')
#
#
# class Child3(Child1, Child2):
#     def __init__(self):
#         super().__init__()
#         print('Child3.__init__')
#
#
# c3 = Child3()
# print(Child3.mro())


################################################
# Using Super without parent class
# having super() in all three classes ensure that the init method from all parent classes will be executed even though
# there is only one super() in Child3


class Child1():
    def __init__(self):
        super().__init__()
        print('Child1.__init__')


class Child2():
    def __init__(self):
        super().__init__()
        print('Child2.__init__')


class Child3(Child1, Child2):
    def __init__(self):
        super().__init__()
        print('Child3.__init__')


c3 = Child3()

print(Child3.mro())
