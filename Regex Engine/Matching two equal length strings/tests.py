# coding: utf-8
from hstest.stage_test import StageTest
from hstest.test_case import SimpleTestCase

import time

class RegexTest(StageTest):
    m_cases = [
        # stage 1
        ("a", "a", "true", "Two identical patterns should return true!"),
        ("a", "b", "false", "Two different patterns should not return true!"),
        ("7", "7", "true", "Two identical patterns should return true!"),
        ("6", "7", "false", "Two different patterns should not return true!"),
        (".", "a", "true", "Don't forget that '.' is a wild-card that matches any single character."),
        ("a", ".", "false", "A period in the input string is still a literal!"),
        ("", "a", "true", "An empty regex always returns true!"),
        ("", "", "true", "An empty regex always returns true!"),
        ("a", "", "false", "A non-empty regex and an empty input string always returns false!"),
        # stage 2
        ("apple", "apple", "true", "Two identical equal-length patterns should return true!"),
        (".pple", "apple", "true", "The wild-card '.' should match any single character in a string."),
        ("appl.", "apple", "true", "The wild-card '.' should match any single character in a string."),
        (".....", "apple", "true", "The wild-card '.' should match any single character in a string."),
        ("", "apple", "true", "An empty regex always returns true!"),
        ("apple", "", "false", "A non-empty regex and an empty input string always returns false!"),
        ("apple", "peach", "false", "Two different patterns should not return true!")
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
