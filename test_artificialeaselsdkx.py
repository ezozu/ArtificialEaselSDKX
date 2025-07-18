# test_artificialeaselsdkx.py
"""
Tests for ArtificialEaselSDKX module.
"""

import unittest
from artificialeaselsdkx import ArtificialEaselSDKX

class TestArtificialEaselSDKX(unittest.TestCase):
    """Test cases for ArtificialEaselSDKX class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ArtificialEaselSDKX()
        self.assertIsInstance(instance, ArtificialEaselSDKX)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ArtificialEaselSDKX()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
