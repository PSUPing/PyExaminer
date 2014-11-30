from couchbase import Couchbase
import joblib

#import numpy as np

bucket_name = 'examiner_data'
host_name = '192.168.100.17'

def get_run_data(design_doc, view_name, x_npy_file, y_npy_file, trn_run=False):
    cb = Couchbase.connect(bucket=bucket_name,  host=host_name)

    rows = cb.query(design_doc, view_name)

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

        if trn_run == True:
            y.append(0)

        count = count + 1

    x.remove([0, 0, 0, 0, 0, 0, 0, 0])
    y.remove(15)

    joblib.dump(x, x_npy_file)
    joblib.dump(y, y_npy_file)

    return count


def get_mult_runs_data(design_doc, view_names, x_npy_file, y_npy_file):
    cb = Couchbase.connect(bucket=bucket_name,  host=host_name)

    x = [[0, 0, 0, 0, 0, 0, 0, 0]]

    for view_name in view_names:
        rows = cb.query(design_doc, view_name)

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

            print view_name + ' count: ' + `count`

    x.remove([0, 0, 0, 0, 0, 0, 0, 0])

    joblib.dump(x, x_npy_file)

# "no_virus_trn_x.npy"
# "no_virus_trn_y.npy"

# cb = Couchbase.connect(bucket='examiner_data',  host='192.168.100.17')
#
# ###### No Virus Training Run ##########################
#
# rows = cb.query("get", "no_virus_trn")
#
# x = [[0, 0, 0, 0, 0, 0, 0, 0]]
# y = [15]
#
# count = 0
# for row in rows:
# 	x.append([row.value[1]['thread_alloc_count'],
# 			  row.value[1]['proc_count'],
# 			  row.value[1]['thread_alloc_size'],
#
# 			  row.value[2]['mem_free'],
# 			  row.value[2]['native_allocated_heap'],
# 			  row.value[2]['native_free_heap'],
# 			  row.value[2]['mem_total'],
# 			  row.value[2]['native_heap'],
#
# 			  row.value[3]['global_class_init'],
# 			  row.value[3]['classes_loaded'],
# 			  row.value[3]['total_methods_invoc'],
#
# 			  row.value[4]['total_tx'],
# 			  row.value[4]['total_rx']])
#     y.append(0)
#
# 	count = count + 1
#
# x.remove([0, 0, 0, 0, 0, 0, 0, 0])
# y.remove(15)
#
# joblib.dump(x, "no_virus_trn_x.npy")
# joblib.dump(y, "no_virus_trn_y.npy")
#
# print 'Fitting Run - No Virus: ' + `count`
#
# ###### Anserver Bot ##########################
#
# rows = cb.query("get", "anserver")
#
# x = [[0, 0, 0, 0, 0, 0, 0, 0]]
# y = [15]
#
# count = 0
# for row in rows:
# 	x.append([row.value[1]['thread_alloc_count'],
# 			  row.value[1]['proc_count'],
# 			  row.value[1]['thread_alloc_size'],
#
# 			  row.value[2]['mem_free'],
# 			  row.value[2]['native_allocated_heap'],
# 			  row.value[2]['native_free_heap'],
# 			  row.value[2]['mem_total'],
# 			  row.value[2]['native_heap'],
#
# 			  row.value[3]['global_class_init'],
# 			  row.value[3]['classes_loaded'],
# 			  row.value[3]['total_methods_invoc'],
#
# 			  row.value[4]['total_tx'],
# 			  row.value[4]['total_rx']])
#     y.append(0)
#
# 	count = count + 1
#
# x.remove([0, 0, 0, 0, 0, 0, 0, 0])
# y.remove(15)
#
# joblib.dump(x, "no_virus_trn_x.npy")
# joblib.dump(y, "no_virus_trn_y.npy")
#
# print 'Fitting Run - No Virus: ' + `count`
#
#
#
# ###### Virus 2 ######################################
#
# rows = cb.query("get", "virus2_cpu_mem")
#
# x = [[0, 0, 0, 0, 0, 0, 0, 0]]
#
# count = 0
# for row in rows:
# 	x.append([row.value[1]['thread_alloc_count'],
# 			  row.value[1]['proc_count'],
# 			  row.value[1]['thread_alloc_size'],
#
# 			  row.value[2]['mem_free'],
# 			  row.value[2]['native_allocated_heap'],
# 			  row.value[2]['native_free_heap'],
# 			  row.value[2]['mem_total'],
# 			  row.value[2]['native_heap']])
# 	count = count + 1
#
# x.remove([0, 0, 0, 0, 0, 0, 0, 0])
#
# joblib.dump(x, "virus2_cpu_mem_x.npy")
#
# print 'Virus 2 - CPU / MEM: ' + `count`
#
# rows = cb.query("get", "virus2_cpu_mem_dvm")
#
# x = [[0, 0, 0, 0, 0, 0, 0, 0]]
#
# count = 0
# for row in rows:
# 	x.append([row.value[1]['thread_alloc_count'],
# 			  row.value[1]['proc_count'],
# 			  row.value[1]['thread_alloc_size'],
#
# 			  row.value[2]['mem_free'],
# 			  row.value[2]['native_allocated_heap'],
# 			  row.value[2]['native_free_heap'],
# 			  row.value[2]['mem_total'],
# 			  row.value[2]['native_heap'],
#
# 			  row.value[3]['global_class_init'],
# 			  row.value[3]['classes_loaded'],
# 			  row.value[3]['total_methods_invoc']])
# 	count = count + 1
#
# x.remove([0, 0, 0, 0, 0, 0, 0, 0])
#
# joblib.dump(x, "virus2_cpu_mem_dvm_x.npy")
#
# print 'Virus 2 - CPU / MEM / DVM: ' + `count`
#
# rows = cb.query("get", "virus2_all")
#
# x = [[0, 0, 0, 0, 0, 0, 0, 0]]
#
# count = 0
# for row in rows:
# 	x.append([row.value[1]['thread_alloc_count'],
# 			  row.value[1]['proc_count'],
# 			  row.value[1]['thread_alloc_size'],
#
# 			  row.value[2]['mem_free'],
# 			  row.value[2]['native_allocated_heap'],
# 			  row.value[2]['native_free_heap'],
# 			  row.value[2]['mem_total'],
# 			  row.value[2]['native_heap'],
#
# 			  row.value[3]['global_class_init'],
# 			  row.value[3]['classes_loaded'],
# 			  row.value[3]['total_methods_invoc'],
#
# 			  row.value[4]['total_tx'],
# 			  row.value[4]['total_rx']])
# 	count = count + 1
#
# x.remove([0, 0, 0, 0, 0, 0, 0, 0])
#
# joblib.dump(x, "virus2_all_x.npy")
#
# print 'Virus 2 - All: ' + `count`
