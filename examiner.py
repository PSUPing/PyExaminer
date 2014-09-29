from sklearn.externals import joblib
from sklearn.neural_network import BernoulliRBM
from sklearn.svm import SVC
import numpy as np

def run_rbm_svc(file_name_x, file_name_y, file_name_vir, out_file_vir, run_name):
	raw_fit_x = joblib.load(file_name_x)
	fit_y = joblib.load(file_name_y)
	raw_virus2_x = joblib.load(file_name_vir)

	# Tried different learning_rates to no avail.  They produced the same result
	rbm = BernoulliRBM()  #learning_rate=0.01
	rbm_fit_x = rbm.fit_transform(raw_fit_x, fit_y)
	rbm_virus2_x = rbm.transform(raw_virus2_x)

	# Tried different C and gamma values to no avail.  They produced the same result
	svc = SVC()   #C=10.0, gamma=0.001
	svc.fit(rbm_fit_x, fit_y)
	virus2_y = svc.predict(rbm_virus2_x)

	correct = 0.0
	wrong = 0.0

	for y in virus2_y:
		if (y == 1):
			correct = correct + 1.0;
		else:
			wrong = wrong + 1.0

	total = correct + wrong
	pos = correct / total
	neg = wrong / total

	print run_name + " (correct): " + `correct` + "/" + `total` + " = " + `pos`
	print run_name + " (wrong): " + `wrong` + "/" + `total` + " = " + `neg`

	joblib.dump(virus2_y, out_file_vir)

run_rbm_svc("fit_all_x.npy", "fit_all_y.npy", "virus2_all_x.npy", "virus2_all_y.npy", "All")
run_rbm_svc("fit_cpu_mem_x.npy", "fit_cpu_mem_y.npy", "virus2_cpu_mem_x.npy", "virus2_cpu_mem_y.npy", "CPU / Mem")
run_rbm_svc("fit_cpu_mem_dvm_x.npy", "fit_cpu_mem_dvm_y.npy", "virus2_cpu_mem_dvm_x.npy", "virus2_cpu_mem_dvm_y.npy", "CPU / Mem / DVM")