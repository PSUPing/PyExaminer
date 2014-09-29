from couchbase import Couchbase
import numpy as np
import joblib

cb = Couchbase.connect(bucket='ex_ml',  host='localhost')

rows = cb.query("get", "fit_cpu_mem")

x = [[0, 0, 0, 0, 0, 0, 0, 0]]
y = [15]

count = 0
for row in rows:
	x.append([row.value[1]['thread_alloc_count'], 
			  row.value[1]['proc_count'],
			  row.value[1]['thread_alloc_size'],

			  row.value[2]['mem_free'],
			  row.value[2]['native_allocated_heap'],
			  row.value[2]['native_free_heap'],
			  row.value[2]['mem_total'],
			  row.value[2]['native_heap']])
	if (row.value[0] == "clean_cpu_mem"):
		y.append(0)
	else: 
		y.append(1)
	count = count + 1

x.remove([0, 0, 0, 0, 0, 0, 0, 0])
y.remove(15)

joblib.dump(x, "fit_cpu_mem_x.npy")
joblib.dump(y, "fit_cpu_mem_y.npy")

print 'Fitting Run - CPU / MEM: ' + `count`

rows = cb.query("get", "fit_cpu_mem_dvm")

x = [[0, 0, 0, 0, 0, 0, 0, 0]]
y = [15]

count = 0
for row in rows:
	x.append([row.value[1]['thread_alloc_count'], 
			  row.value[1]['proc_count'],
			  row.value[1]['thread_alloc_size'],

			  row.value[2]['mem_free'],
			  row.value[2]['native_allocated_heap'],
			  row.value[2]['native_free_heap'],
			  row.value[2]['mem_total'],
			  row.value[2]['native_heap'],

			  row.value[3]['global_class_init'], 
			  row.value[3]['classes_loaded'],
			  row.value[3]['total_methods_invoc']])
	if (row.value[0] == "clean_cpu_mem_dvm"):
		y.append(0)
	else: 
		y.append(1)
	count = count + 1

x.remove([0, 0, 0, 0, 0, 0, 0, 0])
y.remove(15)

joblib.dump(x, "fit_cpu_mem_dvm_x.npy")
joblib.dump(y, "fit_cpu_mem_dvm_y.npy")

print 'Fitting Run - CPU / MEM / DVM: ' + `count`

rows = cb.query("get", "fit_all")

x = [[0, 0, 0, 0, 0, 0, 0, 0]]
y = [15]

count = 0
for row in rows:
	x.append([row.value[1]['thread_alloc_count'], 
			  row.value[1]['proc_count'],
			  row.value[1]['thread_alloc_size'],

			  row.value[2]['mem_free'],
			  row.value[2]['native_allocated_heap'],
			  row.value[2]['native_free_heap'],
			  row.value[2]['mem_total'],
			  row.value[2]['native_heap'],

			  row.value[3]['global_class_init'], 
			  row.value[3]['classes_loaded'],
			  row.value[3]['total_methods_invoc'],

			  row.value[4]['total_tx'], 
			  row.value[4]['total_rx']])
	if (row.value[0] == "clean_all"):
		y.append(0)
	else: 
		y.append(1)
	count = count + 1

x.remove([0, 0, 0, 0, 0, 0, 0, 0])
y.remove(15)

joblib.dump(x, "fit_all_x.npy")
joblib.dump(y, "fit_all_y.npy")

print 'Fitting Run - All: ' + `count`

###### Virus 2 ######################################

rows = cb.query("get", "virus2_cpu_mem")

x = [[0, 0, 0, 0, 0, 0, 0, 0]]

count = 0
for row in rows:
	x.append([row.value[1]['thread_alloc_count'], 
			  row.value[1]['proc_count'],
			  row.value[1]['thread_alloc_size'],

			  row.value[2]['mem_free'],
			  row.value[2]['native_allocated_heap'],
			  row.value[2]['native_free_heap'],
			  row.value[2]['mem_total'],
			  row.value[2]['native_heap']])
	count = count + 1

x.remove([0, 0, 0, 0, 0, 0, 0, 0])

joblib.dump(x, "virus2_cpu_mem_x.npy")

print 'Virus 2 - CPU / MEM: ' + `count`

rows = cb.query("get", "virus2_cpu_mem_dvm")

x = [[0, 0, 0, 0, 0, 0, 0, 0]]

count = 0
for row in rows:
	x.append([row.value[1]['thread_alloc_count'], 
			  row.value[1]['proc_count'],
			  row.value[1]['thread_alloc_size'],

			  row.value[2]['mem_free'],
			  row.value[2]['native_allocated_heap'],
			  row.value[2]['native_free_heap'],
			  row.value[2]['mem_total'],
			  row.value[2]['native_heap'],

			  row.value[3]['global_class_init'], 
			  row.value[3]['classes_loaded'],
			  row.value[3]['total_methods_invoc']])
	count = count + 1

x.remove([0, 0, 0, 0, 0, 0, 0, 0])

joblib.dump(x, "virus2_cpu_mem_dvm_x.npy")

print 'Virus 2 - CPU / MEM / DVM: ' + `count`

rows = cb.query("get", "virus2_all")

x = [[0, 0, 0, 0, 0, 0, 0, 0]]

count = 0
for row in rows:
	x.append([row.value[1]['thread_alloc_count'], 
			  row.value[1]['proc_count'],
			  row.value[1]['thread_alloc_size'],

			  row.value[2]['mem_free'],
			  row.value[2]['native_allocated_heap'],
			  row.value[2]['native_free_heap'],
			  row.value[2]['mem_total'],
			  row.value[2]['native_heap'],

			  row.value[3]['global_class_init'], 
			  row.value[3]['classes_loaded'],
			  row.value[3]['total_methods_invoc'],

			  row.value[4]['total_tx'], 
			  row.value[4]['total_rx']])
	count = count + 1

x.remove([0, 0, 0, 0, 0, 0, 0, 0])

joblib.dump(x, "virus2_all_x.npy")

print 'Virus 2 - All: ' + `count`
