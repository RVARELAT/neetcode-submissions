class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            print("yooo")
        s_list = list(s)
        s_list.sort()
        print(s_list)
        t_list = list(t)
        t_list.sort()
        print(t_list)
        if (t_list == s_list):
            return True
        return False


        