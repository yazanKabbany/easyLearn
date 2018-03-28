function color(cur)
{
    for (i = 1; i <= 5; i++) {
        if (i > cur) {
            $("#star-" + i).addClass("btn-default btn-grey").removeClass("btn-warning");
        }
        else {

            $("#star-" + i).removeClass("btn-default btn-grey").addClass("btn-warning");
        }
    }
}