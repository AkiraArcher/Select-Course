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
            allowDecimals: false,
            title:{
                text: "人数",
                rotation: 0
            }
        },

        tooltip: {
            formatter: function () {
                return this.series.name  + ": " + this.point.y + "人";
            }
        }
    });

});