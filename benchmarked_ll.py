import time
# from singly_linked_list import LinkedList

n = 100000

# l = [i for i in range(0, n)]
l = []
# ll = LinkedList()
start_time = time.time()
for i in range(n):
    l.append(i)
end_time = time.time()
print(f"Adding list took {end_time - start_time}")

