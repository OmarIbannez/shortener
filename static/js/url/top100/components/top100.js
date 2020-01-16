Vue.options.delimiters = ['<%', '%>'];
Vue.component('list-top-100', {
  template: '#list-top-100',
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
      let url = window.config.urlListApi + "?limit=100&ordering=-visits";
      axios.get(url).then(function (response) {
        self.urls = response.data.results;
      });
    },
  }
});