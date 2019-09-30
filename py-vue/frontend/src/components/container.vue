<template>
<el-container>
    <el-header>
        <span>点表配置工具</span>
    </el-header>

    <el-container>
        <el-aside>
            <el-tree :data="treeData" :props="defaultProps"></el-tree>
        </el-aside>
    
        <el-main>
            <el-table :data="tableData">
                <el-table-column prop="date" label="日期" width="140">
                </el-table-column>
                <el-table-column prop="name" label="姓名" width="120">
                </el-table-column>
                <el-table-column prop="address" label="地址">
                </el-table-column>
            </el-table>
        </el-main>
    </el-container>

    <el-footer>
        <span>@2019  西安端怡科技有限公司</span>
    </el-footer>
</el-container>
</template>

<style>
    html,body,#app,.el-container{
        /* 设置内部填充为0，几个布局元素之间没有间距 */
        padding: 0px;
         /*外部间距也是如此设置*/
        margin: 0px;
        /*统一设置高度为100%*/
        height: 100%;
    }

    .el-header {
        background-color: #003366;
        color: white;
        line-height: 60px;
        text-align: center; 
        font-size: 35px;
    }

    .el-aside {
        background-color: rgb(238, 241, 246);
        color: black;
    }

    .el-footer {
        background-color: #003366;
        color: white;
        text-align: center; 
        line-height: 60px;
    }
</style>

<script>
    import axios from 'axios';

    var that = this;
    // 对应 Python 提供的接口
    const path = 'http://127.0.0.1:5000/getMsg';
    axios.get(path).then(function (response) {
        // 服务器返回的 response 为一个json object，可通过如下方法需要转成json字符串
        var staLen = response.data.staLen;
        var staValue = response.data.staValue;
        console.log(staValue);
        var staValue_array = staValue.split(",");
        // console.log(staLen);
        console.log(staValue_array[1]);
    });

    export default {
        data() {
            const item = {
                date: '2016-05-02',
                name: '王小虎',
                address: '上海市普陀区金沙江路 1518 弄'
            };
            return {
                treeData: [{
                    label: '厂站列表',
                    children: [{
                        label: '厂站名',
                        children: [{
                            label: '遥信',
                        }, {
                            label: '遥测',  
                        }, {
                            label: '遥控',
                        }, {
                            label: '遥调',
                        }, {
                            label: 'SOE',
                        }]
                    }]
                }],
                defaultProps: {
                    children: 'children',
                    label: 'label'
                },
                tableData: Array(10).fill(item),
            };
        },
    };
</script>