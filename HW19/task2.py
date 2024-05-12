"""
https://www.codewars.com/kata/52449b062fb80683ec000024


DESCRIPTION:
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
"""


def generate_hashtag(s):
    if not s:
        return False
    s = s.lower()
    s = s.title()
    s = s.split()
    s = "".join(s)
    s_new = "#" + s
    if len(s_new) > 140:
        return False
    else:
        return s_new


print(generate_hashtag(" Hello there thanks for trying my Kata"))
print(generate_hashtag("   Hi there ITs good"))
print(generate_hashtag(" 1 Number in 2 words"))
