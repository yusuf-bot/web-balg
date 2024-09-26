# Boolean algebra toolkit

# overview

The website should provide three modes of input

1. expressions (string)
2. truth table / minterms
3. circuit drawing

Each mode of input is on a seperate webpage and has its own functions

# Expresisons

1. expression to truth table

`expr_to_tt(expression)`

2. expression to diagram

`expr_to_dg`

3. expression to expression comparison (assert equality)

`expr_cmp([expressions list])`

4. simplify expression

`expr_simplify`

# Truth table

1. truth table to epxression by:

- take user input for the number of inputs, create a table of n columns and 2**n rows
- provide minters as input to `tt_to_expr`

2. truth table to diagram
`tt_to_dg`

# circuit diagram

1. create diagram using components
- use components to generate an expression (reverse traverse the diagram and create AST)
- same functionality for the inputs above


# Functionality

1. To balg or not to balg?
- Generate everything for each input? if an expression is entered should the diagram, truth table, and simplified expression (in terms of and or not) be calculated automatically?
- This certainly provides a simpler interface, and the overhead is minimal

2. Use frameworks to make our job easier (like tailwind) or raw html and css?

