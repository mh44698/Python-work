# pangram = "The quick, brown fox jumps over the lazy dog!"
# Test.assert_equals(is_pangram(pangram), True)


import string
s = "The quick, brown fox jumps over the lazy dog!"
def is_pangram(s):
    s = s.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if alpha == s:
        return False
    for alpha in s:
        print("")
    print("True")
    return True
is_pangram(s)