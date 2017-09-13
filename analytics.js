(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

ga('create', 'UA-106206386-1', 'auto');
ga('send', 'pageview');
var pageLoad = Date.now();
            
var trackOutboundLink = function(event) {
  var options = {
    eventCategory: document.title,
    eventAction: 'outbound',
    eventLabel: event.currentTarget.href,
    eventValue: Date.now() - pageLoad,
    transport: 'beacon'
  };

  if(event.currentTarget.target !== '_blank') {
    options.hitCallback = function() {
      document.location = event.currentTarget.href;
    };

    event.preventDefault();
  }

  ga('send', 'event', options);
}

var anchorTags = document.querySelectorAll('a');
for(var i = 0; i < anchorTags.length; i++) {
  anchorTags[i].target = '_blank'; // don't want to lose this page
  anchorTags[i].addEventListener('click', trackOutboundLink);
}
