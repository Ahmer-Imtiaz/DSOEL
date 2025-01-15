#23-ai-55
def longest_palindrome (s):
# this function is made to check the maximum length of palindrome thats using a string s
    char_count = {}
# loop for increment of each charcater    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
# to keep record of palindrome length
    length = 0 
# to check odds
    odd_count_found = False
    for count in char_count.values():
# to check is it odd or even
        length += count  // 2*2 
        if count % 2 == 1:
            odd_count_found = True
# to check if odd exists and adding 1 to length
    if odd_count_found:
        length += 1
    return length


# exmaple use

if __name__ == "__main__":
    example1 = "abccba"
    example2 = "a"

# for output 
print ("Input: ", example1 , "-> Longest_palindrome Length", longest_palindrome(example1))
print ("Input: ", example2 , "-> Longest_palindrome Length", longest_palindrome(example2))
