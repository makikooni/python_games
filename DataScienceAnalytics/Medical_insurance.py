# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(name,age,sex,bmi,num_of_children,smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500

  print("The estimated insurance cost " + name + " is " + str(estimated_cost) + " dollars.")
  return estimated_cost



# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost("Maria",28,0,26.2,3,0)

# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost("Omar",35,1,22.2,0,1)

# X insurance cost
x_insurance_cost = calculate_insurance_cost("X", 27, 0, 20.7, 0, 1)

