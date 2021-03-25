import pulp

# Define the problem
prob = pulp.LpProblem("The Brewery Problem", pulp.LpMinimize)

# Define the variables, MINIMUM ZERO
x1 = pulp.LpVariable("Beer", 0)
x2 = pulp.LpVariable("Ale", 0, cat="Continuous")

# Objective function (NEGATIVE PRODUCTS)
prob += -(23*x1 + 13*x2)

# Constraints
prob += 15*x1 +  5*x2 <=  480, "Corn availability"
prob +=  4*x1 +  4*x2 <=  160, "Hops availability"
prob += 20*x1 + 35*x2 <= 1190, "Malt availability"

# Write the problem on an .lp file
prob.writeLP("Brewery.lp")

# Solve --> prob.solve() AUTOMATIC SOLVER, or instead
prob.solve(pulp.PULP_CBC_CMD(fracGap = 1e-5, maxSeconds = 500, threads = None))

# Status of the solution
print("Status: ", pulp.LpStatus[prob.status])

# Optimal value of objective function
print("Total revenue = ", -1*pulp.value(prob.objective))

# Optimal value of variables
for v in prob.variables():
    print(v.name, " = ", v.varValue)
