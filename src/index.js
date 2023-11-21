// src/index.js
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import highcharts from 'highcharts';

import Highcharts from 'highcharts';

console.log('Hello from index.js!');

// Dynamic chart logic
function createDynamicChart() {
  // Get chart container and attributes
  const chartContainer = document.getElementById('chartContainer');
  const title = chartContainer.getAttribute('data-chart-title') || 'Dynamic Chart';
  const dataAttribute = chartContainer.getAttribute('data-chart-data');
  const chartData = dataAttribute ? JSON.parse(dataAttribute) : [5, 2, 8, 1];

  // Create Highcharts chart
  Highcharts.chart(chartContainer, {
    title: {
      text: title
    },
    series: [{
      data: chartData
    }]
  });
}

// Trigger the dynamic chart creation
createDynamicChart();