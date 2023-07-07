class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        c3 = c5 = 0

        for i in range(1, n+1):
            res = ''
            c3 += 1
            c5 += 1

            if c3 == 3:
                res += 'Fizz'
                c3 = 0
            if c5 == 5:
                res += 'Buzz'
                c5 = 0
            if res == '':
                res = str(i)
            answer.append(res)
        return answer

    # def fizzBuzz(self, n: int) -> List[str]:
    #     res = []
    #     for i in range(1, n+1):
    #         if not i % 15:
    #             res.append('FizzBuzz')
    #         elif not i % 3:
    #             res.append('Fizz')
    #         elif not i % 5:
    #             res.append('Buzz')
    #         else:
    #             res.append(str(i))
    #     return res
