# test_animehandler.py
"""
Tests for AnimeHandler module.
"""

import unittest
from animehandler import AnimeHandler

class TestAnimeHandler(unittest.TestCase):
    """Test cases for AnimeHandler class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AnimeHandler()
        self.assertIsInstance(instance, AnimeHandler)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AnimeHandler()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
