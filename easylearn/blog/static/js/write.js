$('#h1-btn').click(
    function()
    {
        var text = $('#post-text').val();
        if (!text.endsWith('\n') && text.length != 0)
        {
            text += "\n";
        }
        $('#post-text').val(text+"# ").focus();
        
    }
)
$('#h2-btn').click(
    function()
    {
        var text = $('#post-text').val();
        if (!text.endsWith('\n') && text.length != 0)
        {
            text += "\n";
        }
        $('#post-text').val(text+"## ").focus();
    }
)
$('#h3-btn').click(
    function()
    {
        var text = $('#post-text').val();
        if (!text.endsWith('\n') && text.length != 0)
        {
            text += "\n";
        }
        $('#post-text').val(text+"### ").focus();
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
        if (!text.endsWith('\n') && text.length != 0)
        {
            text += "\n";
        }
        $('#post-text').val(text+"1.  عنصر لائحة مرتبة").focus();
    }
)
$('#u-list-btn').click(
    function()
    {
        var text = $('#post-text').val();
        if (!text.endsWith('\n') && text.length != 0)
        {
            text += "\n";
        }
        $('#post-text').val(text+"+  عنصر لائحة غير مرتبة").focus();
    }
)
