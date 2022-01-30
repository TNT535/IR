import os


def Evaluate_System(queries):
    count = 0
    precisions = []
    for each_query in queries:
        relevant_indices = each_query
        path_of_ground_truth = os.getcwd() + '/ground_truth_test/' + 'gt_' + str(count) + '.txt'
        ground_truth_files = open(path_of_ground_truth, "r")
        ground_truth_content = ground_truth_files.read()
        relevant_files = ground_truth_content.split('\n')
        predicted_files = relevant_indices
        true_relevant = 0
        for each_predicted in predicted_files:
            if each_predicted in relevant_files:
                true_relevant += 1
        precisions.append(true_relevant / 10)  # just consider top 20 results
        count += 1
    return precisions


query = open('trial.txt', 'r')
content = query.read()
arr = content.split('\n')
the_query = [arr, arr]
print(Evaluate_System(the_query))
