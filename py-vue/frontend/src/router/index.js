import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import First from '@/components/First'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
		{
				path: '/first',
				name: 'First',
				component: First,
		},
  ],
	// 让 URL 变成http://localhost：8080/ping的形式。如果，不加该设置，默认的 URL 为http://localhost:8080/#/ping的形式。
	mode: 'history',
});
