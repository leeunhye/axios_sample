// 内容をサーバーとやり取りする。
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'

var vm = new Vue({
  el: '#app',
  delimiters: ['${', '}'], // htmlで
  data: {
    records: [],
    company: '',
    name: '',
    apply_date: '',
    title: '',
    content: '',
    error_list:'',
  },
  created: function() {
    this.find();
  },
  methods: {
    find: function() {
      axios
        .get('/communicate/list/')
        .then(response => (
          this.records = response.data
        ))

      console.log('found!!')
      console.log(this.records)
    },

    approval_create: function() {
      console.log('route_create');

      var postData = {
        company: this.company,
        name: this.name,
        apply_date: this.apply_date,
        title: this.title,
        content: this.content
      };
      axios
        .post('/communicate/create/', postData)
        .then((response) => {
          // 入力値初期化
          alert('サーバーに渡しました。');
          this.company = this.apply_date = this.name = this.title = this.content = this.error_list = '';
          this.find();
        })
        .catch((err) => {
          console.log('post err', err.response.data)
          this.error_list = err.response.data;
        })
    },

  },

})