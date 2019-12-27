import math
import unittest

import env  # noqa
from ui.tool_stage_exp import ToolStageExp


class TestComputeGainedExp(unittest.TestCase):
    def test_computeGainedExp(self):
        self.assertEqual(
            ToolStageExp.computeGainedExp(baseExp=500, sRank=False),
            500)
        self.assertEqual(
            ToolStageExp.computeGainedExp(baseExp=500, sRank=True),
            int(500 * 1.2))
        self.assertEqual(
            ToolStageExp.computeGainedExp(baseExp=500, sRank=True, mvp=True),
            int(500 * 1.2 * 2))
        self.assertEqual(
            ToolStageExp.computeGainedExp(baseExp=500, sRank=True,
                                          flagship=True),
            int(500 * 1.2 * 1.5))
        self.assertEqual(
            ToolStageExp.computeGainedExp(baseExp=500, sRank=True,
                                          mvp=True, flagship=True),
            int(500 * 1.2 * 2 * 1.5))
        self.assertEqual(
            ToolStageExp.computeGainedExp(baseExp=500, sRank=False,
                                          bonusExp=1.5),
            int(500 * 1.5))
        self.assertEqual(
            ToolStageExp.computeGainedExp(baseExp=500, sRank=True,
                                          bonusExp=1.5),
            int(500 * 1.5 * 1.2))
        self.assertEqual(
            ToolStageExp.computeGainedExp(baseExp=500, sRank=False,
                                          bonusExp=1.42),
            int(500 * 1.42))
        self.assertEqual(
            ToolStageExp.computeGainedExp(baseExp=3, sRank=False,
                                          bonusExp=1.5),
            4)
        self.assertEqual(
            ToolStageExp.computeGainedExp(baseExp=777, sRank=True,
                                          bonusExp=1.42, mvp=True,
                                          flagship=True),
            int(math.floor(777 * 1.2 * 1.42 * 2 * 1.5)))
