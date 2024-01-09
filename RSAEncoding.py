import math
"""
Given $p_x=(e,n), s_x=(d,n)$, $p_x(M)=M^e\mod n,s_x(M)=M^d\mod n$ can be computed efficiently with the following algorithm.
Based on the following substructure property (called squaring):

.. math::
    M^e\mod n=\begin{cases}1 & e=0\\M & e=1\\(M^{\lfloor e/2\rfloor})^2\mod n&e>1 \text{ even}\\[(M^{\lfloor e/2\rfloor})^2\cdot M]\mod n&e>1\text{ odd}\end{cases}
"""

# sequential version
def MODEXP(M, x_vec: List[int], n) -> int:
	k = len(x_vec) - 1
	d = 1 # invariant, d=(M^c)mod n when c=0
	for i in range(k, -1, -1):
		d = (d*d) % n # c<-2c: (M^c)*(M^c) mod n = M^(2c) mod n
		if x_vec[i] == 1:
			d = (d*M) % n # c<-c+1: (M^c)*M mod n = M^(c+1) mod n
	return d # d=M^x mod n

# recursive version
def MODPOWER(M,x,n):
	if x==0:
		return 1
	if x==1:
		return M

	temp = MODPOWER(M, math.floor(x/2), n)

	if x%2==0:
		return (temp*temp)%n
	else:
		return (temp*temp*M)%n		