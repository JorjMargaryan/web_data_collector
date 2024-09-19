class SaveFiles:
    def save_as_csv_file(self, outputFilePath, officeData):
        """
            Saves the provided data to a CSV file.
        """
        import csv
        with open(outputFilePath, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Country", "CompanyName", "FullAddress"])
            writer.writerows(officeData)
