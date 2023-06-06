import time    

def ft_tqdm(lst: range) -> None:
    size = len(lst)
    start_time = time.time()
    progress = 0

    for item in lst:
        yield item
        progress += 1
        elapsed_time = time.time() - start_time
        percentage = (progress / size) * 100
        bar_length = 80
        filled_length = int(bar_length * (percentage / 100))
        bar = '#' * filled_length + ' ' * (bar_length - filled_length)
        it_per_second = progress / elapsed_time
        print(f"{percentage:.0f}% |{bar} |{progress}/{size}, [{elapsed_time:.2f}s, {it_per_second:.2f}it/s]", end="\r")
    print()
