from naughty_or_nice_old_rules import is_nice_word as old_rules
from naughty_or_nice_new_rules import is_nice_word as new_rules


print(len([word for word in open("input.txt").readlines() if old_rules(word)]))
print(len([word for word in open("input.txt").readlines() if new_rules(word)]))
