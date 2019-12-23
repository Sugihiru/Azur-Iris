import unittest

import env  # noqa
from ui.research_widget import ResearchWidget


class TestComputeRequiredBlueprintsForStrengthenLevel(unittest.TestCase):
    def test_computeRequiredBlueprintsForStrengthenLevel(self):
        self.assertEqual(
            ResearchWidget.computeRequiredBlueprintsForStrengthenLevel(
                target_level=30, current_level=25, current_bp=0,
                is_decisive_ship=False),
            120)
        self.assertEqual(
            ResearchWidget.computeRequiredBlueprintsForStrengthenLevel(
                target_level=30, current_level=25, current_bp=0,
                is_decisive_ship=True),
            180)
        self.assertEqual(
            ResearchWidget.computeRequiredBlueprintsForStrengthenLevel(
                target_level=25, current_level=30, current_bp=0,
                is_decisive_ship=False),
            0)
        self.assertEqual(
            ResearchWidget.computeRequiredBlueprintsForStrengthenLevel(
                target_level=20, current_level=25, current_bp=0,
                is_decisive_ship=False),
            0)
        self.assertEqual(
            ResearchWidget.computeRequiredBlueprintsForStrengthenLevel(
                target_level=30, current_level=25, current_bp=10,
                is_decisive_ship=False),
            110)
        self.assertEqual(
            ResearchWidget.computeRequiredBlueprintsForStrengthenLevel(
                target_level=30, current_level=27, current_bp=10,
                is_decisive_ship=False),
            70)
        self.assertEqual(
            ResearchWidget.computeRequiredBlueprintsForStrengthenLevel(
                target_level=30, current_level=25, current_bp=40,
                is_decisive_ship=False),
            80)
        self.assertEqual(
            ResearchWidget.computeRequiredBlueprintsForStrengthenLevel(
                target_level=30, current_level=20, current_bp=90,
                is_decisive_ship=False),
            120)

    def test_computeRequiredBlueprintsForFateSimulation(self):
        self.assertEqual(
            ResearchWidget.computeRequiredBlueprintsForFateSimulation(
                target_phase=5, current_phase=4, current_bp=0), 65)
        self.assertEqual(
            ResearchWidget.computeRequiredBlueprintsForFateSimulation(
                target_phase=4, current_phase=5, current_bp=0), 0)
        self.assertEqual(
            ResearchWidget.computeRequiredBlueprintsForFateSimulation(
                target_phase=3, current_phase=4, current_bp=0), 0)
        self.assertEqual(
            ResearchWidget.computeRequiredBlueprintsForFateSimulation(
                target_phase=5, current_phase=4, current_bp=10), 55)
        self.assertEqual(
            ResearchWidget.computeRequiredBlueprintsForFateSimulation(
                target_phase=5, current_phase=3, current_bp=50), 55)
