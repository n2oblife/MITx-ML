import numpy as np 

def train(X,Y,linear=True):
	theta = np.zeros(2)
	theta_0 = 0
	if not(linear):
		for i in range(len(X)):
			error = Y[i]*(np.dot(theta.T,X[i])+theta_0) <= 0 
			print("the ",i,"th point is wrong : ",error)
			if error :
				theta += Y[i]*X[i]
				theta_0 += Y[i]
				print("after the ",i,"th element, theta = ",theta," and theta0 = ",theta_0)
	else :
		for i in range(len(X)):
			error = Y[i]*(np.dot(theta.T,X[i])) <= 0 
			print("the ",i,"th point is wrong : ",error)
			if error :
				theta += Y[i]*X[i]
				print("after the ",i,"th element, theta = ",theta)
	return theta

def perceptron_single_step_update(feature, label, theta, theta0, eps = 0.001):
    if label*(np.dot(theta.T,feature)+theta0) <= eps :
        theta += label*feature
        theta0 += label
    return theta, theta0

def perceptron(features, labels, T, eps=0.001):
    theta = np.zeros(len(features[0]))
    theta0 = 0
    for _ in range(T):
        for i in range(len(features)):
            theta, theta0 = perceptron_single_step_update(features[i], labels[i], theta, theta0)
            print("theta :", theta)
            print("theta0 :", theta0) 
    return theta, theta0

if __name__ == "__main__":
	feature_matrix = [[ 0.09664779, -0.02387948, 0.35999331, 0.19968027, -0.27574433, -0.35533527, 0.27197243, -0.13435124, -0.1672966, -0.37716495], [-0.21401518, -0.38195061, -0.33108094, -0.33071019, 0.20339987, -0.22442748, 0.11518262, 0.38221143, -0.43412436, -0.27066153], [ 0.43541725, -0.20671333, -0.3815415, -0.26638258, -0.32342717, 0.25060658, 0.12976023, 0.35504078, -0.32217407, 0.37317503], [-0.04507523, 0.4360915, -0.23118487, 0.44328081, 0.3908528, 0.22044996, 0.41540964, -0.02958575, 0.04125915, 0.27587476] ,[ 0.33558989, 0.20696928, 0.07009595, -0.18767222, 0.0428848, -0.01218594, -0.16082305, -0.04258495, 0.34239423, 0.36481634]]
	labels = [-1, 1, -1, 1, 1]
	T = 5
	perceptron(feature_matrix, labels, T)
