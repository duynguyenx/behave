def before_all(context):
    pass


def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    from browser.browsers import Browser
    context.browser = Browser().make_browser()
    context.browser.maximize_window()


def after_scenario(context, scenario):
    context.browser.quit()


def after_all(context):
    pass
