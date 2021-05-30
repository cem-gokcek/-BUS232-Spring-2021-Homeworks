import csv
import xlsxwriter

if __name__ == '__main__':

    """
       Open .csv File
    """
    with open('IcerikDosyasi.csv', newline='') as f:
        reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        fields = next(reader)
        counter = sumInterest = sumInflation = sumUnEmployment = 1.0

        """
           Open .xlsx File
        """

        workbook = xlsxwriter.Workbook('IcerikDosyasi.xlsx')
        worksheet = workbook.add_worksheet()

        row = column = 0

        for header in fields:
            worksheet.write_string(row, column, header)
            column += 1

        for Year, Interest, Inflation, UnEmployment, in reader:
            counter = 1 + counter
            sumInterest = sumInterest + float(Interest)
            sumInflation = sumInflation + float(Inflation)
            sumUnEmployment = sumUnEmployment + float(UnEmployment)
            row += 1
            worksheet.write_number(row, 1, int(Year))
            worksheet.write_number(row, 2, float(Interest))
            worksheet.write_number(row, 3, float(Inflation))
            worksheet.write_number(row, 4, float(UnEmployment))

        row += 2
        worksheet.write_string(row,0, "Avg:")
        worksheet.write_number(row, 2, sumInterest)
        worksheet.write_number(row, 3, sumInflation)
        worksheet.write_number(row, 4, sumUnEmployment)
        workbook.close()
