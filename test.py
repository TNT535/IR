import os


def Evaluate_System(queries):
    count = 0
    numbers = [5, 3]
    average_precisions = 0
    for each_query in queries:
        relevant_indices = each_query  # Note: Run_Model(each_query)
        path_of_ground_truth = os.getcwd() + '/ground_truth/' + 'gt_' + str(count) + '.txt'
        ground_truth_files = open(path_of_ground_truth, "r")
        ground_truth_content = ground_truth_files.read()
        relevant_files = ground_truth_content.split('\n')
        predicted_files = relevant_indices  # [file_names[index] for index in relevant_indices]
        cur = 1
        true_relevant = 0
        precisions = 0
        for each_predicted in predicted_files:
            if each_predicted in relevant_files:
                true_relevant += 1
                precisions += true_relevant / cur
            cur += 1
        average_precisions += precisions / numbers[count]  # 20  # Because each query was labeled has 20 relevant files
        count += 1
    MAP = average_precisions / 2  # 10 queries were labeled
    return MAP


query = open('trial.txt', 'r')
content = query.read()
arr = content.split('\n')
the_query = [arr, arr]
print(Evaluate_System(the_query))
