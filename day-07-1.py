from icecream import ic
from more_itertools import interleave_longest

def get_operator_lists(n):
    operators = ['+', '*']
    # yield all possible operators for n inputs
    if n == 1:
        for op in operators:
            yield [op]
    else:
        for op in operators:
            for sub_ops in get_operator_lists(n-1):
                yield [op] + sub_ops


def main():
    eqs = []
    with open('data/07.data') as f:
        for row in enumerate(f):
            res, inputs = row[1].strip().split(': ')
            res = int(res)
            inputs = inputs.split(' ')
            eqs.append((res, inputs))
    sum_of_valid = 0
    for eq in eqs:
        res, inputs = eq
        for oplist in get_operator_lists(len(inputs) - 1):
            candidate_res = inputs[0]
            for op, input in zip(oplist, inputs[1:]):
                candidate_res = eval(str(candidate_res) + op + input)
                if candidate_res > res:
                    # already too big
                    break
            if candidate_res == res:
                sum_of_valid += res
                break

    ic(sum_of_valid)

    # 3749 is correct
if __name__ == '__main__':
    main()
