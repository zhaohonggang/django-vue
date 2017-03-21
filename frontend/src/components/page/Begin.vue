<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-date"></i> Charts</el-breadcrumb-item>
                <el-breadcrumb-item>Basic Charts</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="plugins-tips">
            vue-echarts-v3：<a href="https://github.com/xlsdg/vue-echarts-v3" target="_blank">vue-echarts-v3</a>
        </div>
        <div class="echarts">
            <IEcharts :option="line" ></IEcharts>
        </div>
        <div class="echarts">
            <IEcharts :option="bar" ></IEcharts>
        </div>
        <div class="echarts">
            <IEcharts :option="pie" ></IEcharts>
        </div>
        <div class="echarts">
            <IEcharts :option="pie_radius" ></IEcharts>
        </div>
    </div>
</template>

<script>
    import IEcharts from 'vue-echarts-v3';
    export default {
        components: {
            IEcharts
        },
        data: () => ({
            line: {
                color:["#20a0ff","#13CE66","#F7BA2A","#FF4949"],
                title: {
                    text: 'Curves'
                },
                xAxis: {
                    data: ["Pork", "Lamb", "Chicken", "Beef", "Fish", "Other"]
                },
                yAxis:{},
                series: [
                    {
                        name: "Sales",
                        type: "line",
                        data: [5, 20, 36, 10, 10, 20]
                    }
                ]
            },
            bar: {
                color:["#20a0ff","#13CE66","#F7BA2A","#FF4949"],
                title: {
                    text: 'Histogram'
                },
                xAxis: {
                    data: ["Pork", "Lamb", "Chicken", "Beef", "Fish", "Other"]
                },
                yAxis:{},
                series: [
                    {
                        name: "Sales",
                        type: "bar",
                        data: [5, 20, 36, 10, 10, 20]
                    }
                ]
            },
            pie: {
                color:["#20a0ff","#13CE66","#F7BA2A","#FF4949","#61a0a8"],
                title : {
                    text: 'Pie',
                    x:'center'
                },
                tooltip : {
                    trigger: 'item',
                    formatter: "{a} <br/>{b} : {c} ({d}%)"
                },
                legend: {
                    orient: 'vertical',
                    left: 'left',
                    data: ["Pork", "Lamb", "Chicken", "Beef", "Fish"]
                },
                series : [
                    {
                        name: 'Sales',
                        type: 'pie',
                        radius : '55%',
                        center: ['50%', '50%'],
                        data:[
                            {value:335, name:'Pork'},
                            {value:310, name:'Lamb'},
                            {value:234, name:'Chicken'},
                            {value:135, name:'Beef'},
                            {value:548, name:'Fish'}
                        ],
                        itemStyle: {
                            emphasis: {
                                shadowBlur: 10,
                                shadowOffsetX: 0,
                                shadowColor: 'rgba(0, 0, 0, 0.5)'
                            }
                        }
                    }
                ]
            },
            pie_radius:{
                color:["#20a0ff","#13CE66","#F7BA2A","#FF4949","#61a0a8"],
                title : {
                    text: 'Circle',
                    x:'center'
                },
                tooltip : {
                    trigger: 'item',
                    formatter: "{a} <br/>{b} : {c} ({d}%)"
                },
                legend: {
                    orient: 'vertical',
                    left: 'left',
                    data: ["Pork", "Lamb", "Chicken", "Beef", "Fish"]
                },
                series : [
                    {
                        name: 'Sales',
                        type: 'pie',
                        radius : ['40%','60%'],
                        data:[
                            {value:335, name:'Pork'},
                            {value:310, name:'Lamb'},
                            {value:234, name:'Chicken'},
                            {value:135, name:'Beef'},
                            {value:548, name:'Fish'}
                       ],
                        itemStyle: {
                            emphasis: {
                                shadowBlur: 10,
                                shadowOffsetX: 0,
                                shadowColor: 'rgba(0, 0, 0, 0.5)'
                            }
                        }
                    }
                ]
            }
        })
    }
</script>

<style scoped>
    .echarts {
        float: left;
        width: 500px;
        height: 400px;
    }
</style>