class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
        res = ""
        keys_list = sorted(list(d.keys()), reverse=True)

        if num in keys_list:
            res += d[num]
        else:
            for i in keys_list:
                while num >= i:
                    num -= i
                    res += d[i]
        return res
