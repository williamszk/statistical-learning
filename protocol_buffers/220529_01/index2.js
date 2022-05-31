const Schema = require("./employees_pb");
const fs = require("fs");

const hussein = new Schema.Employee();
hussein.setId(1001);
hussein.setName("Hussein");
hussein.setSalary(1000);

console.log("My name is " + hussein.getName());

const ahmed = new Schema.Employee();
ahmed.setId(1002);
ahmed.setName("Ahmed");
ahmed.setSalary(5000);

console.log("My name is " + ahmed.getName());

const rick = new Schema.Employee();
rick.setId(1003);
rick.setName("Rick");
rick.setSalary(95000);

console.log("My name is " + rick.getName());

const employees = new Schema.Employees();
employees.addEmployees(rick);
employees.addEmployees(ahmed);
employees.addEmployees(hussein);

console.log("binary: " + employees.serializeBinary());
// write serialized bytes to disk
const employeesbinary = employees.serializeBinary();
fs.writeFileSync("employeesbinary", employeesbinary);
// what is the size of the binary file?
// 52 bytes

// deserialize data
const employees2 = Schema.Employees.deserializeBinary(employeesbinary);
// we can consider to use protobuf as a storage mechanism

console.log("employees2: " + employees2.toString());
// To be able to cosume the binary again, we would need to know which was the class
// that generated that protobuf binary


