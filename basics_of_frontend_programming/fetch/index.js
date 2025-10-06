const API_URL =
  "https://api.thingspeak.com/channels/3084005/feeds.json?api_key=G4SJQZHMU9FNPTHU&results=2";

google.charts.load("current", { packages: ["corechart"] });
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
  fetch(API_URL)
    .then((response) => response.json())
    .then((data) => {
      const feeds = data.feeds;

      const temperatures = feeds.map((feed) => ({
        time: feed.created_at ? new Date(feed.created_at) : null,
        temperature: feed.field2 ? parseFloat(feed.field2) : null,
      }));

      const dataTable = new google.visualization.DataTable();
      dataTable.addColumn({ type: "datetime", label: "Time" });
      dataTable.addColumn("number", "Temperature");

      temperatures.forEach((temp) => {
        if (
          temp.time instanceof Date &&
          !isNaN(temp.time.getTime()) &&
          temp.temperature !== null &&
          !isNaN(temp.temperature)
        ) {
          dataTable.addRow([temp.time, temp.temperature]);
        }
      });

      const options = {
        title: "Temperature over Time",
        curveType: "function",
        legend: { position: "bottom" },
        vAxis: { title: "Temperature (°C)" },
        hAxis: { title: "Time", format: "HH:mm", gridlines: { count: 6 } },
        backgroundColor: "#ffffff",
        colors: ["red"],
        pointSize: 5,
        lineWidth: 2,
        chartArea: { width: "80%", height: "70%" },
        animation: {
          startup: true,
          duration: 1000,
          easing: "out",
        },
      };
      const chart = new google.visualization.LineChart(
        document.getElementById("output")
      );
      chart.draw(dataTable, options);
    })
    .catch((error) => {
      console.error("Error fetching temperature data:", error);
      document.getElementById("output").textContent = "Error fetching data";
    });
}
