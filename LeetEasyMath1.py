#  Fizz Buzz
# Given an integer n, return a string array answer (1-indexed) where:
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # create an empty list to store the answers
        answer = []
        
        # loop through the numbers 1 to n (inclusive)
        for i in range(1, n+1):
            # if the number is divisible by both 3 and 5, add "FizzBuzz" to the answer list
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            # if the number is divisible by 3, add "Fizz" to the answer list
            elif i % 3 == 0:
                answer.append("Fizz")
            # if the number is divisible by 5, add "Buzz" to the answer list
            elif i % 5 == 0:
                answer.append("Buzz")
            # if none of the above conditions are true, add the number as a string to the answer list
            else:
                answer.append(str(i))
        
        # return the answer list
        return answer

