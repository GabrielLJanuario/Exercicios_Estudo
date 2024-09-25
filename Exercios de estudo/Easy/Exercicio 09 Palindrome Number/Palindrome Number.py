num=10
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if num >= 0:
            num_invert = str(num)[::-1]
            num_int_invert=int(num_invert)
            if num==num_int_invert:
                print(str(num) +" reads as " +str(num)+ " from left to right and from right to left.")
                return True
            else:
                print("From left to right, it reads " + str(num) + " . From right to left, it becomes " + str(num_invert) + ". Therefore it is not a palindrome.")
                return False
        else:
            num_invert = str(num)[::-1]
            # num_str = int(num_str)
            # num_str = num_str * -1
            print("From left to right, it reads " + str(num) + " . From right to left, it becomes " + str(num_invert) + ". Therefore it is not a palindrome.")
            return False
        return;


sol= Solution()
print(sol.isPalindrome(num))
