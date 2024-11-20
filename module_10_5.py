from datetime import datetime
from multiprocessing.pool import Pool


def read_info(name):
    all_data = []
    with open(name) as file:
        while True:
            line = file.readline().strip()
            if line == '':
                break
            all_data.append(line)


filenames = [f'file {number}.txt' for number in range(1, 5)]

# Линейный вызов
start_time1 = datetime.now()
for f in filenames:
    print(f)
    read_info(f)
end_time1 = datetime.now()
elapsed_time = end_time1 - start_time1
print(f'{elapsed_time} - линейный вызов')

# Многопроцессный вызов
if __name__ == '__main__':
    start_time2 = datetime.now()
    with Pool(4) as pool:
        result = pool.map(read_info, filenames)
    end_time2 = datetime.now()
    elapsed_time = end_time2 - start_time2
    print(f'{elapsed_time} - многопроцессный вызов')
