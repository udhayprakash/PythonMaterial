from collections import Counter, defaultdict
from pprint import pprint

jobs_file = r"C:\Users\Amma\Documents\jobs.txt"

months = Counter()
weeks = Counter()
dates = Counter()
vendor = Counter()
times = Counter()
month_vendor = defaultdict(Counter)
for each_line in open(jobs_file, "r").readlines():
    if each_line.startswith("--END--"):
        break
    if each_line[0].isdigit():
        try:
            each_vendor = each_line.split("IST -")[-1].strip().split("-")[0].strip()
            dates.update([each_line.split()[0]])
            months.update(["-".join(each_line.split()[1:3])])
            weeks.update([each_line.split()[2]])
            vendor.update([each_vendor])
            times.update([each_line.split(")")[1].split("-")[0].strip()])
            curr_month = each_line.split()[1]
            month_vendor[curr_month].update([each_vendor])
        except Exception:
            pass

print("~" * 30)
pprint(months)
print("Monthly Average:", round(sum(list(months.values())) / len(months), 2))
# pprint(weeks)
# pprint(dates)
pprint(vendor)
# pprint(times)

pprint(month_vendor[curr_month])


# keys = [k for k in times.keys() if k < '12:00']\
#     + [k for k in times.keys() if k >= '12:00']

# from matplotlib import pyplot as plt
# plt.bar(keys, times.values(),
#         label="times", width=.5, align='center')

# plt.legend()
# plt.xlabel('Times')
# plt.ylabel('Counts')
# plt.title('Time Distribution')
# plt.show()

# plt.pie(extensions.values(), labels=extensions.keys(),
#         autopct='%1.1f%%', shadow=True, startangle=140)
# plt.axis('equal')
# plt.show()
