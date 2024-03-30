import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

import ThemeModelModule
import ThemeServiceModule

theme_service = ThemeServiceModule.ThemeService()
ThemeServiceModule.InjectThemeService(theme_service)