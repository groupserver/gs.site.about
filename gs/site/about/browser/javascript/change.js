jQuery.noConflict();

function gs_site_about_change_init () {
    // This space deliberately left blank.
}

jQuery(window).load( function () {
    gsJsLoader.with_module(['/++resource++popup_help-20071218.js',
                            '/++resource++wymeditor-20090831/jquery.wymeditor.js',
                           '/++resource++gswym.js'],
                           gs_site_about_change_init);
});