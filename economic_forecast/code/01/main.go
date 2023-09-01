// This is a script that consumes a piece of data sp500 daily rate since 2013
//
// Build a Go program that reads an excel; divide it into chuck files and
// then save them into another directory; then zip them; then send them to
// another place; an s3 bucket in another aws account; the compute engine
// is different from the storage account; so I need to think about that;

// this is an example of a simple pipeline program
// "read data, transform it, save data"

package main

import (
	"fmt"

	"encoding/csv"
	"io"
	"log"
	"os"

	"github.com/xuri/excelize/v2"
)

func main() {

	fmt.Println("Hello there")

	readFromExcel()
	readFromCsv()
	// TODO: [ ] move data from local to an S3 bucket, from different accounts
	readCsvProcess()

}

type CsvRow struct {
	Date   string
	Close  string
	Volume string
	Open   string
	High   string
	Low    string
}

func readCsvProcess() {

	input_path := "../../data/HistoricalData_1693532045617.csv"

	f, err := os.Open(input_path)
	if err != nil {
		log.Fatal(err)
	}

	// remember to close the file at the end of the program
	defer f.Close()

	csvReader := csv.NewReader(f)
	counter := 0
	var table []CsvRow
	fmt.Println("Example showing the contents of the csv file:")
	for {
		rec, err := csvReader.Read()
		// break with 20 records

		if err == io.EOF || counter == 20 {
			break
		} else {
			counter++
			if counter == 1 {
				continue
			}
		}

		if err != nil {
			log.Fatal(err)
		}
		// do something with read line
		fmt.Printf("%T | %+v\n", rec, rec)
		record := CsvRow{
			Date:   rec[0],
			Close:  rec[1],
			Volume: rec[2],
			Open:   rec[3],
			High:   rec[4],
			Low:    rec[5],
		}
		table = append(table, record)
	}

	for _, item := range table {
		fmt.Printf("%+v\n", item)
	}
	// Date			Close/Last 	Volume 		Open 		High 		Low
	// 08/30/2023	4514.87 	-- 			4500.34 	4521.65 	4493.59
	// 08/29/2023	4497.63 	-- 			4432.75 	4500.14 	4431.68
	// there is no volume information at least in those two lines

}

func readFromCsv() {
	input_path := "../../data/HistoricalData_1693532045617.csv"

	f, err := os.Open(input_path)
	if err != nil {
		log.Fatal(err)
	}

	// remember to close the file at the end of the program
	defer f.Close()

	csvReader := csv.NewReader(f)
	counter := 0
	fmt.Println("Example showing the contents of the csv file:")
	for {
		rec, err := csvReader.Read()
		if err == io.EOF || counter == 20 {
			break
		} else {
			counter++
		}

		if err != nil {
			log.Fatal(err)
		}
		// do something with read line
		fmt.Printf("%+v\n", rec)
	}

	// Date			Close/Last 	Volume 		Open 		High 		Low
	// 08/30/2023	4514.87 	-- 			4500.34 	4521.65 	4493.59
	// 08/29/2023	4497.63 	-- 			4432.75 	4500.14 	4431.68
	// there is no volume information at least in those two lines

}

func readFromExcel() {

	input_path := "../../data/my_excel_file.xlsx"

	f, err := excelize.OpenFile(input_path)
	if err != nil {
		fmt.Println(err)
		return
	}

	// Get value from cell by given sheet name and axis.
	cellValue, err := f.GetCellValue("Sheet1", "B2")
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println("Value from cell B2: ", cellValue)

	// Get all the rows in the sheet.
	rows, err := f.GetRows("Sheet1")
	if err != nil {
		fmt.Println(err)
		return
	}

	// Iterate over the rows and print the cell values.
	fmt.Println("Example showing the contents of the Excel spreadsheet:")
	for _, row := range rows {
		for _, colCell := range row {
			fmt.Print(colCell, "\t")
		}
		fmt.Println()
	}
}
