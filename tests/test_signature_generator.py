import unittest
from blocklib import generate_signature


class TestPSig(unittest.TestCase):

    def test_feature_value(self):
        """Test signatures generated by feature-value."""
        attr_ind = [0, 1]
        dtuple = ('Joyce', 'Wang', 2134)
        signature_strategies = ['feature-value']
        signature_strategies_config = [{}]
        signatures = generate_signature(signature_strategies, attr_ind, dtuple,
                                        signature_strategies_config)
        assert signatures == set(['JoyceWang'])

    def test_feature_value_substrings(self):
        """Test signatures generated by feature-value."""
        attr_ind = [0, 1]
        list_substrings_indices = [[1, 4], [6]]
        dtuple = ('Joyce', 'Wang', 2134)
        signature_strategy = ['feature-value']
        signatures = generate_signature(signature_strategy, attr_ind, dtuple,
                                        [{'list_substrings_indices': list_substrings_indices}])
        assert signatures == {'oyc', 'ang'}

    def test_soundex(self):
        """Test signatures generated by soundex."""
        attr_ind = [0, 1]
        dtuple = ('Joyce', 'Wang', 2134)
        signature_strategies = ['soundex']
        signature_strategies_config = [{}]
        signatures = generate_signature(signature_strategies, attr_ind, dtuple, signature_strategies_config)
        assert signatures == {'W520', 'J200'}

    def test_n_gram(self):
        """Test signatures generated by n-gram."""
        attr_ind = [0, 1]
        dtuple = ('Joyce', 'Wang', 2134)

        # test 2-gram
        signature_strategies = ['n-gram', 'n-gram']
        signature_strategies_config = [{'n': 2}, {'n': 3}]
        signatures = generate_signature(signature_strategies, attr_ind, dtuple,
                                        signature_strategies_config)
        res1 = {'Jo', 'oy', 'yc', 'ce', 'eW', 'Wa', 'an', 'ng'}
        res2 = {'Joy', 'oyc', 'yce', 'ceW', 'eWa', 'Wan', 'ang'}
        assert signatures == res1.union(res2)