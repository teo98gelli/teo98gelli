#Import csv from Italian standard finacial statement (download from creditsafe.com/it) and outputs main KPIs
import csv

def main():
    bilancio = read_csv(input("Which file? "))
    pri(bilancio, KPIs(bilancio))

def read_csv(filename):
    #Import from CSV
    bilancio = []
    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            bilancio.append({
                "VOCI DI BILANCIO": row["VOCI DI BILANCIO"],
                "31-12-2022": row["31-12-2022"],
                "31-12-2021": row["31-12-2021"],
                "NOTE": row["NOTE"],
                "NOME TAG XBRL": row["NOME TAG XBRL"]})

    return bilancio

def KPIs(bilancio):
    #Calculate main KPIs
    if (int(dict.get(bilancio[213], "31-12-2022"))<0 or int(dict.get(bilancio[213], "31-12-2022")) < 0):
        EBIT_perc = "N/A"
    else:
        EBIT_perc = (int(dict.get(bilancio[213], "31-12-2022")) - int(dict.get(bilancio[213], "31-12-2021")))/int(dict.get(bilancio[213], "31-12-2021"))

    KPIs = {
    "Revenue_year": (dict.get(bilancio[193], "31-12-2022")),
    "Revenue_past_year": (dict.get(bilancio[193], "31-12-2021")),
    "Revenue_growth": str((int(dict.get(bilancio[193], "31-12-2022")) - int(dict.get(bilancio[193], "31-12-2021")))/int(dict.get(bilancio[193], "31-12-2021"))),
    "EBIT_year": (dict.get(bilancio[213], "31-12-2022")),
    "EBIT_past_year": (dict.get(bilancio[213], "31-12-2021")),
    "EBIT_perc": str(EBIT_perc)
    }

    return KPIs

def pri(bilancio, kpis):
    print(dict.get(bilancio[0], "31-12-2022"))
    for key, value in kpis.items():
        print(key, ":", value)

if __name__ == "__main__":
    main()