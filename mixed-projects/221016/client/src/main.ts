/**
 * This is the client it will send POST requests to the backend with
 * the information about weekly sales from Walmart.
 */
import { parse } from "csv-parse";
import * as fs from "fs";
import * as path from "path";
import { hello } from "./module";

// Store	Date	Weekly_Sales	Holiday_Flag	Temperature	Fuel_Price	CPI	Unemployment
// 0	1	05-02-2010	1643690.90	0	42.31	2.572	211.096358	8.106
// 1	1	12-02-2010	1641957.44	1	38.51	2.548	211.242170	8.106
// 2	1	19-02-2010	1611968.17	0	39.93	2.514	211.289143	8.106
type WeeklySalesReport = {
	Store: number;
	Date: string; // this should be date
	Weekly_Sales: number;
	Holiday_Flag: number;
	Temperature: number;
	Fuel_Price: number;
	CPI: number;
	Unemployment: number;
};

(() => {
	const csvFilePath = path.resolve(
		__dirname,
		"../../original-data/Walmart.csv"
	);
	const headers = [
		"Store",
		"Date",
		"Weekly_Sales",
		"Holiday_Flag",
		"Temperature",
		"Fuel_Price",
		"CPI",
		"Unemployment",
	];

	const fileContent = fs.readFileSync(csvFilePath, { encoding: "utf-8" });

	parse(
		fileContent,
		{
			delimiter: ",",
			columns: headers,
		},
		(error, result: WeeklySalesReport[]) => {
			if (error) {
				console.log(error);
			}
			console.log("Result", result);
		}
	);

	console.log("Hello World");
	console.log(hello("Bob"));
})();
