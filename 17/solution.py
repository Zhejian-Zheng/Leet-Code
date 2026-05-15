class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letter_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        res = [""]
        for num in digits:
            temp = []
            letters = letter_map[num]

            for current_str in res:
                for char in letters:
                    temp.append(current_str + char)

            res = temp
            
        return res