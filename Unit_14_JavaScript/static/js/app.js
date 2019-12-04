// from data.js
var tableData = data;

// YOUR CODE HERE!
console.log(tableData);

//Get a reference to the table body
var tbody = d3.select("tbody");

// Refactor to use Arrow Functions!
tableData.forEach((event) => {
    var row = tbody.append("tr");
    Object.values(event).forEach((value) => {
        var cell = row.append("td");
        cell.text(value);
    });
});

var button = d3.select("button");
button.on("click", function () {
    var filterData = tableData
    var input = d3.select("#datetime").property("value");
    if (input !== "") {
        var filterData = filterData.filter(data => data.datetime === input);
    };

    var input = d3.select("#city").property("value");
    if (input !== "") {
        var filterData = filterData.filter(data => data.city === input);
    };

    var input = d3.select("#state").property("value");
    if (input !== "") {
        var filterData = filterData.filter(data => data.state === input);
    };

    var input = d3.select("#country").property("value");
    if (input !== "") {
        var filterData = filterData.filter(data => data.country === input);
    };

    var input = d3.select("#shape").property("value");
    if (input !== "") {
        var filterData = filterData.filter(data => data.shape === input);
    };

    d3.select("tbody").selectAll("tr").remove()
    
    filterData.forEach((event) => {
        var row = tbody.append("tr");
        Object.values(event).forEach((value) => {
            var cell = row.append("td");
            cell.text(value);
        });
    });
});