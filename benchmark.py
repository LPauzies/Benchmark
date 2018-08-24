class Benchmark:
    
    class BenchmarkError(Exception):
        pass
    
    def __init__(self, function, arg_dict):
        self.function = function
        self.func_name = self.function.__name__
        self.args = arg_dict
            
    def run(self, n):
        from datetime import datetime
        if n <= 0:
            raise BenchmarkError("Invalid loop number n is negative or equal to zero")
        print("Launching benchmark of the function {} for {} times".format(self.func_name,n))
        length_n = len(str(n))
        avg_time = 0.0
        start_tot = datetime.now()
        for i in range(0,n):
            n_loop = str(i+1) + ' '*(length_n - len(str(i+1)))
            start = datetime.now()
            try:
                self.function(**self.args)
            except:
                raise BenchmarkError("Invalid use of the function, check the arguments or the function itself")
            time_loop = (datetime.now() - start).total_seconds()
            avg_time += time_loop
            print("#{} : {} s".format(n_loop,time_loop))
        avg_time /= float(n)
        time_benchmark = (datetime.now() - start_tot).total_seconds()
        print("Average time for this function : {} s".format(avg_time))
        print("Total time for this benchmark : {} s".format(time_benchmark))
