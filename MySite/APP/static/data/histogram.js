$(function(){
    $('#container').highcharts({
        data: {
          table: 'datatable'
        },

        chart: {
            type: 'column'
        },

        title: {
            text: '成绩分布'
        },

        yAxis: {
            allowDecimals: true,
            title:{
                text: "分数",
                rotation: 0
            }
        },

        plotOptions: {
            column: {
                pointPadding: 0.2,
                borderWidth: 0,
                pointWidth: 30
            }
        },

        tooltip: {
            formatter: function () {
                return this.point.name.toLowerCase() + ": " + this.point.y + "分";
            }
        }
    });

});