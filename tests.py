# coding: utf-8
from hstest.stage_test import StageTest
from hstest.test_case import TestCase, SimpleTestCase


class RegexTest(StageTest):
    m_cases = [
        # stage 1
        ("a", "a",          "True",     "Two identical patterns should return True!"),
        ("a", "b",          "False",    "Two different patterns should not return True!"),
        ("7", "7",          "True",     "Two identical patterns should return True!"),
        ("6", "7",          "False",    "Two different patterns should not return True!"),
        (".", "a",          "True",     "Don't forget that '.' is a wild-card that matches any single character."),
        ("a", ".",          "False",    "A period in the input string is still a literal!"),
        ("", "a",           "True",     "An empty regex always returns True!"),
        ("", "",            "True",     "An empty regex always returns True!"),
        ("a", "",           "False",    "A non-empty regex and an empty input string always returns False!"),
        # stage 2
        ("apple", "apple",  "True",     "Two identical equal-length patterns should return True!"),
        (".pple", "apple",  "True",     "The wild-card '.' should match any single character in a string."),
        ("appl.", "apple",  "True",     "The wild-card '.' should match any single character in a string."),
        (".....", "apple",  "True",     "The wild-card '.' should match any single character in a string."),
        ("", "apple",       "True",     "An empty regex always returns True!"),
        ("apple", "",       "False",    "A non-empty regex and an empty input string always returns False!"),
        ("apple", "peach",  "False",    "Two different patterns should not return True!"),
        # stage 3
        ("le", "apple",     "True",     "If the input string contains the regex, it should return True!"),
        ("app", "apple",    "True",     "If the input string contains the regex, it should return True!"),
        ("a", "apple",      "True",     "If the input string contains the regex, it should return True!"),
        (".", "apple",      "True",     "Even a single wild-card character '.' can produce a match!"),
        ("apwle", "apple",  "False",    "Two different patterns should not return True!"),
        ("peach", "apple",  "False",    "Two different patterns should not return True!"),
        # stage 4
        ('^app', 'apple',           "True",
         "A regex starting with '^' should match the following pattern only at the beginning of the input string!"),
        ('le$', 'apple',            "True",
         "A regex ending with '$' should match the preceding pattern only at the end of the input string!"),
        ('^a', 'apple',             "True",
         "A regex starting with '^' should match the following pattern only at the beginning of the input string!"),
        ('.$', 'apple',             "True",
         "A regex ending with '$' should match the preceding pattern only at the end of the input string!"),
        ('apple$', 'tasty apple',   "True",
         "A regex ending with '$' should match the preceding pattern only at the end of the input string!"),
        ('^apple', 'apple pie',     "True",
         "A regex starting with '^' should match the following pattern only at the beginning of the input string!"),
        ('^apple$', 'apple',        "True",
         "A regex starting with '^' and ending with '$' should match only the enclosed literals!"),
        ('^apple$', 'tasty apple',  "False",
         "A regex starting with '^' and ending with '$' should match only the enclosed literals!"),
        ('^apple$', 'apple pie',    "False",
         "A regex starting with '^' and ending with '$' should match only the enclosed literals!"),
        ('app$', 'apple',           "False",
         "A regex ending with '$' should match the preceding pattern only at the end of the input string!"),
        ('^le', 'apple',            "False",
         "A regex starting with '^' should match the following pattern only at the beginning of the input string!"),
        # stage 5
        ("colou?r", "color",        "True",
         "'?' in a regex should match the preceding character exactly 0 or 1 times!"),
        ("colou?r", "colour",       "True",
         "'?' in a regex should match the preceding character exactly 0 or 1 times!"),
        ("colou?r", "colouur",      "False",
         "'?' in a regex should match the preceding character exactly 0 or 1 times!"),
        ("colou*r", "color",        "True",
         "'*' in a regex should match the preceding character 0 or more times!"),
        ("colou*r", "colour",       "True",
         "'*' in a regex should match the preceding character 0 or more times!"),
        ("colou*r", "colouur",      "True",
         "'*' in a regex should match the preceding character 0 or more times!"),
        ("colou+r", "colour",        "True",
         "'+' in a regex should match the preceding character 1 or more times!"),
        ("colou+r", "color",        "False",
         "'+' in a regex should match the preceding character 1 or more times!"),
        (".*", "aaa",               "True",
         "The repetition operators can be combined with the wild card '.'!"),
        (".+", "aaa",               "True",
         "The repetition operators can be combined with the wild card '.'!"),
        (".?", "aaa",               "True",
         "The repetition operators can be combined with the wild card '.'!"),
        ("no+$", "noooooooope",     "False",
         "The repetition operators can be combined with other metacharacters, like '.', '^' and '$'."),
        ("^no+", "noooooooope",     "True",
         "The repetition operators can be combined with other metacharacters, like '.', '^' and '$'."),
        ("^no+pe$", "noooooooope",     "True",
         "The repetition operators can be combined with other metacharacters, like '.', '^' and '$'."),
        ("^n.+pe$", "noooooooope",     "True",
         "The repetition operators can be combined with other metacharacters, like '.', '^' and '$'."),
        ("^n.+p$", "noooooooope",     "False",
         "The repetition operators can be combined with other metacharacters, like '.', '^' and '$'."),
        ('^.*c$', 'abcabc', "True",
         "The repetition operators can be combined with other metacharacters, like '.', '^' and '$'."),
        # stage 6
        ("\\.$",  "end.",              "True",
         "Don't forget that '\\' is an escape symbol in Python itself, so it has to be duplicated!"),
        ("3\\+3", "3+3=6",             "True",
         "Don't forget that '\\' is an escape symbol in Python itself, so it has to be duplicated!"),
        ("\\?",   "Is this working?",  "True",
         "Don't forget that '\\' is an escape symbol in Python itself, so it has to be duplicated!"),
        ("\\\\",  "\\",                "True",
         "Don't forget that '\\' is an escape symbol in Python itself, so it has to be duplicated!"),
        ("colou\\?r", "color",         "False",
         "Don't forget that '\\' is an escape symbol in Python itself, so it has to be duplicated!"),
        ("colou\\?r", "colour",        "False",
         "Don't forget that '\\' is an escape symbol in Python itself, so it has to be duplicated!")
    ]


    def generate(self):
        return [
            SimpleTestCase(
                stdin="{0}|{1}".format(regex, text),
                stdout=output,
                feedback=fb
            ) for regex, text, output, fb in self.m_cases
        ]


if __name__ == '__main__':
    RegexTest('regex.regex').run_tests()
