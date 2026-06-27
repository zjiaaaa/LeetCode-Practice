class Solution:
    def climbStairs(self, n: int) -> int:
        list1 = {}
        
        def num(steps):
            if steps == 1:
                return 1
            if steps == 2:
                return 2
            if steps in list1:
                return list1[steps]

            list1[steps] = num(steps-1)+num(steps-2)
            return list1[steps]

        return num(n)


        