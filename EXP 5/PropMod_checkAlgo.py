import re

class Literal:
    def __init__(self, name, sign=True):
        self.name = str(name)
        self.sign = sign

    def __neg__(self):
        return Literal(self.name, False)

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        if self.sign:
            return '%r' % str(self.__str__())
        else:
            return '%r' % str("-" + self.__str__())

def CNFconvert(KB):
    storage = []
    for i in KB:
        i = list(i)
        for j in i:
            j = str(j)
            storage.append(i)
    return storage

def VariableSet(KB):
    KB = eval((CNFconvert(KB).__str__()))
    storage = []
    for obj in KB:
        for item in obj:
            if item[0] == '-' and item[1:] not in storage:
                storage.append(str(item[1:]))
            elif item not in storage and item[0] != '-':
                storage.append(str(item))
    return storage

def Negativeofx(x):
    check = re.match("-", str(x))
    if check:
        return str(x[1:])
    else:
        return "-" + str(x)

def pickX(literals, varList):
    for x in varList:
        if x not in literals:
            break
    return x

def splitFalseLiterals(cnf, x):
    holder = []
    for item in cnf:
        if x in item:
            item.remove(x)
        holder.append(item)
    return holder

def splitTrueLiteral(cnf, x):
    holder = []
    for item in cnf:
        if x in item:
            continue
        else:
            holder.append(item)
    return holder

def unitResolution(clauses):
    literalholder = {}
    i = 0
    while i < len(clauses):
        newClauses = []
        clause = clauses[i]
        if len(clause) == 1:
            literal = str(clause[0])
            pattern = re.match("-", literal)
            if pattern:
                nx = literal[1:]
                literalholder[nx] = False
            else:
                nx = "-" + literal
                literalholder[literal] = True
            for item in clauses:
                if item != clauses[i]:
                    if nx in item:
                        item.remove(nx)
                    newClauses.append(item)
            i = 0
            clauses = newClauses
        else:
            i += 1
    return literalholder, clauses

def dpll(clauses, varList):
    literals, cnf = unitResolution(clauses)
    if cnf == []:
        return literals
    elif [] in cnf:
        return "notsatisfiable"
    else:
        while True:
            x = pickX(literals, varList)
            x = str(x)
            nx = Negativeofx(x)
            ncnf = splitTrueLiteral(cnf, x)
            ncnf = splitFalseLiterals(ncnf, nx)
            if ncnf == cnf:
                varList.remove(x)
            else:
                break
        case1 = dpll(ncnf, varList)
        if case1 != "notsatisfiable":
            copy = case1.copy()
            copy.update(literals)
            copy.update({x: True})
            return copy
        case1 = dpll(ncnf, varList)
        if not case1:
            copy = case1.copy()
            copy.update(literals)
            copy.update({x: False})
            return copy
        else:
            return "notsatisfiable"

def DPLL(KB):
    KB = eval((CNFconvert(KB).__str__()))
    varList = VariableSet(KB)
    result = dpll(KB, varList)
    if result == 'notsatisfiable':
        False
    else:
        for i in varList:
            if i in result and result[i] == True:
                result[i] = 'true'
            elif i in result and result[i] == False:
                result[i] = 'false'
            else:
                result[i] = 'free'
        return [True, result]

A = Literal('A')
B = Literal('B')
C = Literal('C')
D = Literal('D')
KB = [{A, B}, {A, -C}, {-A, B, D}]
print(DPLL(KB))
