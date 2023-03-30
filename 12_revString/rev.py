
def reverse(str):
    st = ""
    for i in str:
        st = i + st
    return st
 
word = "Differentwords"
 
print("The original string is : ")
print(word)
 
print("The reversed string is : ")
print(reverse(word))