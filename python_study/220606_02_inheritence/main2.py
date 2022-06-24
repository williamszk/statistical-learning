
from abc import ABC, abstractmethod

# @ABC
class PPC(ABC):

    def kkfunc(self):
        print('kk func in parent class')

    def __call__(self, x):
        xx= self.forward(x)
        # print('call function === ', x)
        return xx

    @abstractmethod
    def forward(self, x):
        raise NotImplementedError("no .forward method")

# This doesn’t change how any of the classes work, but the @ABC and
# @abstractmethod decorator arrange that you can’t actually make an
# instance of PPC. The @ABC decorator makes the class check that none of
# its methods are abstractmethods.


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
