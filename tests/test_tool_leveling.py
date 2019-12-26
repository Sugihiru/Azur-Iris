import unittest

import env  # noqa
from ui.tool_leveling import ToolLeveling


class TestComputeRealLevel(unittest.TestCase):
    def test_computeRealLevel(self):
        self.assertEqual(
            ToolLeveling.computeRealLevel(currentLevel=120, currentExp=0),
            120)
        self.assertEqual(
            ToolLeveling.computeRealLevel(currentLevel=115, currentExp=100),
            115)
        self.assertEqual(
            ToolLeveling.computeRealLevel(currentLevel=1, currentExp=10),
            1)
        self.assertEqual(
            ToolLeveling.computeRealLevel(currentLevel=1, currentExp=100),
            2)
        self.assertEqual(
            ToolLeveling.computeRealLevel(currentLevel=1, currentExp=10_000),
            14)
        self.assertEqual(
            ToolLeveling.computeRealLevel(currentLevel=1,
                                          currentExp=4_325_675),
            120)
        self.assertEqual(
            ToolLeveling.computeRealLevel(currentLevel=115,
                                          currentExp=4_325_675),
            120)
        self.assertEqual(
            ToolLeveling.computeRealLevel(currentLevel=115,
                                          currentExp=4_325_675 - 2_940_675),
            120)
        self.assertEqual(
            ToolLeveling.computeRealLevel(currentLevel=115,
                                          currentExp=4_325_675 - 2_940_676),
            119)


class TestComputeNeededExpForLevel(unittest.TestCase):
    def testComputeNeededExpForLevel(self):
        self.assertEqual(
            ToolLeveling.computeNeededExpForLevel(targetLevel=120,
                                                  currentLevel=120,
                                                  currentExp=0),
            0)
        self.assertEqual(
            ToolLeveling.computeNeededExpForLevel(targetLevel=100,
                                                  currentLevel=120,
                                                  currentExp=0),
            0)
        self.assertEqual(
            ToolLeveling.computeNeededExpForLevel(targetLevel=2,
                                                  currentLevel=1,
                                                  currentExp=0),
            100)
        self.assertEqual(
            ToolLeveling.computeNeededExpForLevel(targetLevel=2,
                                                  currentLevel=1,
                                                  currentExp=50),
            50)
        self.assertEqual(
            ToolLeveling.computeNeededExpForLevel(targetLevel=4,
                                                  currentLevel=1,
                                                  currentExp=500),
            100)
