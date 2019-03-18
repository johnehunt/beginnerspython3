import csv


def main():
    print('Starting write of dict CSV example')
    with open('names.csv', 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name', 'result']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'first_name': 'John',
                         'last_name': 'Smith',
                         'result' : 54})
        writer.writerow({'first_name': 'Jane', 'last_name': 'Lewis', 'result' : 63})
        writer.writerow({'first_name': 'Chris', 'last_name': 'Davies', 'result' : 72})

    print('Starting to read dict CSV example')
    with open('names.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for heading in reader.fieldnames:
            print(heading, end=' ')
        print('\n------------------------------')
        for row in reader:
            print(row['first_name'], row['last_name'], row['result'])
    print('Done')


if __name__ == '__main__':
    main()