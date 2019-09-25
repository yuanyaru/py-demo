<template>
    <div>
      <span>{{ serverResponse }} </span>
      <button @click="getData">GET DATA</button>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
		name: "First",
		data: function() {
			return {
				serverResponse: 'resp',
			};
		},
		methods: {
			getData() {
				var that = this;
				// 对应 Python 提供的接口
				const path = 'http://127.0.0.1:5000/getMsg';
				axios.get(path).then(function (response) {
					// 服务器返回的 response 为一个 json object，可通过如下方法需要转成 json 字符串
					var msg = response.data.msg;
					that.serverResponse = msg;

					alert('Success ' + msg);
				}).catch(function (error) {
					alert('Error ' + error);
				});
			},
		},
	};
</script>