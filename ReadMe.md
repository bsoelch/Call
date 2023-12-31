# Call
Call is an implementation of Lambda Calculus using only the symbols `(` and `)`

## Examples

Identity function:
```
()
```

Successor function (`n->g->x->g (n g x)`):
```
((())(()(())((()))))
```


## Usage

run the Python-script in interactive mode:
`python -i callLang.py`

parsing an expression:
`e=parse("<code to be parsed>")`

evaluating in next calculation step for an expression:
`e=evaluationStep(expr)`

## Syntax

Code in call is a balanced sequence of round brackets `(` `)` all other characters will be ignored.

The contents of the first bracket will be parsed a lambda expression.

All successive brackets are function arguments, they will be recursively parsed as sub-expressions.
(First element as lambda-function, all successive elements as arguments)

For example

```
((())(()(())((())))) ( (()(())) () ( (()(())) ) )
```

will be parsed as
```
[Labc.b(a b c)] ( [Lab.ab] [La.a] [Lab.ba] )
```

### Lambda expressions

Like for the parsing of the whole function body any bracket containing more than one element is used for grouping its elements.
The brackets containing only a single element represent the positions of the function arguments within the function body,
the index of the argument is encoded by the nesting depth of the bracket.

For instance `((())(()(())((()))))` will be decoded as `(1 (0 1 2) )` which represents the lambda expression `a->b->c->b(a(b)(c))` or `Labc.b(abc)`

Most Lambda expressions with unused arguments cannot correctly be encoded in a single bracket expression,
they can still be represented by using additional arguments an passing the correct functions as arguments

Example:

```
x->y->x
```
would be encoded as
```
(())
```
which will be interpreted as as `x->x`

It can be encoded as `(a->b->c->a c b) (x->y->y)`

giving the expression `(()((()))(()))(((())))`




