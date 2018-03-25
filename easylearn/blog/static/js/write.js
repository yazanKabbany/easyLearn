$('#h1-btn').click(
    function()
    {
        var text = $('#post-text').val();
        $('#post-text').val(text+"\n# ").focus();
        //$('#post-text').focus()
    }
)
$('#h2-btn').click(
    function()
    {
        var text = $('#post-text').val();
        $('#post-text').val(text+"\n## ").focus();
    }
)
$('#h3-btn').click(
    function()
    {
        var text = $('#post-text').val();
        $('#post-text').val(text+"\n### ").focus();
    }
)
$('#bold-btn').click(
    function()
    {
        var text = $('#post-text').val();
        $('#post-text').val(text+"**نص غامق**").focus();
    }
)
$('#italic-btn').click(
    function()
    {
        var text = $('#post-text').val();
        $('#post-text').val(text+"*نص مائل*").focus();
    }
)
$('#o-list-btn').click(
    function()
    {
        var text = $('#post-text').val();
        $('#post-text').val(text+"\n1.  عنصر لائحة مرتبة").focus();
    }
)
$('#u-list-btn').click(
    function()
    {
        var text = $('#post-text').val();
        $('#post-text').val(text+"\n+  عنصر لائحة غير مرتبة").focus();
    }
)
