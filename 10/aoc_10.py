#!/usr/bin/env python3

def match(open_p, close_p):
    if open_p == '(' and close_p == ')':
        return True

    if open_p == '[' and close_p == ']':
        return True

    if open_p == '{' and close_p == '}':
        return True

    if open_p == '<' and close_p == '>':
        return True

    return False

# --------
    
def part_one():
    paren2score = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    
    with open("input.txt", "r") as f:
        stack = []
        score = 0
        for line in f.readlines():
            for c in line:
                if c in ['(', '[', '{', '<']:
                    # -- when see opening parenthesis do a push
                    stack.append(c)
                elif c in [')', ']', '}', '>']:
                    # -- when see a closing parenthesis, do a pop and
                    # -- check if type matches.
                    opening_paren = stack.pop()
                    closing_paren = c

                    if not match(opening_paren, closing_paren):
                        score += paren2score[closing_paren]

        print(f"Result of part one: {score}")
        
# ----------------------------
    
def part_two():

    open2close = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    paren2score = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,        
    }
    
    with open("input.txt", "r") as f:
        scores = []
        
        for line in f.readlines():
            stack = []
            is_corrupted = False
            
            for c in line:
                if c in ['(', '[', '{', '<']:
                    # -- when see opening parenthesis do a push
                    stack.append(c)
                elif c in [')', ']', '}', '>']:
                    # -- when see a closing parenthesis, do a pop and
                    # -- check if type matches.
                    opening_paren = stack.pop()
                    closing_paren = c

                    if not match(opening_paren, closing_paren):
                        # -- discard corrupted lines
                        is_corrupted = True
                        break

            if not is_corrupted and len(stack) > 0:
                # -- compute score and add it to list of scores
                score = 0
                stack.reverse()
                for p in stack:
                    closing_p = open2close[p]
                    score = score * 5 + paren2score[closing_p]
                scores.append(score)

        scores.sort()
        # NOTE: it is assume we always have a single middle score
        middle_score = scores[int(len(scores) / 2)]
        print(f"Result of part two: {middle_score}") 

# ------
    
if __name__ == "__main__":
    part_one()
    part_two()
