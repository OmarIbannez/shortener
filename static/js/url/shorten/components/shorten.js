Vue.options.delimiters = ['<%', '%>'];
Vue.component('shorten', {
  template: '#shorten',
  data() {
    return {
      short_urls: [],
    }
  },
  methods: {
    shortenUrl() {
      let self = this;
      let long_url = $(self.$refs.url).val();
      $(self.$refs.url).val('');
      axios.post(window.config.shortenUrlApi, {
        url: long_url,
      }).then(function (response) {
        self.short_urls.push(response.data.short_url);
      }).catch(function (error) {
        alert(error.response.data);
      });
    },
  }
});