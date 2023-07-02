import copy

class Lambda:
  def __init__(self,expr):
    self.expr=expr
  
  def __repr__(self):
    return f"l:{{{self.expr}}}"


def parseArgs(expr):
  if len(expr)==0:
    return Lambda([0])
  expr[0]=parseLambda(expr[0])
  for i in range(1,len(expr)):
    if len(expr[i])<=1:
      expr[i]=parseLambda(expr[i])
    else:
      expr[i]=parseArgs(expr[i])
  return expr

def mergeEmpty(expr):
  for e in range(0,len(expr)):
    expr[e]=mergeEmpty(expr[e])
    if len(expr[e])==0:
      expr[e]=0
    elif len(expr[e])==1 and isinstance(expr[e][0],int):
      expr[e]=expr[e][0]+1
  return expr

def parseLambda(expr):
  expr=mergeEmpty(expr)
  if len(expr)==0:
    expr=[0]
  return Lambda(expr)

def parse(code):
  expr=[[]]
  for i in range(0,len(code)):
    if code[i] in '(':
      expr.append([])
    elif code[i] in ')':
      prev=expr.pop()
      if len(expr)==0:
        raise Exception("unexpected closing parenthesis")
      expr[-1].append(prev)
  if len(expr)>1:
    raise Exception("missing closing parenthesis")
  expr=expr[0]
  expr[0]=parseLambda(expr[0])
  for i in range(1,len(expr)):
    expr[i]=parseArgs(expr[i])
  return expr

## use dummy variable + evaluation with identity at to write expressions with a single variable in the function body

def evaluateLambda(expr,val):
  for i in range(0,len(expr)):
    if isinstance(expr[i],list):
      expr[i]=evaluateLambda(expr[i],val)
    elif isinstance(expr[i],int):
      expr[i]-=1
      if expr[i]<0:
        expr[i]=Lambda(copy.deepcopy(val.expr))
    elif not isinstance(expr[i],Lambda):
      NotImplemented
  return expr
  
def hasArgument(expr):
  for i in range(0,len(expr)):
    if isinstance(expr[i],list) and hasArgument(expr[i]):
      return True
    elif isinstance(expr[i],int):
      return True
    elif not isinstance(expr[i],Lambda):
      NotImplemented
  return False

def evaluationStep(expr):
  if len(expr)==0:
    return expr ## nothing to evaluate
  if isinstance(expr[0],list):
    expr[0]=evaluationStep(expr[0])
    return expr
  if len(expr)==1:
    return expr[0] ## unwrap single element
  if isinstance(expr[1],list):
    expr[1]=evaluationStep(expr[1])
    return expr
  expr[0].expr=evaluateLambda(expr[0].expr,expr[1])
  if not hasArgument(expr[0].expr):
    expr[0]=expr[0].expr
  expr[1:2]=[]
  return expr
  
