# The first input array contains the correct answers to an exam, like ["a", "a", "b", "d"]. The second one is "answers" array and contains student's answers.

# The two arrays are not empty and are the same length. Return the score for this array of answers, giving +4 for each correct answer, -1 for each incorrect answer, and +0 for each blank answer(empty string).

# If the score < 0, return 0.
arr1 = ["a", "a", "b", "b"]
arr2 = ["a", "c", "b", "d"]
def check_exam(arr1,arr2):
    score = 0
    for i in range(0,4):
        if arr1[i] == arr2[i]:
            score += 4
        elif arr1[i] == "" or arr2[i] == "":
            score += 0
        else: 
            score -= 1
    print( score if score >= 0  else 0  )
    return score if score >= 0  else 0  
    
check_exam(arr1,arr2)

# Test.it("Basic tests")
# Test.assert_equals(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]), 6)
# Test.assert_equals(check_exam(["a", "a", "c", "b"], ["a", "a", "b",  ""]), 7)
# Test.assert_equals(check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"]), 16)
# Test.assert_equals(check_exam(["b", "c", "b", "a"], ["",  "a", "a", "c"]), 0)