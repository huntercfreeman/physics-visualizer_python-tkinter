import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

import DialogModelModule
import DialogServiceModule
import DialogInitializerDisplayModule
import DialogDisplayModule

dialog_service = DialogServiceModule.DialogService()
DialogServiceModule.InjectDialogService(dialog_service)
DialogDisplayModule.InjectDialogService(dialog_service)