
class PPC():
    def kkfunc(self):
        print('kk func in parent class')

    def __call__(self, x):
        xx = self.forward(x)
        # print('call function === ', x)
        return xx


class PPSub(PPC):
    def __init__(self):
        pass

    def pfunc(self):
        print('in sub class')

    def forward(self, x):
        print('forward function in ppsub class===', x)
        return x+1


ps1 = PPSub()
xxx = ps1(9)

print(xxx)