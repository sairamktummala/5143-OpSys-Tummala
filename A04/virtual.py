# sai rama krishna tummala
# 5/7/2019

import time
import random
import sys
import os

import matplotlib.pyplot as plt

def parse_token(token):
    pid, addr = token.split(",")
    return int(pid), int(addr, 16)

def parse_filename(filename):
    filename = os.path.basename(filename)

    args = filename.split(".")[0].split("_")
    assert len(args) == 5

    # s   = args[0]
    # run = args[1]
    np  = args[2]
    vm  = args[3]
    pm  = args[4]

    return int(np), int(vm), int(pm)

def parse_argv(sys_argv):
    assert len(sys_argv) == 2
    assert len(sys_argv[1]) > 10
    assert sys_argv[1][0:10] in ["directory=", "data_file="]
    return sys_argv[1][0:9], sys_argv[1][10:]

def load_references(file_name):
    with open(file_name) as infile:
        token = ""
        while True:
            c = infile.read(1)
            if not c:
                break
            else:
                # read a char
                if c != " ":
                    token += c
                else:
                    pid, addr = parse_token(token)
                    token = ""
                    yield pid, addr

class page_frame(object):
    def __init__(self):
        self.valid_bit = False  # in memory
        self.dirty = False      # updated
        self.last_access = 0    # time stamp
        self.access_count = 0   # sum of accesses

class physical_memory(object):
    def __init__(self, mem_size):
        self.mem_size = mem_size
        self.mem_table = []

class page_table(object):
    physical_memory = None
    def __init__(self, virt_mem_page_count, phys_mem_size):
        self.vm_page_count = virt_mem_page_count
        self.pm_size = phys_mem_size

        self.page_table = {}        # dictionary of page_frames
        for i in range(self.vm_page_count):
            self.page_table[i] = page_frame()
        if page_table.physical_memory == None:
            page_table.physical_memory = physical_memory(self.pm_size)

        self.total_reference = 0
    
    def ref(self, page_number, alg = 'FIFO'):
        if page_number in self.page_table:
            pf = self.page_table[page_number]
            if pf.valid_bit == False:
                if len(self.physical_memory.mem_table) == self.pm_size:
                    # physical memory is full, replace a page
                    if alg == 'FIFO':
                        self.REPLACEMENT_FIFO()
                    elif alg == 'LRU':
                        self.REPLACEMENT_LRU()
                    elif alg == 'LFU':
                        self.REPLACEMENT_LFU()
                    elif alg == 'RAND':
                        self.REPLACEMENT_RANDOM()

                pf.valid_bit = True
                pf.last_access = time.time()
                pf.access_count += 1
                self.physical_memory.mem_table.append(pf)
                self.total_reference += 1
                return True
            else:
                pf.access_count += 1
                pf.last_access = time.time()
                self.total_reference += 1
                return False
    
    def REPLACEMENT_FIFO(self):
        rpf = self.physical_memory.mem_table[0]
        rpf.valid_bit = False
        self.physical_memory.mem_table.remove(rpf)
    
    def REPLACEMENT_LRU(self):
        # rpf = sorted(self.physical_memory.mem_table, key = lambda x : x.last_access)[0]
        rpf = self.physical_memory.mem_table[0]
        for frame in self.physical_memory.mem_table:
            if frame.last_access < rpf.last_access:
                rpf = frame
        rpf.valid_bit = False
        self.physical_memory.mem_table.remove(rpf)
    
    def REPLACEMENT_LFU(self):
        if self.total_reference != 0:
            rpf = sorted(self.physical_memory.mem_table, key = lambda x : (x.access_count / self.total_reference))[0]
        else:
            rpf = sorted(self.physical_memory.mem_table, key = lambda x : (x.access_count / 0.1))[0]
        rpf.valid_bit = False
        self.physical_memory.mem_table.remove(rpf)
    
    def REPLACEMENT_RANDOM(self):
        rpf = self.physical_memory.mem_table[random.randint(0, self.pm_size - 1)]
        rpf.valid_bit = False
        self.physical_memory.mem_table.remove(rpf)

# file_name = "sim_1_5_1024_256.dat"
# np, vm, pm = parse_filename(file_name);

# modes = ['FIFO', 'LRU', 'LFU', 'RAND']

# for mode in modes:
#     result = [0 for _ in range(np)]
#     ptable = page_table(vm, pm)
#     for pid, addr in load_references(file_name):
#         if ptable.ref(addr, mode):
#             result[pid] += 1
#     print(mode, result)

class Simulator(object):
    modes = ['FIFO', 'LRU', 'LFU', 'RAND']
    def __init__(self):
        pass
    
    def run(self, file_name):
        np, vm, pm = parse_filename(file_name)
        print("INPUT FILE:", file_name)
        print("vm_size: {:<8} pm_size: {:<8}".format(vm, pm))
        print("-" * 50)
        plot_datas = []
        MAX_FAULT = -1
        loaded_refs = [x for x in load_references(file_name)]



        for mode in self.modes:
            result = [[] for _ in range(np)]
            ptables = [page_table(vm, pm) for _ in range(np)]
            ref_counter = 0
            plot_data = [[], []]
            for pid, addr in loaded_refs:
                ref_counter += 1
                if ptables[pid].ref(addr, mode):
                    result[pid].append(ref_counter)

                plot_data[0].append(ref_counter)
                plot_data[1].append(sum([len(x) for x in result]))


            print("Algorithm: {}".format(mode))
            for i in range(np):
                print("  {:<5} {}".format("p" + str(i), len(result[i])))
            print("Total fault: {}\n".format(sum([len(x) for x in result])))

            if sum([len(x) for x in result]) > MAX_FAULT:
                MAX_FAULT = sum([len(x) for x in result])
            
            plot_data.append(result)
            plot_datas.append(plot_data)
            page_table.physical_memory = None
        
        for mode in self.modes:
            plot_data = plot_datas[self.modes.index(mode)]
            plt.subplot(2, 2, self.modes.index(mode) + 1)
            plt.plot(plot_data[0], plot_data[1])

            for pid in range(len(plot_data[2])):
                plt.plot([x for x in plot_data[2][pid]], [x for x in range(len(plot_data[2][pid]))])

            plt.axis([0, len(plot_data[0]), 0, MAX_FAULT])
            plt.title("{}, Total = {}".format(mode, sum(len(x) for x in plot_data[2])))
            plt.ylabel('Page Fault')
            plt.xlabel('Time')

        # plt.suptitle("PROCESS_COUNT = {}, VM_SIZE = {}, PM_SIZE = {}".format(np, vm, pm))
        plt.tight_layout()
        # plt.show()
        plt.savefig('{}.png'.format(os.path.basename(file_name).split('.')[0]))
        plt.clf()
        

        print("-" * 50)
        print()

def main():
    input_mode, value = parse_argv(sys.argv)
    
    if input_mode == 'data_file':
        if not os.path.exists(value):
            print("[Error]: File does not exist")
        elif not os.path.isfile(value):
            print("[Error]: Input is not a file")
        else:
            s = Simulator()
            s.run(value)
    elif input_mode == 'directory':
        if not os.path.exists(value):
            print("[Error]: Directory does not exist")
        elif not os.path.isdir(value):
            print("[Error] Input is not a directory")
        else:
            for root, _, files in os.walk(value):
                for filename in sorted(files):
                    s = Simulator()
                    s.run(os.path.join(root, filename))


if __name__ == '__main__':
    main()

