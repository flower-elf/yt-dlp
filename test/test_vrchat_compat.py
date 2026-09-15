#!/usr/bin/env python3

# Allow direct execution
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from yt_dlp.options import parseOpts


class TestVRChatCompat(unittest.TestCase):
    """Old VRChat video players invoke yt-dlp with these options, so they must keep parsing"""

    def test_allow_list_options_are_accepted_and_ignored(self):
        for opt in ('--explicit-allow-list', '--exp-allow', '--wildcard-allow-list', '--wild-allow'):
            with self.subTest(opt=opt):
                _, opts, args = parseOpts([opt, 'youtube.com', 'https://example.com/v'], ignore_config_files=True)
                self.assertEqual(args, ['https://example.com/v'])
                self.assertEqual(opts.explicit_allow_list or opts.wildcard_allow_list, 'youtube.com')


if __name__ == '__main__':
    unittest.main()
