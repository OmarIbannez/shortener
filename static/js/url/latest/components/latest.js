Vue.options.delimiters = ['<%', '%>'];
Vue.component('list-latest', {
  template: '#list-latest',
  data() {
    return {
      urls: []
    }
  },
  created: function () {
    this.fetchUrls();
  },
  methods: {
    fetchUrls() {
      let self = this;
      let url = window.config.urlListApi + "?limit=100&ordering=-date_added";
      axios.get(url).then(function (response) {
        self.urls = response.data.results;
      });
    },
  }
});