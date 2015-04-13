from pastry import node


pastry_node = node.Node (8484, None)
pastry_node.bootstrap ([('127.0.0.1', 8485), ('127.0.0.1', 8486), ('127.0.0.1', 8487)])
