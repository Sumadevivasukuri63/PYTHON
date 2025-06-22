import ast


inp = "[[1,2,3,4] , ['Python','C']]"

required_input = ast.literal_eval(inp)

print(required_input)






# import ast

# code = "x = 2 + 3"
# tree = ast.parse(code)
# print(ast.dump(tree, indent=4))