import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

import LayoutServiceModule
import PanelModelModule
import AppBodyDisplayModule
import AppFooterDisplayModule
import AppHeaderDisplayModule

layout_service = LayoutServiceModule.LayoutService()
LayoutServiceModule.InjectLayoutService(layout_service)
PanelModelModule.InjectLayoutService(layout_service)
AppBodyDisplayModule.InjectLayoutService(layout_service)
AppFooterDisplayModule.InjectLayoutService(layout_service)
AppHeaderDisplayModule.InjectLayoutService(layout_service)