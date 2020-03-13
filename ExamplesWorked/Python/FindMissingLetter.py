# test.describe("kata tests")
# test.it("example tests")
# test.assert_equals(find_missing_letter(['a','b','c','d','f']), 'e')
# test.assert_equals(find_missing_letter(['O','Q','R','S']), 'P')

chars = ['O','Q','R','S']
def find_missing_letter(chars):
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    x = chars[0]
    y = alpha.find(x)
    for x in range(len(chars)):
        a = chars[x]
        b = alpha[y]
        if a != b:
            print("Missing value is ",b)
            return b
        else:
            y = y+1

find_missing_letter(chars)