class Polynomial():
    def __init__(self, iterable):
        non_zero_position = 0
        for i, c in enumerate(iterable):
            if c != 0:
                non_zero_position = i
                break

        self.coef = list(iterable)[non_zero_position:]
        self.deg = len(self.coef) - 1


    def __gt__(self, q):
        return self.deg > q.deg


    def __lt__(self, q):
        return self.deg < q.deg


    def __eq__(self, q):
        return self.coef == q.coef


    def __add__(self, q):
        result = []
        if self.deg >= q.deg:
            for i in self.coef[0:self.deg - q.deg]:
                result.append(i)
            for j, k in zip(self.coef[self.deg - q.deg:], q.coef):
                result.append(j + k)
        else:
            for i in q.coef[0:q.deg - self.deg]:
                result.append(i)            
            for j, k in zip(q.coef[q.deg - self.deg:], self.coef):
                result.append(j + k)            

        return Polynomial(result)


    def __sub__(self, q):
        result = []
        if self.deg >= q.deg:
            for i in self.coef[0:self.deg - q.deg]:
                result.append(i)
            for j, k in zip(self.coef[self.deg - q.deg:], q.coef):
                result.append(j - k)
        else:
            for i in q.coef[0:q.deg - self.deg]:
                result.append(-i)
            for j, k in zip(self.coef, q.coef[q.deg - self.deg:]):
                result.append(j - k)

        return Polynomial(result)       


    def linmul(self, c):
        result = []
        for i in self.coef:
            result.append(i * c)
        return Polynomial(result)


    def div(self, q):
        if q.deg > self.deg:
            raise ValueError
            return
        else:
            result, remainder = Polynomial([]), Polynomial([])
            result.coef.append(self.coef[0] / q.coef[0])
            remainder = self - Polynomial(q.linmul(self.coef[0] / q.coef[0]).coef + [0] * (self.deg - q.deg))

            while remainder.deg >= q.deg:
                result.coef.append(remainder.coef[0] / q.coef[0])
                remainder = remainder - Polynomial(q.linmul(remainder.coef[0] / q.coef[0]).coef + [0] * (remainder.deg - q.deg))
            
            return (result, remainder)
