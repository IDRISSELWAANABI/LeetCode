class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone_mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def backtrack(index, path):
            if index == len(digits):
                combinations.append("".join(path))
                return
            
            current_digit = digits[index]
            for char in phone_mapping[current_digit]:
                path.append(char)
                backtrack(index + 1, path)
                path.pop()
        
        combinations = []
        backtrack(0, [])
        return combinations
