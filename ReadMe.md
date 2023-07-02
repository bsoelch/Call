# Call
Call is an implementation of Lambda Calculus using only he symbols `(` and `)`

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

```
((())(()(())((())))) ( (()(())) () ( (()(())) ) )
```

### Lambda expressions

Like for the parsing of the whole function body any bracket containing more than one element is used for grouping its elements.
The brackets containing only a single element represent the positions of the function arguments within the function body,
the index of the argument is encoded by the nesting depth of the bracket.

For instance `((())(()(())((()))))` will be decoded as `(1 (0 1 2) )` which represents the lambda expression `Labc.b(abc)` or `a->b->c->b(a(b)(c))`





