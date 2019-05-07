# sai rama krishna tummala
# 5/7/2019
# The main purpose of the program is to find page faults for FIFO, LRU, LFU and random replacement and 
# comparing the page faults and plotting them in graphs.


import random



def parse_filename(filename):
    args = filename.split(".")[0].split("_")
    assert len(args) == 5

    s   = args[0]
    run = args[1]
    np  = args[2]
    vm  = args[3]
    pm  = args[4]

    return int(np), int(vm), int(pm)

def parse_token(token):
    pid, addr = token.split(",")
    return int(pid), int(addr, 16)

np, vm, pm = parse_filename(infile)

print(np, vm, pm)

counter = [0 for _ in range(np)]
physical_frame = []
page_access_dict = {}


modes = ['FIFO', 'LRU', 'LFU', 'RANDOM']
mode = modes[1]

print(mode)
ref_counter = 0
with open("./snapshots/" + infile) as infile:
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
                if mode == 'FIFO':
                    # keep a "used order list" , new pages are appended
                    #   to the end and remove from the front. Use physical
                    #   frame list as a FIFO queue.
                    if addr not in physical_frame:
                        counter[pid] += 1
                        if len(physical_frame) == pm:
                            physical_frame.pop(0)
                        physical_frame.append(addr)
                elif mode == 'LRU':
                    # when referenced page is in the physical frame, update
                    #   the access time, aka move it to the back of the queue
                    #   the first frame in physical frame list is the that is
                    #   not referenced for the longest time.
                    if addr not in physical_frame:
                        counter[pid] += 1
                        if len(physical_frame) == pm:
                            physical_frame.pop(0)
                        physical_frame.append(addr)
                    else:
                        physical_frame.remove(addr)
                        physical_frame.append(addr)
                elif mode == 'LFU':
                    # read the instruction for clue on this one
                    if addr not in physical_frame:
                        counter[pid] += 1
                        if len(physical_frame) == pm:
                            # swap
                            # Si = sum(page_access_dict.values())
                            Si = ref_counter
                            # sort based on si / Si
                            sortedpm = sorted(physical_frame, key = lambda x : (page_access_dict[x] / Si))
                            physical_frame.remove(sortedpm[0])
                            if addr not in page_access_dict:
                                page_access_dict[addr] = 0
                            page_access_dict[addr] += 1
                            physical_frame.append(addr)
                        else:
                            # not filled up yet
                            physical_frame.append(addr)
                            if addr not in page_access_dict:
                                page_access_dict[addr] = 0
                            page_access_dict[addr] += 1
                    else:
                        page_access_dict[addr] += 1
                elif mode == 'RANDOM':
                    # randomly select a page in the physical memory 
                    #   and remove it
                    if addr not in physical_frame:
                        counter[pid] += 1
                        if len(physical_frame) == pm:
                            # swap
                            x = random.randint(0, pm - 1)
                            physical_frame.pop(x)
                            physical_frame.append(addr)
                        else:
                            physical_frame.append(addr)
                ref_counter += 1


for i in range(len(counter)):
    print("p{} -> {} fault".format(i, counter[i])),
