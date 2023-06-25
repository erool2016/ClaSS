


class A:
    def __init__(self,id):
        self.id = id

    def use_info(self,b,s):
        print(f'use info,\n{self.id} {b} {s}')
        self.send_info(b,s)

    def get_info(self):
        print(self.id * 2)
        b = self.id * 2
        s = b * 2
        print(b,s)
        self.use_info(b,s)

    def send_info(self,b,s):
        print(f'send info,\n{self.id} {b} {s}')
        b = B(b,s)
        b.save_db()




class B:
    def __init__(self,a,b):
        self.a = a
        self.b = b


    def save_db(self):
        print('save db a ',self.a)
        print('save db b ',self.b)


a = A(1001)

a.get_info()
