VARIABLES = ["csc", "maths", "phy", "che", "tam", "eng", "bio"]
DOMAIN = ["Monday", "Tuesday", "Wednesday"]
CONSTRAINTS = [
    ("csc", "maths"),
    ("csc", "phy"),
    ("mat", "phy"),
    ("mat", "che"),
    ("mat", "tam"),
    ("phy", "tam"),
    ("phy", "eng"),
    ("che", "eng"),
    ("tam", "eng"),
    ("tam", "bio"),
    ("eng", "bio")
]

def backtrack(assignment):
    if len(assignment) == len(VARIABLES):
        return assignment
    
    var = select_unassigned_variable(assignment)
    for value in DOMAIN:
        if consistent(var, value, assignment):
            assignment[var] = value
            result = backtrack(assignment)
            if result is not None:
                return result
            del assignment[var]
    
    return None

def select_unassigned_variable(assignment):
    for var in VARIABLES:
        if var not in assignment.keys():
            return var

def consistent(var, value, assignment):
    for var1, var2 in CONSTRAINTS:
        if var1 == var or var2 == var:
            for var3, day in assignment.items():
                if (var3 == var2 or var3 == var1) and day == value:
                    return False
    return True

solution = backtrack(dict())
print(solution)
