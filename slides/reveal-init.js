// More info https://github.com/hakimel/reveal.js#configuration
Reveal.initialize({
  controls: true,
  progress: true,
  history: true,
  center: true,

  transition: 'slide', // none/fade/slide/convex/concave/zoom

  // More info https://github.com/hakimel/reveal.js#dependencies
  dependencies: [
    { src: '../RevealJS/lib/js/classList.js', condition: function() { return !document.body.classList; } },
    { src: '../RevealJS/plugin/markdown/marked.js', condition: function() { return !!document.querySelector( '[data-markdown]' ); } },
    { src: '../RevealJS/plugin/markdown/markdown.js', condition: function() { return !!document.querySelector( '[data-markdown]' ); } },
    { src: '../RevealJS/plugin/highlight/highlight.js', async: true, callback: function() { hljs.initHighlightingOnLoad(); } },
    { src: '../RevealJS/plugin/zoom-js/zoom.js', async: true },
    { src: '../RevealJS/plugin/notes/notes.js', async: true }
  ]
});
