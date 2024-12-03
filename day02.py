# --- Day 2: Red-Nosed Reports ---

def is_safe(report):
    deltas_levels = [report[x] - report[x+1] for x in range(len(report)-1)]
    check_increasing = all((num > 0 and num < 4) for num in deltas_levels)
    check_decreasing = all((num < 0 and num > -4) for num in deltas_levels)
    check_same = deltas_levels.count(0) == 0
    return (check_increasing or check_decreasing) and check_same


with open("input02.txt") as file:
    safe_reports_1, safe_reports_2 = 0, 0
    
    for line in file:
        report = [int(x) for x in line.strip().split()]
        # Part one
        if is_safe(report):
            safe_reports_1 += 1
        else:
            # Part two
            damp_reports = []
            for i in range(len(report)):
                dampened_report = report[:]
                dampened_report.pop(i)
                damp_reports.append(dampened_report)
            if any(is_safe(damped) for damped in damp_reports):
                safe_reports_2 += 1

print(f"Part one answer -->  {safe_reports_1}")
print(f"Part two answer -->  {safe_reports_1 + safe_reports_2}")

    
