from couchbase import Couchbase
import numpy as np
import joblib
import sys

cb = Couchbase.connect(bucket='ex_ml',  host='localhost')

if (sys.argv[1] == '1'):
	rows = cb.query("get", "fit_cpu_mem")

	for row in rows:
		virus = "true"
		if (row.value[0] == "clean_cpu_mem"):
			virus = "false"
		else: 
			virus = "true"

		print `row.value[1]['thread_alloc_count']` + " " + `row.value[1]['proc_count']` + " " + `row.value[1]['thread_alloc_size']` + " " + `row.value[2]['mem_free']` + " " + `row.value[2]['native_allocated_heap']` + " " + `row.value[2]['native_free_heap']` + " " + `row.value[2]['mem_total']` + " " + `row.value[2]['native_heap']` + " " + virus
elif (sys.argv[1] == '2'):
	rows = cb.query("get", "fit_cpu_mem_dvm")

	for row in rows:
		virus = "true"
		if (row.value[0] == "clean_cpu_mem_dvm"):
			virus = "false"
		else: 
			virus = "true"

		print `row.value[1]['thread_alloc_count']` + " " + `row.value[1]['proc_count']` + " " + `row.value[1]['thread_alloc_size']` + " " + `row.value[2]['mem_free']` + " " + `row.value[2]['native_allocated_heap']` + " " + `row.value[2]['native_free_heap']` + " " + `row.value[2]['mem_total']` + " " + `row.value[2]['native_heap']` + " " + `row.value[3]['global_class_init']` + " " + `row.value[3]['classes_loaded']` + " " + `row.value[3]['total_methods_invoc']` + " " + virus
elif (sys.argv[1] == '3'):
	rows = cb.query("get", "fit_all")

	for row in rows:
		virus = "true"
		if (row.value[0] == "clean_all"):
			virus = "false"
		else: 
			virus = "true"

		print `row.value[1]['thread_alloc_count']` + " " + `row.value[1]['proc_count']` + " " + `row.value[1]['thread_alloc_size']` + " " + `row.value[2]['mem_free']` + " " + `row.value[2]['native_allocated_heap']` + " " + `row.value[2]['native_free_heap']` + " " + `row.value[2]['mem_total']` + " " + `row.value[2]['native_heap']` + " " + `row.value[3]['global_class_init']` + " " + `row.value[3]['classes_loaded']` + " " + `row.value[3]['total_methods_invoc']` + " " + `row.value[4]['total_tx']` + " " + `row.value[4]['total_rx']` + " " + virus
	###### Virus 2 ######################################
elif (sys.argv[1] == '4'):
	rows = cb.query("get", "virus2_cpu_mem")

	for row in rows:
		print `row.value[1]['thread_alloc_count']` + " " + `row.value[1]['proc_count']` + " " + `row.value[1]['thread_alloc_size']` + " " + `row.value[2]['mem_free']` + " " + `row.value[2]['native_allocated_heap']` + " " + `row.value[2]['native_free_heap']` + " " + `row.value[2]['mem_total']` + " " + `row.value[2]['native_heap']`
elif (sys.argv[1] == '5'):
	rows = cb.query("get", "virus2_cpu_mem_dvm")

	for row in rows:
		print `row.value[1]['thread_alloc_count']` + " " + `row.value[1]['proc_count']` + " " + `row.value[1]['thread_alloc_size']` + " " + `row.value[2]['mem_free']` + " " + `row.value[2]['native_allocated_heap']` + " " + `row.value[2]['native_free_heap']` + " " + `row.value[2]['mem_total']` + " " + `row.value[2]['native_heap']` + " " + `row.value[3]['global_class_init']` + " " + `row.value[3]['classes_loaded']` + " " + `row.value[3]['total_methods_invoc']`
elif (sys.argv[1] == '6'):
	rows = cb.query("get", "virus2_all")

	for row in rows:
		print `row.value[1]['thread_alloc_count']` + " " + `row.value[1]['proc_count']` + " " + `row.value[1]['thread_alloc_size']` + " " + `row.value[2]['mem_free']` + " " + `row.value[2]['native_allocated_heap']` + " " + `row.value[2]['native_free_heap']` + " " + `row.value[2]['mem_total']` + " " + `row.value[2]['native_heap']` + " " + `row.value[3]['global_class_init']` + " " + `row.value[3]['classes_loaded']` + " " + `row.value[3]['total_methods_invoc']` + " " + `row.value[4]['total_tx']` + " " + `row.value[4]['total_rx']`