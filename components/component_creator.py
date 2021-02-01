"""
"""
import components.component_manager as component_manager
import components.component as component


class ComponentCreator(component_manager.ComponentManager):

    def __init__(self, database_path, installed_components: dict):
        component_manager.ComponentManager.__init__(self, database_path=database_path,
                                                    installed_components=installed_components)

    def get_installed_components(self) -> dict:
        return self.installed_components

    def select_creation_matrix(self, request: int):
        all_components: list = list(self.installed_components.keys())
        matrix_name = all_components[request-1]
        return self.installed_components.get(matrix_name)

    def create_component(self, component_name, request) -> component.Component:
        selected_matrix = self.select_creation_matrix(request=request)
        return selected_matrix(name=component_name)

    def sort_component(self, new_component: component.Component):
        component_type: str = new_component.get_type
        target_component: list = self.loaded_data.get(component_type)
        target_component.append(new_component.get_name)







