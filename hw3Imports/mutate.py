import ast
import astor
import sys
import random
import copy

class ComparisonMutator(ast.NodeTransformer):
    def mutate_comparison(self, node):
        """Mutates comparison operators in an AST node."""
        if random.random() < 0.5:  # 50% chance
            if isinstance(node, ast.Compare):
                for i, op in enumerate(node.ops):
                    if isinstance(op, ast.Eq):
                        node.ops[i] = ast.NotEq()
                    elif isinstance(op, ast.NotEq):
                        node.ops[i] = ast.Eq()
            # Extend with more comparison operator mutations as needed
        return self.generic_visit(node)

class addSub(ast.NodeTransformer):
   
    def addSub(self, node):
        """Mutates binary operators in an AST node."""
        randNum=random.random()
        print(randNum)
        if randNum < 0.5:  # 50% chance
            if isinstance(node.op, ast.Add):
                node.op = ast.Sub()
            elif isinstance(node.op, ast.Sub):
                node.op = ast.Add()
            # Extend with more binary operator mutations as needed
        return self.generic_visit(node)

def parse_file_to_AST(filename):
    """Parses a Python source file to an Abstract Syntax Tree (AST)."""
    with open(filename, "r") as file:
        source_code = file.read()
        tree = ast.parse(source_code, filename=filename)
    return tree

def apply_mutations_and_generate_files(tree, original_filename, num_mutants):
    """Applies mutations to an AST and writes mutated code to new files."""
    for i in range(num_mutants):
        # Make a deep copy of the AST for each mutation to ensure isolation
        mutated_tree = copy.deepcopy(tree)
        
        # Apply different types of mutations
        mutator_comparison = ComparisonMutator()
        mutated_tree = mutator_comparison.visit(mutated_tree)  # Changed: Call visit method
        
        mutator_binary_op = addSub()
        mutated_tree = mutator_binary_op.visit(mutated_tree)  # Changed: Call visit method
        
        mutated_code = astor.to_source(mutated_tree)

        with open("{0}.py".format(i,), "w") as mutant_file:
            mutant_file.write(mutated_code)


if __name__ == "__main__":
    random.seed(0)
    if len(sys.argv) != 3:
        print("Usage: python mutate.py <source_file.py> <num_mutants>")
        sys.exit(1)

    source_file_path = sys.argv[1]
    number_of_mutants = int(sys.argv[2])
    ast_tree = parse_file_to_AST(source_file_path)
   
    apply_mutations_and_generate_files(ast_tree, source_file_path, number_of_mutants)