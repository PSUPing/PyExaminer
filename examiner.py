import cb
import joblib

from sklearn.neighbors import KNeighborsClassifier

#from couchbase import Couchbase
#from sklearn.neural_network import BernoulliRBM
#from sklearn.svm import SVC
#from sklearn.externals import joblib
#import numpy as np

def exec_knn():
    count = cb.get_run_data("get", "no_virus_trn", "no_virus_trn_x.npy", "no_virus_trn.npy", True)
    print 'Training data count: ' + `count`
    run_names = ["anserver", "hipposms", "no_virus", "radardroid"]
    cb.get_mult_runs_data("get", run_names, "mixed_predict_x.npy")

    trn_x = joblib.load("no_virus_trn_x.npy")
    trn_y = joblib.load("no_virus_trn_y.npy")
    pred_x = joblib.load("mixed_predict_x.npy")

    neigh = KNeighborsClassifier(n_neighbors=4)
    neigh.fit(trn_x, trn_y)

    print neigh.predict(pred_x)





# def run_cpu_mem():
#     cb = Couchbase.connect(bucket='examiner',  host='localhost')
#
#     rows = cb.query("get", "fit_cpu_mem")
#
#     x = [[0, 0, 0, 0, 0, 0, 0, 0]]
#     y = [15]
#
#     count = 0
#     for row in rows:
#         x.append([row.value[1]['thread_alloc_count'],
#             row.value[1]['proc_count'],
#             row.value[1]['thread_alloc_size'],
#
#             row.value[2]['mem_free'],
#             row.value[2]['native_allocated_heap'],
#             row.value[2]['native_free_heap'],
#             row.value[2]['mem_total'],
#             row.value[2]['native_heap']])
#         if (row.value[0] == "clean_cpu_mem"):
#             y.append(0)
#         else:
#             y.append(1)
#         count = count + 1
#
#     x.remove([0, 0, 0, 0, 0, 0, 0, 0])
#     y.remove(15)
#
#     rows = cb.query("get", "virus2_cpu_mem")
#
#     z = [[0, 0, 0, 0, 0, 0, 0, 0]]
#
#     count = 0
#     for row in rows:
#         z.append([row.value[1]['thread_alloc_count'],
#             row.value[1]['proc_count'],
#             row.value[1]['thread_alloc_size'],
#
#             row.value[2]['mem_free'],
#             row.value[2]['native_allocated_heap'],
#             row.value[2]['native_free_heap'],
#             row.value[2]['mem_total'],
#             row.value[2]['native_heap']])
#         count = count + 1
#
#     z.remove([0, 0, 0, 0, 0, 0, 0, 0])
#
#     exec_rbm_svc(x, y, z, "fit_cpu_mem")
#
# def run_cpu_mem_dvm():
#     cb = Couchbase.connect(bucket='ex_ml',  host='localhost')
#     rows = cb.query("get", "fit_cpu_mem_dvm")
#
#     x = [[0, 0, 0, 0, 0, 0, 0, 0]]
#     y = [15]
#
#     count = 0
#     for row in rows:
#         x.append([row.value[1]['thread_alloc_count'],
#             row.value[1]['proc_count'],
#             row.value[1]['thread_alloc_size'],
#
#             row.value[2]['mem_free'],
#             row.value[2]['native_allocated_heap'],
#             row.value[2]['native_free_heap'],
#             row.value[2]['mem_total'],
#             row.value[2]['native_heap'],
#
#             row.value[3]['global_class_init'],
#             row.value[3]['classes_loaded'],
#             row.value[3]['total_methods_invoc']])
#
#         if (row.value[0] == "clean_cpu_mem_dvm"):
#             y.append(0)
#         else:
#             y.append(1)
#         count = count + 1
#
#     x.remove([0, 0, 0, 0, 0, 0, 0, 0])
#     y.remove(15)
#
#     rows = cb.query("get", "virus2_cpu_mem_dvm")
#
#     z = [[0, 0, 0, 0, 0, 0, 0, 0]]
#
#     count = 0
#     for row in rows:
#         z.append([row.value[1]['thread_alloc_count'],
#             row.value[1]['proc_count'],
#             row.value[1]['thread_alloc_size'],
#
#             row.value[2]['mem_free'],
#             row.value[2]['native_allocated_heap'],
#             row.value[2]['native_free_heap'],
#             row.value[2]['mem_total'],
#             row.value[2]['native_heap'],
#
#             row.value[3]['global_class_init'],
#             row.value[3]['classes_loaded'],
#             row.value[3]['total_methods_invoc']])
#         count = count + 1
#
#     z.remove([0, 0, 0, 0, 0, 0, 0, 0])
#
#     print 'Fitting Run - CPU / MEM / DVM: ' + `count`
#
#     exec_rbm_svc(x, y, z, "fit_cpu_mem_dvm")
#
# def run_all():
#     cb = Couchbase.connect(bucket='ex_ml',  host='localhost')
#     rows = cb.query("get", "fit_all")
#
#     x = [[0, 0, 0, 0, 0, 0, 0, 0]]
#     y = [15]
#
#     count = 0
#     for row in rows:
#         x.append([row.value[1]['thread_alloc_count'],
#             row.value[1]['proc_count'],
#             row.value[1]['thread_alloc_size'],
#
#             row.value[2]['mem_free'],
#             row.value[2]['native_allocated_heap'],
#             row.value[2]['native_free_heap'],
#             row.value[2]['mem_total'],
#             row.value[2]['native_heap'],
#
#             row.value[3]['global_class_init'],
#             row.value[3]['classes_loaded'],
#             row.value[3]['total_methods_invoc'],
#
#             row.value[4]['total_tx'],
#             row.value[4]['total_rx']])
#         if (row.value[0] == "clean_all"):
#             y.append(0)
#         else:
#             y.append(1)
#         count = count + 1
#
#     x.remove([0, 0, 0, 0, 0, 0, 0, 0])
#     y.remove(15)
#
#     print 'Fitting Run - All: ' + `count`
#
#     rows = cb.query("get", "virus2_all")
#
#     z = [[0, 0, 0, 0, 0, 0, 0, 0]]
#
#     count = 0
#     for row in rows:
#         z.append([row.value[1]['thread_alloc_count'],
#             row.value[1]['proc_count'],
#             row.value[1]['thread_alloc_size'],
#
#             row.value[2]['mem_free'],
#             row.value[2]['native_allocated_heap'],
#             row.value[2]['native_free_heap'],
#             row.value[2]['mem_total'],
#             row.value[2]['native_heap'],
#
#             row.value[3]['global_class_init'],
#             row.value[3]['classes_loaded'],
#             row.value[3]['total_methods_invoc'],
#
#             row.value[4]['total_tx'],
#             row.value[4]['total_rx']])
#         count = count + 1
#
#     z.remove([0, 0, 0, 0, 0, 0, 0, 0])
#
#     print 'Virus 2 - All: ' + `count`
#
#     exec_rbm_svc(x, y, z, "fit_all")
#
# def exec_rbm_svc(x_fit, y_fit, x_virus, run_name):
#     # Tried different learning_rates to no avail.  They produced the same result
#     rbm = BernoulliRBM()  #learning_rate=0.01
#     rbm_fit_x = rbm.fit_transform(x_fit, y_fit)
#     rbm_virus2_x = rbm.transform(x_virus)
#
#     # Tried different C and gamma values to no avail.  They produced the same result
#     svc = SVC()   #C=10.0, gamma=0.001
#     svc.fit(rbm_fit_x, y_fit)
#     virus2_y = svc.predict(rbm_virus2_x)
#
#     correct = 0.0
#     wrong = 0.0
#
#     for y in virus2_y:
#         if y == 1:
#             correct = correct + 1.0
#         else:
#             wrong = wrong + 1.0
#
#     total = correct + wrong
#     pos = correct / total
#     neg = wrong / total
#
#     print run_name + " (correct): " + `correct` + "/" + `total` + " = " + `pos`
#     print run_name + " (wrong): " + `wrong` + "/" + `total` + " = " + `neg`
#
# run_cpu_mem()

