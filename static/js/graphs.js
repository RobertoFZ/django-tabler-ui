document.addEventListener("DOMContentLoaded", function () {
  const graphs = $("[data-lines]");

  if (graphs.length > 0) {
    $.each(graphs, (i, element) => {
      const lines = $(element).data("lines");
      const titles = $(element).data("titles").split(',');
      const series = [];

      lines.forEach((line, index) => {
        series.push({
          name: titles[index],
          data: Object.keys(line).reduce((accumulator, value) => {
            accumulator.push(line[value])
            return accumulator
          }, [])
        })
      });
      const labels = lines.length ? Object.keys(lines[0]) : [];

      window.ApexCharts &&
        new ApexCharts(element, {
          chart: {
            type: "line",
            fontFamily: "inherit",
            height: 240,
            parentHeightOffset: 0,
            toolbar: {
              show: false,
            },
            animations: {
              enabled: false,
            },
          },
          fill: {
            opacity: 1,
          },
          stroke: {
            width: 2,
            lineCap: "round",
            curve: "straight",
          },
          series: series,
          grid: {
            padding: {
              top: -20,
              right: 0,
              left: -4,
              bottom: -4,
            },
            strokeDashArray: 4,
          },
          xaxis: {
            labels: {
              padding: 0,
            },
            tooltip: {
              enabled: false,
            },
            type: "datetime",
            categories: labels
          },
          yaxis: {
            labels: {
              padding: 4,
              formatter: (value) => value ? parseFloat(value.toFixed(2)) : value,
            },
          },
          colors: ["#ff922b", "#206bc4", "#5eba00"],
          legend: {
            show: true,
            position: 'bottom',
            offsetY: 12,
            markers: {
              width: 10,
              height: 10,
              radius: 100,
            },
            itemMargin: {
              horizontal: 8,
              vertical: 8
            },
          },
        }).render();
    });
  }
});