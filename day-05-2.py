from icecream import ic
from collections import defaultdict

def is_valid_update(update, rules):
    valid_update = True
    rules_for_update = rules.copy()
    new_update = update.copy()
    for rule in rules_for_update:
        try:
            before_index = new_update.index(rule[0])
            after_index = new_update.index(rule[1])
        except ValueError:
            # rule not found in update
            continue
        if not before_index < after_index:
            valid_update = False
            # switch the pages
            new_update[after_index] = rule[0]
            new_update[before_index] = rule[1]
            continue
    return valid_update, new_update

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
        new_update = update.copy()
        valid_update = False
        valid_update, new_update = is_valid_update(new_update, rules)
        if valid_update:
            # skip initially valid updates
            continue
        while True:
            valid_update, new_update = is_valid_update(new_update, rules)
            if valid_update:
                break
        # get the middle page from new_update
        middle_index = len(new_update) // 2
        middle_page = new_update[middle_index]
        sum_of_middle_pages += int(middle_page)
    ic(sum_of_middle_pages)
    # 143 is correct

if __name__ == '__main__':
    main()
