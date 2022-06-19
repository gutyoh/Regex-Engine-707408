# coding: utf-8
from hstest.stage_test import StageTest
from hstest.test_case import TestCase, SimpleTestCase

import time


class RegexTest(StageTest):
    m_cases = [
        # stage 1
        ("a", "a", "true", "Two identical patterns should return True!"),
        ("a", "b", "false", "Two different patterns should not return True!"),
        ("7", "7", "true", "Two identical patterns should return True!"),
        ("6", "7", "false", "Two different patterns should not return True!"),
        (".", "a", "true", "Don't forget that '.' is a wild-card that matches any single character."),
        ("a", ".", "false", "A period in the input string is still a literal!"),
        ("", "a", "true", "An empty regex always returns True!"),
        ("", "", "true", "An empty regex always returns True!"),
        ("a", "", "false", "A non-empty regex and an empty input string always returns False!"),
        # stage 2
        ("apple", "apple", "true", "Two identical equal-length patterns should return True!"),
        (".pple", "apple", "true", "The wild-card '.' should match any single character in a string."),
        ("appl.", "apple", "true", "The wild-card '.' should match any single character in a string."),
        (".....", "apple", "true", "The wild-card '.' should match any single character in a string."),
        ("", "apple", "true", "An empty regex always returns True!"),
        ("apple", "", "false", "A non-empty regex and an empty input string always returns False!"),
        ("apple", "peach", "false", "Two different patterns should not return True!"),
        # stage 3
        ("le", "apple", "true", "If the input string contains the regex, it should return True!"),
        ("app", "apple", "true", "If the input string contains the regex, it should return True!"),
        ("a", "apple", "true", "If the input string contains the regex, it should return True!"),
        (".", "apple", "true", "Even a single wild-card character '.' can produce a match!"),
        ("apwle", "apple", "false", "Two different patterns should not return True!"),
        ("peach", "apple", "false", "Two different patterns should not return True!"),
        # stage 4
        ('^app', 'apple', "true",
         "A regex starting with '^' should match the following pattern only at the beginning of the input string!"),
        ('le$', 'apple', "true",
         "A regex ending with '$' should match the preceding pattern only at the end of the input string!"),
        ('^a', 'apple', "true",
         "A regex starting with '^' should match the following pattern only at the beginning of the input string!"),
        ('.$', 'apple', "true",
         "A regex ending with '$' should match the preceding pattern only at the end of the input string!"),
        ('apple$', 'tasty apple', "true",
         "A regex ending with '$' should match the preceding pattern only at the end of the input string!"),
        ('^apple', 'apple pie', "true",
         "A regex starting with '^' should match the following pattern only at the beginning of the input string!"),
        ('^apple$', 'apple', "true",
         "A regex starting with '^' and ending with '$' should match only the enclosed literals!"),
        ('^apple$', 'tasty apple', "false",
         "A regex starting with '^' and ending with '$' should match only the enclosed literals!"),
        ('^apple$', 'apple pie', "false",
         "A regex starting with '^' and ending with '$' should match only the enclosed literals!"),
        ('app$', 'apple', "false",
         "A regex ending with '$' should match the preceding pattern only at the end of the input string!"),
        ('^le', 'apple', "false",
         "A regex starting with '^' should match the following pattern only at the beginning of the input string!")
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
    start = time.time()
    RegexTest().run_tests()
    end = time.time()
    print(f'Total time taken for tests: {(end - start):.2f} seconds')
