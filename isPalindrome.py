def isPalindrome(s):
    s = "".join(s.split(" ")).lower()
    alpha = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    s_list = []
    for x in s:
        if x in alpha :
            s_list.append(x)
    
    s = "".join(s_list)

    print(s)
    return s == s [::-1]

print(isPalindrome("Was it a car or a cat I saw?"))