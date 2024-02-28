import ast
import astor
import sys
import random
import copy
 #total mutants where a change did occur
mutationCount=0 #total number of potential mutants
actionCount=0 # number of changes that occur
maxMutants=1 # number of mutants before we stop making changes  
class ComparisonMutator(ast.NodeTransformer):
   
    def visit_Gt(self, node):
        global mutationCount
        mutationCount+=1
        global actionCount
        global maxMutants
       
        randomNum=random.random()
        if(randomNum>0.95 and actionCount<maxMutants):
            new_node = ast.LtE()
            actionCount+=1
        else:
            new_node=ast.Gt()
        
        node=ast.copy_location(new_node, node)
        self.generic_visit(node)
        return node
    
    def visit_Lt(self, node):
        global mutationCount
        mutationCount+=1
        global actionCount
        global maxMutants
        randomNum=random.random()
        if(randomNum>0.95 and actionCount<maxMutants):
            new_node = ast.GtE()
            actionCount+=1

        else:
            new_node=ast.Lt()
        node=ast.copy_location(new_node, node)
        self.generic_visit(node)
        return node
    
    def visit_LtE(self, node):
        global mutationCount
        mutationCount+=1
        global actionCount
        global maxMutants
        randomNum=random.random()
        #print("called2")
        if(randomNum>0.95 and actionCount<maxMutants):
            new_node = ast.Gt()
            actionCount+=1

        else:
            new_node=ast.LtE()
        
        node=ast.copy_location(new_node, node)
        self.generic_visit(node)
        return node
    
    def visit_GtE(self, node):
        global mutationCount
        mutationCount+=1
        global actionCount
        global maxMutants
        randomNum=random.random()
       # print("called")
        if(randomNum>0.95 and actionCount<maxMutants):
            actionCount+=1

            new_node = ast.Lt()
        else:
            new_node=ast.GtE()
        node=ast.copy_location(new_node, node)
        self.generic_visit(node)
        return node
    def visit_Eq(self, node):
        global mutationCount
        mutationCount+=1
        global actionCount
        global maxMutants
        randomNum=random.random()
       # print("called3")
        if(randomNum>0.95 and actionCount<maxMutants):
            new_node=ast.NotEq()
            actionCount+=1
        else:
            new_node=ast.Eq()

        node=ast.copy_location(new_node, node)
        self.generic_visit(node)
        return node
    def visit_NotEq(self, node):
        global mutationCount
        mutationCount+=1
        global actionCount
        global maxMutants
        randomNum=random.random()
        #doesn't get called
        if(randomNum>0.95 and actionCount<maxMutants):
            
            new_node=ast.Eq()
            actionCount+=1
        else:
            new_node = ast.NotEq()
        node=ast.copy_location(new_node, node)
        self.generic_visit(node)
        return node
    def visit_NotIn(self, node):
        global mutationCount
        mutationCount+=1
        global actionCount
        global maxMutants
        randomNum=random.random()
        #doesn't get called
        print("Not In")
        if(randomNum>0.95 and actionCount<maxMutants):
            actionCount+=1
            new_node = ast.In()
        else:
            new_node=ast.NotIn()
        node=ast.copy_location(new_node, node)
        self.generic_visit(node)
        return node
    def visit_In(self, node):
        randomNum=random.random()
        global mutationCount
        mutationCount+=1
        global actionCount
        global maxMutants
        #print("called7")
        if(randomNum>0.95 and actionCount<maxMutants):
            
            actionCount+=1
            new_node=ast.NotIn()
        else:
            new_node = ast.In()
        node=ast.copy_location(new_node, node)
        self.generic_visit(node)
        return node
    def visit_UAdd(self, node):
        randomNum=random.random()
        global mutationCount
        mutationCount+=1
        global actionCount
        global maxMutants
        
        print("UAdding")
        if(randomNum>0.95 and actionCount<maxMutants):
           
            new_node=ast.USub()
            actionCount+=1
        else:
            new_node = ast.UAdd()
        node=ast.copy_location(new_node, node)
        self.generic_visit(node)
        return node
    def visit_USub(self, node):
        randomNum=random.random()
        global mutationCount
        mutationCount+=1
        global actionCount
        global maxMutants

        if(randomNum>0.95 and actionCount<maxMutants):
            new_node = ast.UAdd()
            actionCount+=1
        else:
            new_node=ast.USub()
        node=ast.copy_location(new_node, node)
        self.generic_visit(node)
        return node
    def visit_Add(self, node):
        randomNum=random.random()
        global mutationCount
        mutationCount+=1
        global actionCount
        global maxMutants

        if(randomNum>0.95 and actionCount<maxMutants):
           
            new_node=ast.Sub()
            actionCount+=1
        else:
             new_node = ast.Add()
        node=ast.copy_location(new_node, node)
        self.generic_visit(node)
        return node
    def visit_Sub(self, node):
        randomNum=random.random()
        global mutationCount
        mutationCount+=1
        global actionCount
        global maxMutants

        if(randomNum>0.95 and actionCount<maxMutants):
            new_node = ast.Add()
            actionCount+=1
        else:
            new_node=ast.Sub()
        node=ast.copy_location(new_node, node)
        self.generic_visit(node)
        return node
    def visit_Mult(self, node):
        randomNum=random.random()
        global mutationCount
        mutationCount+=1
        global actionCount
        global maxMutants

        if(randomNum>0.95 and actionCount<maxMutants):
           # new_node = ast.Mult()
            new_node=ast.Div()
            actionCount+=1
        else:
            new_node = ast.Mult()
        node=ast.copy_location(new_node, node)
        self.generic_visit(node)
        return node
    
    def visit_Div(self, node):
        randomNum=random.random()
        print("Dividing")
        global mutationCount
        mutationCount+=1
        global actionCount
        global maxMutants

        if(randomNum>0.95 and actionCount<maxMutants):
            actionCount+=1
            new_node = ast.Mult()
         
        else:
            new_node=ast.Div()

        node=ast.copy_location(new_node, node)
        self.generic_visit(node)
        return node
    def visit_Pow(self, node):
        randomNum=random.random()
        print("exponentiating")
        global mutationCount
        mutationCount+=1
        global actionCount
        global maxMutants
        if(randomNum>0.95 and actionCount<maxMutants):
         
            new_node=ast.Div()
            actionCount+=1
        else:
            new_node = ast.Pow()
           
        node=ast.copy_location(new_node, node)
        self.generic_visit(node)
        return node
    def visit_FloorDiv(self, node):
        randomNum=random.random()
        print("Floor Dividing")
        global mutationCount
        mutationCount+=1
        global actionCount
        global maxMutants
        if(randomNum>0.95 and actionCount<maxMutants):
           
            new_node=ast.Mult()
            actionCount+=1
        else:
            new_node = ast.FloorDiv()
        node=ast.copy_location(new_node, node)
        self.generic_visit(node)
        return node
    def visit_xpr(self, node):
        randomNum=random.random()
        #print("Assigning")
        #self.generic_visit(node)
        #return node
       # t=isinstance(node.value, ast.Call)
        #print(t)
        #print(node.value)
       # if(t):
           # print("t==true")
           # print(node.value.func)
            #print(isinstance(node.value.func, ast.Name))
        #if isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name) and randomNum >0.95:
            #print("return NOTHING")
            #self.generic_visit(None)
            #return None
            
       # print("return something")
       # self.generic_visit(node)
        #return node
        
 
        
        

   


