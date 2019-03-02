gem_map = {
        'purple':'Power', 
        'green':'Time', 
        'blue':'Space', 
        'orange':'Soul', 
        'red':'Reality', 
        'yellow':'Mind'
}

for _ in range(int(input())):
    s = input().strip()
    del gem_map[s]
print(len(gem_map))
for i in gem_map: print(gem_map[i])