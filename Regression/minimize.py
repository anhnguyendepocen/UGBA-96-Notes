def RMSE(alpha, beta):
	x_values = table.column("x") #column of x values to conduct prediction
	actual_y = table.column("actual_y") #column of actual y values
	predicted_y = alpha + beta * x_values #column of predicted y values
	rmse = np.mean((actual_y - predicted_y) ** 2) ** (1/2)
	return rmse