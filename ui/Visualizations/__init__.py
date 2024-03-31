import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

import VisualizationServiceModule
import CoordinatesVisualizationModule
import VectorVisualizationModule
import CoordinatesEditorDisplayModule
import CanvasDisplayModule
import MainDisplayModule
import ToolbarDisplayModule

visualization_service = VisualizationServiceModule.VisualizationService()
VisualizationServiceModule.InjectVisualizationService(visualization_service)
CoordinatesEditorDisplayModule.InjectVisualizationService(visualization_service)
CanvasDisplayModule.InjectVisualizationService(visualization_service)
MainDisplayModule.InjectVisualizationService(visualization_service)
ToolbarDisplayModule.InjectVisualizationService(visualization_service)