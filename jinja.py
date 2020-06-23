
def render_rst_with_jinja(app, docname, source):
    """
    Pass our RST files through the jinja parser.
    This allows us to use all jinja features in all RST templates
    """
    if app.builder.format != 'html':
        return

    final_context = app.config.html_context.copy()
    src = source[0]
    rendered = app.builder.templates.render_string(src, final_context)
    source[0] = rendered
