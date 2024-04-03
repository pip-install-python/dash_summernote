# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dashSummernote <- function(id=NULL, height=NULL, toolbar=NULL, value=NULL) {
    
    props <- list(id=id, height=height, toolbar=toolbar, value=value)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashSummernote',
        namespace = 'dash_summernote',
        propNames = c('id', 'height', 'toolbar', 'value'),
        package = 'dashSummernote'
        )

    structure(component, class = c('dash_component', 'list'))
}