def parse_file_to_AST(filename):
    """Parses a Python source file to an Abstract Syntax Tree (AST)."""
    with open(filename, "r") as file:
        source_code = file.read()
        tree = ast.parse(source_code, filename=filename)
    return tree



def apply_mutations_and_generate_files(tree, original_filename, num_mutants):
    """Applies mutations to an AST and writes mutated code to new files."""
    global actionCount
    global mutationCount
    for i in range(num_mutants):
        # Make a deep copy of the AST for each mutation to ensure isolation
        mutated_tree = copy.deepcopy(tree)
        actionCount=0
        mutationCount=0
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
        #co = compile(mutated_tree, "", "exec")
        #exec(co)
        
        mutated_code = astor.to_source(mutated_tree)
       # print(mutated_code)
        with open("{0}.py".format(i,), "w") as mutant_file:
            mutant_file.write(mutated_code)


if __name__ == "__main__":
    random.seed(0)
   # print("test")
    if len(sys.argv) != 3:
        print("USAGE: python mutate.py <source_file.py> <num_mutants>")
        sys.exit(1)

    source_file_path = sys.argv[1]
    number_of_mutants = int(sys.argv[2])
    ast_tree = parse_file_to_AST(source_file_path)
    #print(type(ast_tree))
    apply_mutations_and_generate_files(ast_tree, source_file_path, number_of_mutants)