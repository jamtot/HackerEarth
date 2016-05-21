def power_sort(creatures):
    powers = map(int,(raw_input().split()))
    if len(powers) != creatures:
        return "inputs don't match"
    else:
        zombies, vampires = [],[]
        [zombies.append(p) if p%2==0 else vampires.append(p) for p in sorted(powers)]
        print ' '.join(map(str,zombies)), sum(zombies),
        print ' '.join(map(str,vampires)), sum(vampires)

if __name__ == "__main__":
    power_sort(int(raw_input()))
