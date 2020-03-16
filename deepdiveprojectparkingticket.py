filename = "D:/PythonDeepDive/dataset/Project-3-Solution-Goal-1/nyc_parking_tickets_extract.csv"
"""
with open(filename) as f:
    for _ in range(10):
        print(next(f))
"""
with open(filename) as f:
    column_header = next(f).strip('\n').split(',')
    sample_data = next(f).strip('\n').split(',')
print(column_header)
print(sample_data)