(function() {
    var imgur = new Imgur({
        clientid: 'cc86a8de0e7c459',
        callback: feedback
    });
  
  function onSubmit(event, form) {
      if (event) { event.preventDefault(); }
  
        var d = new FormData;
        d.append("image", this.image.value);
  
      //debugger;
        imgur.post(imgur.endpoint, d, imgur.callback);
  }
  
  var form = document.getElementById('linkform');
  form.addEventListener('submit', onSubmit, false);
  form.submit = onSubmit;
    
  })();
  
  
  
  
  var imgur = new Imgur({
              clientid: '',
              callback: feedback
  });
  
  var d = new FormData;
  d.append("image", ""),
  
  imgur.post(imgur.endpoint, d, imgur.callback);