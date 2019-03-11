from datetime import datetime

print('Creating file')
file = open('date_file.txt', 'w')
print('Writing date information to file')
todays_date = str(datetime.today())
file.write(todays_date)
print('closing file')
file.close()
print('Done')


