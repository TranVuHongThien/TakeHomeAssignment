class NestedSetModel:
    def __init__(self):
        self.tree_structure = []
        self.left_index = 1
        self.right_index = 2

    def convert_to_nested_set(self, hierarchical_data):
        """
        Convert hierarchical data to the nested set model.

        Args:
        - hierarchical_data (list): List of dictionaries representing hierarchical data.

        Returns:
        - None
        """
        self.tree_structure = []
        self.left_index = 1
        self.right_index = 2
        self._build_nested_set(hierarchical_data)

    def _build_nested_set(self, node_list, parent=None):
        """
        Recursively build the nested set model.

        Args:
        - node_list (list): List of dictionaries representing hierarchical data.
        - parent: Parent node.

        Returns:
        - None
        """
        for node in node_list:
            self.tree_structure.append({
                'node': node,
                'left_index': self.left_index,
                'right_index': None,
            })
            self.left_index += 1

            if 'children' in node:
                self._build_nested_set(node['children'], node)

            self.tree_structure[-1]['right_index'] = self.left_index
            self.left_index += 1

    def get_parent_child_relationships(self):
        """
        Retrieve parent-child relationships from the nested set model.

        Returns:
        - List of dictionaries representing parent-child relationships.
        """
        relationships = []

        for node_data in self.tree_structure:
            node = node_data['node']
            parent = node.get('parent')

            if parent is not None:
                relationships.append({
                    'parent': parent,
                    'child': node,
                })

        return relationships

if __name__ == "__main__":
    # Example hierarchical data
    hierarchical_data = [
        {'name': 'Root', 'children': [
            {'name': 'Node 1', 'children': [
                {'name': 'Node 1.1'},
                {'name': 'Node 1.2'},
            ]},
            {'name': 'Node 2'},
            {'name': 'Node 3', 'children': [
                {'name': 'Node 3.1'},
            ]},
        ]},
    ]

    nested_set_model = NestedSetModel()
    nested_set_model.convert_to_nested_set(hierarchical_data)

    # Retrieve and print parent-child relationships
    relationships = nested_set_model.get_parent_child_relationships()
    for rel in relationships:
        print(f"Parent: {rel['parent']}, Child: {rel['child']}")