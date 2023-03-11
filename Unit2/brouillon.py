import numpy as np

# compute Risk function

def hinge_loss(z):
	if z >= 1:
		return 0
	else :
		return 1-z

def squared_loss(z):
	return z**2/2

def R_n(loss,theta,X,Y):
	n = len(X)
	return 1/n * sum( [ loss(Y[i]-np.dot(theta.transpose(),X[i])) for i in range(n)] )


def main_R():
	# parameters
	theta = np.array([0,1,2])
	X= np.array([[1,0,1], [1,1,1], [1,1,-1], [-1,1,1]])
	Y = np.array([2, 2.7, -0.7, 2])
	loss = suared_loss
	
	# computing
	R = R_n(loss,theta, X, Y)
	print(R)
	return None

def squarred_error(Y,X):
	n, m = Y.shape
	S = 0
	for a in range(n) :
		for i in range(m) :
			if Y[a,i] != None :
				S += (Y[a,i] - X[a,i])**2
	return S/2

def collaborating_filtering():
	U = np.array([6,0,3,6])
	V = np.array([4,2,1])
	X = np.array([[24,12,6], [0,0,0], [12,6,3], [24,12,6]])
	Y = np.array([[5, None, 7], [None, 2, None], [4, None, None], [None, 3, 6]])
	print()
	return None

def regul(U,V,l):
	return l/2*(np.sum(np.square(U))+np.sum(np.square(V)))

def compute_J()
	U = np.array([6,0,3,6])
	V = np.array([4,2,1])
	X = np.array([[24,12,6], [0,0,0], [12,6,3], [24,12,6]])
	Y = np.array([[5, None, 7], [None, 2, None], [4, None, None], [None, 3, 6]])
	S = squarred_error(Y,X)
	print("S=",S)
	R = regul(U,V,1)
	print("R=",R)
	return None

if __name__ == "__main__":
	