#def run_rbm_svc(file_name_x, file_name_y, file_name_vir, out_file_vir, run_name):
#	raw_fit_x = joblib.load(file_name_x)
#	fit_y = joblib.load(file_name_y)
#	raw_virus2_x = joblib.load(file_name_vir)
#
	# Tried different learning_rates to no avail.  They produced the same result
#	rbm = BernoulliRBM()  #learning_rate=0.01
#	rbm_fit_x = rbm.fit_transform(raw_fit_x, fit_y)
#	rbm_virus2_x = rbm.transform(raw_virus2_x)

	# Tried different C and gamma values to no avail.  They produced the same result
#	svc = SVC()   #C=10.0, gamma=0.001
#	svc.fit(rbm_fit_x, fit_y)
#	virus2_y = svc.predict(rbm_virus2_x)



#	joblib.dump(virus2_y, out_file_vir)

#run_rbm_svc("fit_all_x.npy", "fit_all_y.npy", "virus2_all_x.npy", "virus2_all_y.npy", "All")
#run_rbm_svc("fit_cpu_mem_x.npy", "fit_cpu_mem_y.npy", "virus2_cpu_mem_x.npy", "virus2_cpu_mem_y.npy", "CPU / Mem")
#run_rbm_svc("fit_cpu_mem_dvm_x.npy", "fit_cpu_mem_dvm_y.npy", "virus2_cpu_mem_dvm_x.npy", "virus2_cpu_mem_dvm_y.npy", "CPU / Mem / DVM")