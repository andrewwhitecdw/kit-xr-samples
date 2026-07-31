import ast
import os
import unittest


class TestExtensionShutdown(unittest.TestCase):
    def test_prim_maker_example_is_destroyed(self):
        module_path = os.path.join(
            os.path.dirname(__file__), "..", "omni", "kit", "xr", "samples", "usd_scene_ui",
            "extension.py",
        )
        with open(module_path, "r", encoding="utf-8") as f:
            source = f.read()
        tree = ast.parse(source)
        shutdown = next(
            (node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == "on_shutdown"),
            None,
        )
        self.assertIsNotNone(shutdown, "on_shutdown method not found")
        body = ast.unparse(shutdown)
        self.assertIn("_prim_maker_example.destroy()", body)


if __name__ == "__main__":
    unittest.main()
