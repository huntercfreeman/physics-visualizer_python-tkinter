class VisualizationService:
    pass

def InjectVisualizationService(injectedVisualizationService: VisualizationService):
    global visualization_service
    visualization_service = injectedVisualizationService

visualization_service: VisualizationService = None