import math


class Steps:
    def __init__(self, total_steps, allowed_steps):
        self.symbol_dict_list = []
        self.allowed_steps = allowed_steps
        self.total_steps = total_steps
        self.partition_solutions = [0]

    def get_solutions(self):
        self.symbol_dict_list = []
        self.partition_solutions = [0]*self.total_steps
        print("Total steps: {0}; Allowed steps: {1}".format(self.total_steps, self.allowed_steps))
        self.integer_partition(self.total_steps, self.total_steps, 0)
        number_of_solutions = 0
        for solution in self.symbol_dict_list:
            r_list = [solution[x] for x in solution]
            r = self.naive_multinomial(sum(r_list), r_list)
            number_of_solutions += r
            #print("Solution with steps and number: {0}; number of unique steps: {1}".format(solution, r))
            for dict_item in solution:
                print("\t :: Step length: {0}, number of steps: {1}".format(dict_item, solution[dict_item]))
            print("\t Unique number of steps: {0}".format(r))
            print('\t ----------------------------------------')
        print('Total number of solutions: {0}'.format(number_of_solutions))
        print('\n')

    def integer_partition(self, m, upper_bound, count):
        if m == 0:
            solution_dict = {}
            for part in self.partition_solutions[:count]:
                if part not in self.allowed_steps:
                    return
                if part not in solution_dict:
                    solution_dict[part] = 0
                solution_dict[part] += 1
            self.symbol_dict_list.append(solution_dict)
        else:
            for i in range(1, min(upper_bound, m) + 1):
                self.partition_solutions[count] = i
                self.integer_partition(m - i, i, count + 1)

    @staticmethod
    def naive_multinomial(n, r_list):
        p = 1
        for r in r_list:
            p *= math.factorial(r)
        return int(math.factorial(n)/p)

    def set_allowed_steps(self, new_allowed_steps):
        self.allowed_steps = new_allowed_steps

    def set_total_steps(self, new_total_steps):
        self.total_steps = new_total_steps


step = Steps(6, [1, 2])
step.get_solutions()
step.set_allowed_steps([1, 2])
step.set_total_steps(3)
step.get_solutions()
step.set_total_steps(8)
step.get_solutions()
step.set_allowed_steps([1, 3, 4])
step.get_solutions()
