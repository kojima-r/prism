#define CXX_COMPILE 
extern "C" {
#include "up/up.h"
#include "up/flags.h"
#include "bprolog.h"
}
#include "eigen/Core"
#include "eigen/LU"
#include <iostream>

using namespace Eigen;

// need to declare this function before
double bpx_get_float(TERM t);
extern "C"
int pc_solve_linear_system_4(void) {
	// get arguments
	TERM pr_n, pr_A, pr_b, pr_x;
	pr_n = bpx_get_call_arg(1,4); // first argument: vector size
	pr_A = bpx_get_call_arg(2,4); // second argument: matrix A
	pr_b = bpx_get_call_arg(3,4); // third argument: RHS vector b
	pr_x = bpx_get_call_arg(4,4); // fourth argument: solution x
	
	// transform to c types
	int n = bpx_get_integer(pr_n);
	MatrixXd A = MatrixXd(n,n);
	VectorXd b = VectorXd(n);
	VectorXd x;
	int i, j;
	for(i = 0; i < n; i++) {
		b(i) = bpx_get_float(bpx_get_car(pr_b));
		pr_b = bpx_get_cdr(pr_b);
		for(j = 0; j < n; j++) {
			A(j,i) = bpx_get_float(bpx_get_car(pr_A));
			pr_A = bpx_get_cdr(pr_A);
		}
	}
	FullPivLU< MatrixXd > lu(A);
	x=lu.solve(b);

	// check for correct conversion
	if(exception) {
		return BP_FALSE;
	}

	// transform result back to prolog list
	for(i = 0; i < n; i++) {
		TERM nl = bpx_build_list();
		TERM car = bpx_get_car(nl);
		TERM cdr = bpx_get_cdr(nl);

		bpx_unify(car, bpx_build_float(x(i)));
		bpx_unify(pr_x, nl);
		pr_x = cdr;
	}
	bpx_unify(pr_x, bpx_build_nil());
	// check for correct conversion
	if(exception) {
		return BP_FALSE;
	}
	return BP_TRUE;
}

