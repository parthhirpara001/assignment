"""Write a Python program to combine values in python list of dictionaries.
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':
300}, o {'item': 'item1', 'amount': 750}]
Expected Output:
Counter ({'item1': 1150, 'item2': 300})"""



data = [{'item': 'item1', 'amount': 400},
        {'item': 'item2', 'amount': 300}, 
         {'item': 'item1', 'amount': 750}]

combined_values = {}
for d in data:
    item = d['item']
    amount = d.get('amount', 0)
    combined_values[item] = combined_values.get(item, 0) + amount

print("Combined values:", combined_values)