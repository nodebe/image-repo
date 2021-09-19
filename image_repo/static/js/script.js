$("#src-2").on('change',function() {
 var fileList = this.files; 
 for(var i = 0; i < fileList.length; i++)
 {
    //get a blob 
    var t = window.URL || window.webkitURL;
    var objectUrl = t.createObjectURL(fileList[i]);
    $('#imgs').append('<img src="' + objectUrl + '" class="rounded float-start mb-2 mr-2" width="30%"/>');
    j = i+1;
    if(j % 3 == 0)
    {
      $('#imgs').append('<br>');
    }

 }
});