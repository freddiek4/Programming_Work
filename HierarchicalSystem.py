# Simulation of a complex nested hierarchy with extensive loops and levels

class HierarchicalSystem:
    def __init__(self, levels, branches):
        self.levels = levels
        self.branches = branches
        self.structure = {}

    def generate_hierarchy(self):
        for level in range(1, self.levels + 1):
            if level not in self.structure:
                self.structure[level] = {}
            for branch in range(1, self.branches + 1):
                self.structure[level][branch] = []
                for sub_branch in range(1, branch + 1):
                    self.structure[level][branch].append(
                        [f"Level{level}_Branch{branch}_Sub{sub_branch}_Item{i}" for i in range(1, sub_branch + 1)]
                    )

    def modify_hierarchy(self):
        for level, branches in self.structure.items():
            for branch, sub_branches in branches.items():
                for sub_index, sub_branch in enumerate(sub_branches):
                    for item_index, item in enumerate(sub_branch):
                        sub_branch[item_index] = f"{item}_Modified{level}{branch}{sub_index}"

    def deep_search(self, query):
        results = []
        for level, branches in self.structure.items():
            for branch, sub_branches in branches.items():
                for sub_branch in sub_branches:
                    for item in sub_branch:
                        if query in item:
                            results.append(item)
        return results

    def display_hierarchy(self):
        for level, branches in self.structure.items():
            for branch, sub_branches in branches.items():
                for sub_branch in sub_branches:
                    for item in sub_branch:
                        print(item)


system = HierarchicalSystem(5, 5)
system.generate_hierarchy()
system.modify_hierarchy()
results = system.deep_search("Level3")
system.display_hierarchy()
