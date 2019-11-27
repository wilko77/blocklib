from blocklib import generate_signatures


class TestPSig:

    def test_feature_value(self):
        """Test signatures generated by feature-value."""
        dtuple = ('Joyce', 'Wang', 2134)
        signatures = [[{'type': 'feature-value', 'feature-idx': 0},
                      {'type': 'feature-value', 'feature-idx': 1},
                      ]]
        signatures = generate_signatures(signatures, dtuple)
        assert signatures == {"JoyceWang"}

    def test_char_at(self):
        """Test signatures generated by characters-at."""
        dtuple = ('Joyce', 'Wang', 2134)
        # test start_ind: end_ind
        signatures = [[{'type': 'characters-at', 'feature-idx': 0, 'config': {'pos': ["1:4"]}},
                      {'type': 'characters-at', 'feature-idx': 1, 'config': {'pos': ["1:4"]}}
                      ]]
        signatures = generate_signatures(signatures, dtuple)
        assert signatures == {"oycang"}

        # test :end_ind
        strategy = [
            [
                {'type': 'characters-at', 'feature-idx': 0, 'config': {'pos': [':2', '-2:', 2, '2']}}
            ]
        ]
        signature = generate_signatures(strategy, dtuple)
        assert signature == {"Joceyy"}

    # def test_soundex(self):
    #     """Test signatures generated by soundex."""
    #     dtuple = ('Joyce', 'Wang', 2134)
    #     signature_strategies = [[{'type': 'soundex', 'feature-idx': 0},
    #                             {'type': 'soundex', 'feature-idx': 1},]]
    #     signatures = generate_signatures(signature_strategies, dtuple)
    #     assert signatures == {'J2W52'}

    def test_metaphonee(self):
        """Test signatures generated by metaphone."""
        dtuple = ('Smith', 'Schmidt', 2134)
        signature_strategies = [
            [
                {'type': 'metaphone', 'feature-idx': 0}
            ]
        ]
        signatures = generate_signatures(signature_strategies, dtuple)
        assert signatures == {"SM0XMT"}
        'SM0XMT'

    def test_generate_signatures(self):
        """Test a multi-stragegy signatures."""
        dtuple = ('Joyce', 'Wang', 2134)
        signatures = [
            [
                {'type': 'feature-value', 'feature-idx': 0},
                {'type': 'feature-value', 'feature-idx': 1},
            ],
            [
                {'type': 'soundex', 'feature-idx': 0},
                {'type': 'soundex', 'feature-idx': 1},
            ]
        ]
        signatures = generate_signatures(signatures, dtuple)
        assert signatures == {"J2W52", "JoyceWang"}
