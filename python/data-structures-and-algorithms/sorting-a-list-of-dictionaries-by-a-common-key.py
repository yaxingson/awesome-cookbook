from operator import itemgetter

rows = [
  {'user_id':'1004', 'first_name':'Ralph', 'last_name':'Copeland'},
  {'user_id':'1001', 'first_name':'Adelaide', 'last_name':'Benson'},
  {'user_id':'1005', 'first_name':'Craig', 'last_name':'Greer'},
  {'user_id':'1003', 'first_name':'Clarence', 'last_name':'Lawrence'},
  {'user_id':'1002', 'first_name':'Robert', 'last_name':'Medina'},
]

rows_by_uid = sorted(rows, key=itemgetter('user_id'))

# rows_by_name = sorted(rows, key=lambda r: (r['first_name'], r['last_name']))
rows_by_name = sorted(rows, key=itemgetter('first_name', 'last_name'))

print(rows_by_uid)
print(rows_by_name)
