/**
 * Highcharts-zh_CN plugins v1.0.1 (2017-04-05)
 *
 * (c) 2017 Jianshu Technology co.,LTD (https://jianshukeji.com)
 *
 * Author: john@jianshukeji.com, Blue Monkey
 *
 * License: Creative Commons Attribution (CC)
 */

(function(H) {
  var protocol = window.location.protocol;

  var defaultOptionsZhCn = {
    lang: {
      // Highcharts
      contextButtonTitle: '鍥捐〃瀵煎嚭鑿滃崟',
      decimalPoint: '.',
      downloadJPEG: "瀵煎嚭 JPG 鍥剧墖",
      downloadPDF: "瀵煎嚭 PDF 鏂囨。",
      downloadPNG: "瀵煎嚭 PNG 鍥剧墖",
      downloadSVG: "瀵煎嚭 SVG 鍥剧墖",
      drillUpText: "杩斿洖 {series.name}",
      invalidDate: '鏃犳晥鐨勬椂闂�',
      loading: '鍔犺浇涓�...',
      months: ['涓€鏈�', '浜屾湀', '涓夋湀', '鍥涙湀', '浜旀湀', '鍏湀', '涓冩湀', '鍏湀', '涔濇湀', '鍗佹湀', '鍗佷竴鏈�', '鍗佷簩鏈�'],
      noData: "娌℃湁鏁版嵁",
      numericSymbols: null,
      printChart: "鎵撳嵃鍥捐〃",
      resetZoom: '閲嶇疆缂╂斁姣斾緥',
      resetZoomTitle: '閲嶇疆涓哄師濮嬪ぇ灏�',
      shortMonths: ['涓€鏈�', '浜屾湀', '涓夋湀', '鍥涙湀', '浜旀湀', '鍏湀', '涓冩湀', '鍏湀', '涔濇湀', '鍗佹湀', '鍗佷竴鏈�', '鍗佷簩鏈�'],
      thousandsSep: ',',
      weekdays: ['鏄熸湡涓€', '鏄熸湡浜�', '鏄熸湡涓�', '鏄熸湡鍥�', '鏄熸湡浜�', '鏄熸湡鍏�', '鏄熸湡澶�'],

      // Highstock
      rangeSelectorFrom: '寮€濮嬫椂闂�',
      rangeSelectorTo: '缁撴潫鏃堕棿',
      rangeSelectorZoom: '缂╂斁',

      // Highmaps
      zoomIn: '缂╁皬',
      zoomOut: '鏀惧ぇ'
    },

    global: {
      useUTC: true,
      //timezoneOffset: -8 * 60,
      canvasToolsURL: protocol + '//cdn.hcharts.cn/highcharts/modules/canvas-tools.js',
      VMLRadialGradientURL: protocol + +'//cdn.hcharts.cn/highcharts/gfx/vml-radial-gradient.png'
    },

    title: {
      text: '鍥捐〃鏍囬'
    },

    tooltip: {
      dateTimeLabelFormats: {
        millisecond: '%H:%M:%S.%L',
        second: '%H:%M:%S',
        minute: '%H:%M',
        hour: '%H:%M',
        day: '%Y-%m-%d',
        week: 'Week from %A, %b %e, %Y',
        month: '%Y-%m',
        year: '%Y'
      }
    },

    exporting: {
      url: protocol + '//export.highcharts.com.cn'
    },

    credits: {
      text: 'Highcharts.com.cn',
      href: 'https://www.highcharts.com.cn'
    },
    xAxis: {
      dateTimeLabelFormats: {
        millisecond: '%H:%M:%S.%L',
        second: '%H:%M:%S',
        minute: '%H:%M',
        hour: '%H:%M',
        day: '%Y-%m-%d',
        week: '%e. %b',
        month: '%Y-%m',
        year: '%Y'
      }
    }
  };

  H.setOptions(defaultOptionsZhCn);
}(Highcharts));