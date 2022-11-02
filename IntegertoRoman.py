class Solution:
    def intToRoman(self, num: int) -> str:
        s = ["MMM", "MM", "M", "CM", "DCCC", "DCC", "DC", "D", "CD",
                "CCC",	"CC", "C", "XC", "LXXX", "LXX", "LX", "L", "XL",
                "XXX", "XX", "X", "IX", "VIII", "VII", "VI", "V", "IV",
                "III", "II", "I"]
        a = [3000, 2000, 1000, 900, 800, 700, 600, 500, 400,
                300, 200, 100, 90, 80, 70, 60, 50, 40,
                30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        out = ""
        for i in range(30):
            if a[i] <= num:
                out += s[i]
                num -= a[i]
        return out

fin = open("oo.xx", "r")
fout = open("xx.oo", "w")

n = int(fin.readline()[:-1])
out = Soluton().intToRoman(n)
print(out)

