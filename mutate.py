import ast
import astor
import sys
import random
import copy

class ComparisonMutator(ast.NodeTransformer):
    def mutate_comparison(self, node):
        """Mutates comparison operators in an AST node."""
        #print("accessed this line HERE")
        randNum=random.random()
        #print(randNum)
       # print(type(node))
        if randNum < 0.5:  # 50% chance
           # print("RANDOM CHANCE SUCCEED")
          
            if isinstance(node, ast.Compare):
             #   print("\naccessed this line\n")
                for i, op in enumerate(node.ops):
                    if isinstance(op, ast.Eq):
                        node.ops[i] = ast.NotEq()
                    elif isinstance(op, ast.NotEq):
                        node.ops[i] = ast.Eq()
            # Extend with more comparison operator mutations as needed
        #print("return here")
        return self.generic_visit(node)
    
    def visit_Num(self, node):
        #WE CAN GET RID OF THESE PRINT STATMENTS LATER
        print("Visitor sees a number: ", ast.dump(node), " aka ", astor.to_source(node))
        # Note how we never say "node.contents = 481" or anything like
        # that. We do not directly assign to nodes. Intead, the Visitor
        # Pattern hides that information from us. We use the return value
        # of this function and the new node we return is put in place by
        # the library. 
        # Note: some students may want: return ast.Num(n=481) 
        return ast.Num(481)

    def visit_Str(self, node):
        #WE CAN GET RID OF THESE PRINT STATMENTS LATER
        print("Visitor sees a string: ", ast.dump(node), " aka ", astor.to_source(node))
        # Note: some students may want: return ast.Str(s=481)
        return ast.Str("SE")

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
        prev=mutated_tree
        
        #print(type(mutated_tree))
        mutated_tree = mutator_comparison.visit(mutated_tree) # Changed: Call visit method
        ast.fix_missing_locations(mutated_tree)
        
        #print(mutated_tree==prev)
        #mutator_binary_op = addSub()
       # mutated_tree = mutator_binary_op.visit(mutated_tree)  # Changed: Call visit method
        #ast.fix_missing_locations(tree)
        co = compile(mutated_tree, "", "exec")
        #exec(co)
        
        mutated_code = astor.to_source(mutated_tree)
       # print(mutated_code)
        with open("{0}.py".format(i,), "w") as mutant_file:
            mutant_file.write(mutated_code)


if __name__ == "__main__":
    random.seed(0)
   # print("test")
    if len(sys.argv) != 3:
        print("Usage: python mutate.py <source_file.py> <num_mutants>")
        sys.exit(1)

    source_file_path = sys.argv[1]
    number_of_mutants = int(sys.argv[2])
    ast_tree = parse_file_to_AST(source_file_path)
    #print(type(ast_tree))
    apply_mutations_and_generate_files(ast_tree, source_file_path, number_of_mutants)