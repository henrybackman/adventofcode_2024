from icecream import ic
from collections import defaultdict

def main():
    rules = []
    updates = []
    collecting_rules = True
    with open('data/05.data') as f:
        for row in f:
            if row == '\n':
                collecting_rules = False
                continue
            if collecting_rules:
                before, after = row.strip().split("|")
                rules.append((before, after))
            else:
                updates.append(row.strip().split(","))

    sum_of_middle_pages = 0
    for update in updates:
        valid_update = True
        rules_for_update = rules.copy()
        for rule in rules_for_update:
            try:
                before_index = update.index(rule[0])
                after_index = update.index(rule[1])
            except ValueError:
                # rule not found in update
                continue
            if not before_index < after_index:
                valid_update = False
                break
        if valid_update:
            # get the middle page from update
            middle_index = len(update) // 2
            middle_page = update[middle_index]
            sum_of_middle_pages += int(middle_page)
    ic(sum_of_middle_pages)
    # 143 is correct

if __name__ == '__main__':
    main()
